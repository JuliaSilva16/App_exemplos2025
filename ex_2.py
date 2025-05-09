import flet as ft
from flet import AppBar, ElevatedButton,Text, View
from flet.core import page
from flet.core.colors import Colors

class User():
    def __init__(self, titulo,descricao,categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor

def main(page: ft.Page):
    page.title = "Livros"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    lista = []

    def salvar_livros(e):
        if input_titulo.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_user = User(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
                autor=input_autor.value
            )
            lista.append(obj_user)
            input_titulo.value = ''
            input_descricao.value = ''
            input_categoria.value = ''
            input_autor.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_nome.controls.clear()
        for user in lista:
            lv_nome.controls.append(
                ft.Text(value=
                        f"Título:{user.titulo} \n "
                        f"Descrição: {user.descricao} \n"
                        f"Categoria: {user.categoria} \n"
                        f"Autor: {user.autor} \n\n"

                        )
            )
        page.update()

    def vizualizar_detalhe(e):
        for livro in lista:
            lv_nome.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(f"{livro.titulo}"),
                    subtitle=ft.Text(f"{livro.autor}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Detalhes", on_click=lambda _: page.go("/terceira"))
                        ]
                    )
                )
            )

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,input_descricao, input_categoria, input_autor,
                    ft.Button(text='Salvar', on_click=lambda _: salvar_livros(e)),
                    ft.Button(text='Exibir Lista', on_click=lambda _: page.go('/segunda')),
                ],
            )
        )

        if page.route == "/segunda" or page.route == "/terceira":
            vizualizar_detalhe(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("LIVROS"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                    ],
                )
            )
        page.update()


        if page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("DETALHES "), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                    ],
                )
            )
        page.update()





    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    input_titulo = ft.TextField(label="Digite o título: ")
    input_descricao = ft.TextField(label="Digite a descrição: ")
    input_categoria = ft.TextField(label="Digite a categoria: ")
    input_autor = ft.TextField(label="Digite o autor: ")
    msg_sucesso = ft.SnackBar(content=ft.Text("Salvo com sucesso!"), bgcolor=Colors.GREEN)
    msg_error = ft.SnackBar(content=ft.Text("Não pode estar vazio!"), bgcolor=Colors.RED)

    lv_nome = ft.ListView(
        height=500
    )

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)
import flet as ft
from flet import AppBar,Text, View
from flet.core.colors import Colors
from sqlalchemy import select

from models import *

def main(page: ft.Page):
    page.title = "Livros"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    lista = []

    def salvar_livros(e):
        if input_titulo.value == '' or input_descricao.value == '' or input_categoria.value == '' or input_autor.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            livros = Livro (
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
                autor=input_autor.value
            )
            livros.save()
            input_titulo.value = ''
            input_descricao.value = ''
            input_categoria.value = ''
            input_autor.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def detalhes (titulo,descricao,categoria,autor):
        txt_titulo.value = titulo
        txt_descricao.value = descricao
        txt_categoria.value = categoria
        txt_autor.value = autor

        page.go("/detalhes_livro")

    def exibir_lista(e):
        lv.controls.clear()
        sql_livro = select(Livro)
        resultado_livro = db_session.execute(sql_livro).scalars()

        for livro in resultado_livro:
            lv.controls.append(
                ft.ListTile(
                    title=ft.Text(f"Título: {livro.titulo}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Ver", on_click=lambda _, l=livro: detalhes(l.titulo, l.descricao, l.categoria, l.autor)),
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
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ft.Button(
                        text='Salvar', on_click=lambda _: salvar_livros(e)),
                    ft.Button(
                        text='Exibir Lista', on_click=lambda _: page.go('/lista_livro')),
                ],
            )
        )

        if page.route == "/lista_livro" or page.route == "/detalhes_livro":
            exibir_lista(e)
            page.views.append(
                View(
                    "/lista_livro",
                    [
                        AppBar(title=Text("LIVROS"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv,
                    ]
                )
            )

        if page.route == "/detalhes_livro":
            page.views.append(
                View(
                    "/detalhes_livro",
                    [
                        AppBar(title=Text("DETALHES "), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_titulo,
                        txt_descricao,
                        txt_categoria,
                        txt_autor,
                    ]
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
    lv = ft.ListView(
        height=500
    )
    msg_sucesso = ft.SnackBar(
        content=ft.Text('Salvo com sucesso!'),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text('Não pode estar vazio!'),
        bgcolor=Colors.RED
    )

    txt_titulo = ft.Text
    txt_descricao = ft.Text
    txt_categoria = ft.Text
    txt_autor = ft.Text

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)
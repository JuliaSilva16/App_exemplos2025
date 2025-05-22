import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from sqlalchemy import select
from  models import *


def main(page: ft.Page):
    page.title = "Exemplo de Listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def salvar(e):
        if input_nome.value == "" or input_profissao.value == "" or input_salario.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()

        else:
            salario = input_salario.value

            if not salario.isnumeric():
                input_salario.error = True #verificar se é número
                input_salario.error_text = "Apenas números"
                page.update()
                return

            informacoes_usuario = Usuario(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=salario
            )

            informacoes_usuario.save()
            input_nome.value = ""
            input_profissao.value = ""
            input_salario.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def detalhe (nome,profissao,salario):
        txt_nome.value = nome
        txt_profissao.value = profissao
        txt_salario.value = salario

        page.update()
        page.go("/detalhe_usuario")

    def usuario(e):
        lv.controls.clear()
        sql_usuarios = select(Usuario)
        resultado_usuario = db_session.execute(sql_usuarios).scalars()

        for usuario in resultado_usuario:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome:{usuario.nome}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="DETALHES",on_click=lambda _, u=usuario: detalhe(u.nome,u.profissao,u.salario)),
                        ]
                    )
                )
            )

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("USÚARIO: CADASTRO"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_profissao,
                    input_salario,
                    ft.Button(
                        "Salvar",
                        on_click=lambda _: salvar(e)),
                    ft.Button(
                        "Exibir lista",
                        on_click=lambda _: page.go("/lista_usuario")
                    )
                ],

            )
        )
        if page.route == "/lista_usuario" or page.route == "/detalhe_usuario":
            usuario(e)
            page.views.append(
                View(
                    "/lista_usuario",
                    [
                        AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv,
                    ],
                )
            )

        if page.route == "/detalhe_usuario":
            page.views.append(
                View  (
                    "/detalhe usuario",
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_nome,
                        txt_profissao,
                        txt_salario,
                    ]
                )
            )
        page.update()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

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

    txt_nome = ft.Text()
    txt_profissao = ft.Text()
    txt_salario = ft.Text()

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)
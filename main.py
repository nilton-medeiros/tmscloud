import flet as ft

from pages.landing.landing_page import LandingPage
from pages.login import Login
from pages.signup import Signup


class AppTheme:
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            background='#20202a',
            on_background='#2d2d3a',
            on_inverse_surface='#2d2d3a',
            primary=ft.colors.INDIGO,
        ),
        text_theme=ft.TextTheme(
            body_large=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                size=14,
            ),
            body_medium=ft.TextStyle(
                weight=ft.FontWeight.NORMAL,
                color=ft.colors.GREY,
                size=14,
            ),
            headline_large=ft.TextStyle(
                weight=ft.FontWeight.W_900,
                color=ft.colors.WHITE,
                size=50,
            ),
            label_large=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.colors.WHITE,
                size=16,
            ),
            headline_medium=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.colors.WHITE,
                size=30,
            )
        ),
        font_family="Roboto",
        # scrollbar_theme=ft.ScrollbarTheme(
        #     track_visibility=False,
        #     thumb_visibility=False,
        #     track_color={
        #         ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
        #     },
        #     thumb_color={
        #         ft.ControlState.HOVERED: ft.colors.TRANSPARENT,
        #         ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
        #     }
        # )
    )


def main(page: ft.Page):
    if not hasattr(page, 'sessions_data'):
        page.sessions_data = {}

    page.theme = AppTheme.theme
    page.title = "TMS.CLOUD"
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.min_width = 300
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.colors.BLUE_GREY_900

    page.fonts = {
        'Roboto Bold': 'fonts/Roboto-Bold.ttf',
        'Roboto Medium': 'fonts/Roboto-Medium.ttf',
        "Roboto Regular": "fonts/Roboto-Regular.ttf",
    }

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        pg_view = None

        match e.route:
            case '/':
                landing_page = LandingPage(page)
                pg_view = ft.View(
                    route='/',
                    controls=[landing_page],
                    appbar=page.appbar,
                    vertical_alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            case '/logout':
                # page.sessions_data.clear()
                page.route = '/'
            case '/login':
                pg_view = ft.View(route='/login', controls=[Login(page)])
            case '/signup':
                pg_view = ft.View(route='/signup', controls=[Signup(page)])
            case _:
                # Opcional: tratamento para rotas não encontradas
                pg_view = ft.View(
                    route="/404",
                    controls=[
                        ft.AppBar(title=ft.Text("Página não encontrada"),
                            bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("404 - Página não encontrada", size=30),
                        ft.ElevatedButton("Voltar para Início",
                                    on_click=lambda _: page.go("/"))
                    ]
                )

        page.views.append(pg_view)
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")

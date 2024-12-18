import flet as ft

from pages.landing.landing_page import LandingPage
from pages.login import Login


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
    page.window.min_width = 300
    page.bgcolor = ft.colors.BLUE_GREY_900

    page.fonts = {
        'Roboto Bold': 'fonts/Roboto-Bold.ttf',
        'Roboto Medium': 'fonts/Roboto-Medium.ttf',
        "Roboto Regular": "fonts/Roboto-Regular.ttf",
    }

    def routes(e):
        page.controls.clear()

        try:
            route = page.route

            if route == '/':
                LandingPage(page).build()
            elif route == 'logout':
                # page.sessions_data.clear()
                page.route = '/'
                page.update()

            if route == 'login':
                Login(page)
            elif route == 'register':
                # Implementar a página de registro
                #
                page.add(ft.SnackBar(ft.Text("Página de registro"), open=True))

            page.update()

        except Exception as e:
            print(f"Error routing: {e}")
            page.go('/')

    page.on_route_change = routes

    page.go('/')
    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")

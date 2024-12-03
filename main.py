import flet as ft

from pages.landing_page import LandingPage


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


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.theme = AppTheme.theme

        self.page.theme = self.theme
        self.page.title = "TMS.CLOUD"
        # self.page.padding = 0
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # As configurações iniciais da página é da LandingPage que não usa o padrão do Thema,
        # que será usado a partir da Home (dashboard) e demais páginas do sistema TMS com usuário logado

        # window_min_width: Somente modo Desktop, mobile e tablets. Não funciona modo web
        self.page.window.min_width = 300
        self.page.bgcolor = ft.colors.BLUE_GREY_900

        self.landingpg = LandingPage(self.page)
        self.page.add(*self.landingpg.build())


if __name__ == '__main__':
    ft.app(target=App, assets_dir="assets")

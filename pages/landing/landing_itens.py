import flet as ft


class MainContentItem():
    def __init__(self, title: str, description: str, image: str, image_size: int = 0, image_left=True, url: str = None, tooltip: str = None):
        self.title = title
        self.description = description
        self.image_left = image_left
        self.image = ft.Image(src=image, border_radius=5, fit=True)
        self.image_size = image_size
        self.url = url
        self.tooltip = tooltip

    def build(self):
        if self.url:
            description = ft.Column(
                controls=[
                    ft.Text(value=self.title,
                            theme_style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(name=ft.icons.LINK,
                                        color=ft.colors.WHITE30),
                                ft.Text(
                                    value=self.description,
                                    theme_style=ft.TextThemeStyle.TITLE_SMALL,
                                    color=ft.colors.WHITE54
                                ),
                            ],
                            tight=True,
                        ),
                        url=self.url,
                        tooltip=self.tooltip,
                    ),
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
            description = ft.Column(
                controls=[
                    ft.Text(value=self.title,
                            theme_style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.Text(value=self.description,
                            theme_style=ft.TextThemeStyle.TITLE_SMALL,
                            color=ft.colors.WHITE54),
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.CENTER,
            )

        if self.image_size > 0:
            self.image.width = self.image_size

        image_ctnr = ft.Container(
            # margin=ft.margin.only(top=20, bottom=20),
            margin=ft.margin.all(50),
            content=self.image,
            col={"md": 5},
            alignment=ft.alignment.center
        )

        descr_ctnr = ft.Container(
            # margin=ft.margin.only(top=20, bottom=20),
            margin=ft.margin.all(50),
            content=description,
            col={"md": 7},
            alignment=ft.alignment.center
        )

        side_left = image_ctnr if self.image_left else descr_ctnr
        side_right = descr_ctnr if self.image_left else image_ctnr
        bgcolor = ft.colors.BLUE_GREY_700 if self.image_left else ft.colors.BLUE_GREY_800

        return ft.Container(
            bgcolor=bgcolor,
            border_radius=10,
            # margin=ft.margin.only(top=40),
            expand=True,
            content=ft.ResponsiveRow(
                controls=[side_left, side_right],
                spacing=20,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

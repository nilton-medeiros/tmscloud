import flet as ft

class MainContentItem():
    def __init__(self, title: str, description: str, image: str, image_left=True):
        self.title = title
        self.description = description
        self.image_left = image_left
        self.image = ft.Image(
            src=image,
            # width=750,
            # height=300,
            # fit=ft.ImageFit.CONTAIN,
        )

    def build(self):
        description = ft.Column(
            controls=[
                ft.Text(value=self.title,
                        theme_style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Text(value=self.description,
                        theme_style=ft.TextThemeStyle.TITLE_SMALL),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        image_ctnr = ft.Container(
            content=self.image,
            col={"md": 5},
            alignment=ft.alignment.center
        )
        descr_ctnr = ft.Container(
            content=description,
            col={"md": 7},
            alignment=ft.alignment.center
        )

        side_left = image_ctnr if self.image_left else descr_ctnr
        side_right = descr_ctnr if self.image_left else image_ctnr
        bgcolor = ft.colors.BLUE_GREY_700 if self.image_left else ft.colors.BLUE_GREY_800

        return ft.Container(
            content=ft.ResponsiveRow(
                controls=[side_left, side_right],
                spacing=20,
                # run_spacing={"xs": 10},
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=40),
            bgcolor=bgcolor,
            padding=20,
            border_radius=10,
            alignment=ft.alignment.center,
        )

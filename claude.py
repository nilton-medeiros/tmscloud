import flet as ft


def main(page: ft.Page):
    page.title = "By Claude"
    page.theme_mode = "light"
    page.padding = 50

    def go_to_app():
        page.route = "/app"
        page.update()

    def go_to_login():
        page.route = "/login"
        page.update()

    def go_to_signup():
        page.route = "/signup"
        page.update()

    header = ft.Row(
        controls=[
            ft.Text("My App", size=24, weight="bold"),
            ft.Row(
                controls=[
                    ft.TextButton("Login", on_click=lambda _: go_to_login()),
                    ft.TextButton("Sign Up", on_click=lambda _: go_to_signup())
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    hero = ft.Column(
        controls=[
            ft.Image(src="https://via.placeholder.com/600x400",
                     width=600, height=400),
            ft.Text("Discover the power of our app", size=24)
        ],
        alignment=ft.CrossAxisAlignment.CENTER
    )

    features = ft.Column(
        controls=[
            ft.Text("Key Features:", size=24, weight="bold"),
            ft.Row(
                controls=[
                    ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE,
                            color=ft.colors.GREEN),
                    ft.Text("Feature 1")
                ]
            ),
            ft.Row(
                controls=[
                    ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE,
                            color=ft.colors.GREEN),
                    ft.Text("Feature 2")
                ]
            ),
            ft.Row(
                controls=[
                    ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE,
                            color=ft.colors.GREEN),
                    ft.Text("Feature 3")
                ]
            )
        ]
    )

    footer = ft.Row(
        controls=[
            ft.Text("© 2023 My App. All rights reserved.")
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        header,
        hero,
        features,
        footer
    )


ft.app(target=main)

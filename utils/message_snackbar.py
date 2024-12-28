import flet as ft


def message_snackbar(page: ft.Page, message: str, msg_error: bool = True):
    bg_color = ft.colors.RED_100 if msg_error else ft.colors.GREEN_100
    icon_color = ft.colors.RED if msg_error else ft.colors.GREEN

    snack_bar = ft.SnackBar(
        content=ft.Text(message),
        bgcolor=bg_color,
        show_close_icon=True,
        close_icon_color=icon_color,
        padding=ft.padding.all(10),
        duration=10000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.margin.all(10),
    )

    page.overlay.append(snack_bar)
    page.update()
    snack_bar.open = True  # Abre o SnackBar após adicioná-lo
    page.update()

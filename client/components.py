import flet as ft


def get_match_card(match_event):
    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text(f"{match_event["teams"]}", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(f"End Time: {match_event["end_datetime"]}", size=16),
                ft.Text(f"Score: {match_event["result_score"]}", size=16)
            ]),
            padding=ft.padding.all(10),
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=5,
                color=ft.colors.with_opacity(0.2, ft.colors.BLACK),
                offset=ft.Offset(0, 3)
            )
        ),
        elevation=3,
        margin=ft.margin.all(10)
    )

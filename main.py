import flet as ft

def main(page: ft.Page):
    page.title = "Моё первое Flet приложение"
    page.add(ft.Text("Привет, Flet!"))

ft.app(target=main)

import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    greeting_text = ft.Text("Hello world")
    greeting_history = ft.Column()
    
    dark_mode = False  


    def toggle_theme(e):
        nonlocal dark_mode
        dark_mode = not dark_mode
        page.theme_mode = ft.ThemeMode.DARK if dark_mode else ft.ThemeMode.LIGHT
        theme_button.text = "Dark" if dark_mode else "Light"
        page.update()

    def get_greeting_by_hour(hour: int) -> str:
        if 6 <= hour < 12:
            return "Доброе утро"
        elif 12 <= hour < 18:
            return "Добрый день"
        elif 18 <= hour < 23:
            return "Добрый вечер"
        else:
            return "Спокойной ночи"

    def on_button_click(e):
        name = name_input.value.strip()
        age_str = age_input.value.strip()
        try:
            age = int(age_str)
        except ValueError:
            greeting_text.value = "Возраст должен быть числом!"
            greeting_text.color = ft.Colors.RED
            page.update()
            return
        
        now = datetime.now()
        timestamp = now.strftime("%H:%M")
        hour = now.hour

        if name:
            greeting = get_greeting_by_hour(hour)
            greeting_text.value = f"{timestamp} — {greeting}, {name}, вам {age} лет!"
            greeting_text.color = ft.Colors.BLACK
            greeting_history.controls.insert(0, ft.Text(f"{timestamp} — {greeting}, {name}, {age} лет"))
       
            name_input.value = None
            age_input.value = None
        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)
    age_input = ft.TextField(label="Введите ваш возраст", keyboard_type=ft.KeyboardType.NUMBER)
    name_button = ft.ElevatedButton("Отправить", icon=ft.Icons.SEND, on_click=on_button_click)

    theme_button = ft.ElevatedButton(text="Light", on_click=toggle_theme)

    page.add(
        greeting_text,
        ft.Row([name_input, age_input, name_button, theme_button], alignment=ft.MainAxisAlignment.START),
        ft.Text("История приветствий:"), 
        greeting_history
    )

ft.app(target=main, view=ft.WEB_BROWSER)





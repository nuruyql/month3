import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Приветствия с любимыми именами и фильтром"
    
    greeting_text = ft.Text("Hello world")
    greeting_history = ft.Column()
    favorite_names = ft.Column()
    all_greetings = []  
    dark_mode = False  

   
    try: 
        with open("history.txt","r",encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
            for line in reversed(lines):
                greeting_history.controls.append(ft.Text(line))
                all_greetings.append(line)
    except FileNotFoundError:
        pass

  
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
        
        if not name:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED
            page.update()
            return

        now = datetime.now()
        timestamp = now.strftime("%H:%M")
        hour = now.hour
        greeting = get_greeting_by_hour(hour)
        gr_full = f"{timestamp} — {greeting}, {name}, вам {age} лет!"

        greeting_text.value = gr_full
        greeting_text.color = ft.Colors.BLACK

  
        all_greetings.insert(0, gr_full)
        greeting_history.controls.insert(0, ft.Text(gr_full))

      
        try:
            with open("history.txt", "a", encoding="utf-8") as file:
                file.write(gr_full + "\n")
        except Exception as ex:
            greeting_text.value = f"Ошибка записи: {ex}"
            greeting_text.color = ft.Colors.RED

        name_input.value = ""
        age_input.value = ""
        page.update()

    def add_to_favorites(e):
        if all_greetings:
            last_greeting = all_greetings[0]
            name_part = last_greeting.split(",")[1].strip()  # берём имя
            favorite_names.controls.insert(0, ft.Text(name_part))
            page.update()


    def filter_morning(e):
        greeting_history.controls.clear()
        for g in all_greetings:
            time_str = g.split(" — ")[0]
            hour = int(time_str.split(":")[0])
            if hour < 12:
                greeting_history.controls.append(ft.Text(g))
        page.update()

    def filter_evening(e):
        greeting_history.controls.clear()
        for g in all_greetings:
            time_str = g.split(" — ")[0]
            hour = int(time_str.split(":")[0])
            if hour >= 12:
                greeting_history.controls.append(ft.Text(g))
        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)
    age_input = ft.TextField(label="Введите ваш возраст", keyboard_type=ft.KeyboardType.NUMBER)
    name_button = ft.ElevatedButton("Отправить", icon=ft.Icons.SEND, on_click=on_button_click)
    theme_button = ft.ElevatedButton(text="Light", on_click=toggle_theme)
    favorite_button = ft.ElevatedButton("Добавить в избранное", on_click=add_to_favorites)
    morning_button = ft.ElevatedButton("Утренние", on_click=filter_morning)
    evening_button = ft.ElevatedButton("Вечерние", on_click=filter_evening)

    page.add(
        greeting_text,
        ft.Row([name_input, age_input, name_button, theme_button]),
        ft.Row([favorite_button, morning_button, evening_button]),
        ft.Text("История приветствий:"), 
        greeting_history,
        ft.Text("Любимые имена:"),
        favorite_names
    )

ft.app(target=main, view=ft.WEB_BROWSER)

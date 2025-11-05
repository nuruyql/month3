import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text("Hello world")
    greeting_history = []

    
    def on_button_click(_):
        name = name_input.value.strip()
        greeting_text.value = f"Hello! {name}"
        timestamp = datetime.now().strftime("%H:%M")
        
        if name:
            greeting_text.value =  f"{timestamp} Hello! {name}"
            name_input.value = None
            greeting_history.append(timestamp + "-" + name)
        else:
            greeting_text.value = "enter correct name"
            greeting_text.color = ft.Colors.RED
        
        
        
        
        
        
        
        
        
        page.update()
        
        
    name_input = ft.TextField(label='Введите имя',on_submit=on_button_click)

    name_button = ft.ElevatedButton('send', icon=ft.Icons.SEND,on_click=on_button_click)
 

    page.add(greeting_text, name_input, name_button)


ft.app(target=main, view=ft.WEB_BROWSER)
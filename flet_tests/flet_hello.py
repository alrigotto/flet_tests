import time
import flet as ft

def main(page: ft.Page):
    # page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.title = "Andre APP"
    t = ft.Text(value="Hello, world!", color="blue", size=30)
    page.controls.append(t)
    page.bgcolor = "#010101"
    page.window_always_on_top = False
    # page.window.left = 200
    # page.window.top = 200
    # page.height = 200
    # page.width = 200
    
    page.update()
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=230)
    new_task_2 = ft.TextField(hint_text="done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked), new_task_2]))
    
    
    # for i in range(10):
    #     t.value = f"Step {i}"
    #     page.update()
    #     time.sleep(1)
    
    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.3)
    
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
    
    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
    
    page.add(
    ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ])
)
    
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)

ft.app(main)
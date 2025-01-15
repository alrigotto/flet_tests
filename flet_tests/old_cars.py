import flet as ft
from database_cars import cars

def main(page: ft.Page):
    
    def clicar(e):
        dialog = ft.AlertDialog(
            title = ft.Text("André"),
            actions = [
                ft.TextButton("Fechar", on_click = lambda e: page.close(dialog))
            ]
        )
        page.open(dialog)
        
    def check_item_clicked(e): ## Toggle the checkmark symbol on and off
        e.control.checked = not e.control.checked
        page.update()
        
    def show_car_description(e):
        car = next((car for car in cars if car["id"] == e.control.parent.key), None)
        dialog = ft.AlertDialog(
            title = ft.Text(car["descricao"]),
            actions = [
                ft.TextButton("Fechar", on_click = lambda e: page.close(dialog))
            ]
        )
        page.open(dialog)
    
    
    
    page.title = "Carros"
    page.window.height = 800
    page.window.width = 400
    
    
    app_bar = ft.AppBar(
        leading = ft.Icon(ft.Icons.DIRECTIONS_CAR_FILLED),
        leading_width = 40,
        title = ft.Text("Carros"),
        center_title = True,
        bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions = [
            ft.IconButton(
                icon = ft.Icons.NOTIFICATIONS,
            ),
            ft.PopupMenuButton(
                items = [
                    ft.PopupMenuItem(
                        icon = ft.Icons.PERSON,
                        text = "Perfil",
                        on_click = clicar
                    ),
                    ft.PopupMenuItem(
                        icon = ft.Icons.SETTINGS,
                        text = "Configurações",
                        on_click = clicar
                    ),
                    ft.PopupMenuItem(), # This is just to make a separator line
                    ft.PopupMenuItem(
                        text = "Mostrar todos",
                        on_click = check_item_clicked
                    )
                ]
                
            )
        ]
    )
    
    cars_list = ft.Column(
        scroll = ft.ScrollMode.ALWAYS,
        expand = True,
    )
    
    for car in cars:
        car_component = ft.ListTile(
            leading = ft.Image(
                src = car["foto"],
                fit = ft.ImageFit.COVER,
                repeat = ft.ImageRepeat.NO_REPEAT,
                height = 100,
                width = 80,
                border_radius = 5,
            ),
            title = ft.Text(f'{car["modelo"]} - {car["marca"]}'),
            subtitle = ft.Text(car["ano"],),
            trailing = ft.PopupMenuButton(
                key = car["id"],
                icon = ft.icons.MORE_VERT,
                items = [
                    ft.PopupMenuItem(
                        icon = ft.icons.REMOVE_RED_EYE_SHARP,
                        text = "Ver Descrição",
                        on_click = show_car_description,
                    ),
                    ft.PopupMenuItem(
                        icon = ft.icons.DELETE,
                        text = "Deletar",
                        # on_click = ,
                    )
                ]
            )
        )
        cars_list.controls.append(car_component)
    
    nav_bar = ft.NavigationBar(
        destinations = [
            ft.NavigationBarDestination(
                icon = ft.Icons.DIRECTIONS_CAR_FILLED_OUTLINED,
                label = "Usados",
            ),
            ft.NavigationBarDestination(
                icon = ft.Icons.CAR_RENTAL,
                label = "Novos",
            ),
            ft.NavigationBarDestination(
                icon = ft.Icons.ELECTRIC_CAR_OUTLINED,
                label = "Elétrico",
            )
        ]
    )    
    
    page.add(
        app_bar,
        nav_bar,
        cars_list,
    )
    




ft.app(main)


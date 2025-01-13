import flet as ft

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
        nav_bar
    )
    




ft.app(main)


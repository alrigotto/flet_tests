import flet as ft

def main(page: ft.Page):
    
    test_icons = ft.Icon(
        name = ft.icons.FAVORITE,
        color = ft.colors.PINK,
        size = 60,
        tooltip = "Andre", 
    )
    
    # Creating btn styles
    my_btn_style = ft.ButtonStyle(
        color = {
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
            ft.MaterialState.HOVERED: ft.colors.YELLOW_ACCENT_400,        
        },
        bgcolor = {
            ft.MaterialState.DEFAULT: ft.colors.RED_ACCENT_100,
            ft.MaterialState.HOVERED: ft.colors.YELLOW_ACCENT_400,        
        },
        animation_duration = 500
    )
    
    config_icon = ft.Icon(
        name = ft.icons.SETTINGS,
        color = ft.colors.GREEN_ACCENT,
        size = 60,
        tooltip = "Config"
    )
    
    e_btn = ft.ElevatedButton(
        text = "Go to Flet docs!",
        # color = ft.colors.YELLOW_700,
        icon = ft.icons.ADS_CLICK_ROUNDED,
        icon_color = ft.colors.BLUE_400,
        url = "https://flet.dev/",
        tooltip = "Docs!",
        style = my_btn_style,
    )
    
    f_btn = ft.FilledButton(
        icon = ft.icons.SAFETY_CHECK,
        text = "Aqui!",
        style = ft.ButtonStyle(
            bgcolor = ft.colors.WHITE12,
            color = ft.colors.GREEN_300,
            padding = 10,
            text_style = ft.TextStyle(size = 32),
            icon_size = 40,            
        ),
    )
    
    
    page.add(       # adding in the page   the components that were created
        test_icons,
        config_icon,
        e_btn,
        f_btn,
    )

ft.app(main)
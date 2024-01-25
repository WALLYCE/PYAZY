from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import flet as ft

global navegador
navegador = None  # Inicialize o navegador como None

def init(e):
    global navegador
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    navegador.get("https://web.whatsapp.com/")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    mensatem = """Teste 
    123"""

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 800
    page.window_resizable = False
    color_status = 'red300'
    page.add(
         ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text("Desconectado", size= 20, weight=ft.FontWeight.W_900, selectable=True),
                    height=30,
                    expand=True,
                    alignment=ft.alignment.center,
                    bgcolor=color_status,
                    border=ft.border.all(2, ft.colors.GREY_500),
                    
                )
            ]
         ),
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.ResponsiveRow(
                        [
                            ft.IconButton(
                                icon=ft.icons.QR_CODE_SCANNER_ROUNDED,
                                icon_color="GREEN600",
                                icon_size=80,
                                tooltip="Iniciar Whatsapp",
                                col={"sm": 6, "md": 4, "xl": 2},
                                on_click=init
                            ),
                            ft.IconButton(
                                icon=ft.icons.PLAY_CIRCLE,
                                icon_color="BLUE600",
                                icon_size=80,
                                tooltip="Iniciar envio",
                                col={"sm": 6, "md": 4, "xl": 2},
                            ),
                            ft.IconButton(
                                icon=ft.icons.STOP_CIRCLE_OUTLINED,
                                icon_color="pink600",
                                icon_size=80,
                                tooltip="Parar",
                                col={"sm": 6, "md": 4, "xl": 2},
                            ),
                        ],
                    ),
                    height=100,
                    expand=True,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.LIGHT_GREEN_100,
                    border=ft.border.all(2, ft.colors.GREY_500),
                )
            ]
        )
    )

    page.update()

ft.app(target=main)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import flet as ft
global navegador

def main(page: ft.Page):
    page.window_width = 800        # window's width is 200 px
    page.window_height = 800       # window's height is 200 px
    page.window_resizable = False  # window is not resizable

    row_1 = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    

    row_1.controls.append(
        ft.Container(
            height=200,
            expand= True,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.AMBER_200,
            border=ft.border.all(2, ft.colors.AMBER_600)
        )
    )
    page.add(row_1)
    page.update()


ft.app(target=main)


def init():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    navegador = webdriver.Chrome(service=service, options=options)

    navegador.get("https://web.whatsapp.com/")


    mensatem = """Teste 
    123"""

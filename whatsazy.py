from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    border_radius,
    colors,
    border,
    UserControl,
    IconButton,
    alignment,
    icon,
    ResponsiveRow,
    icons,
    FontWeight
)
import time

global navegador
global page
page = None


navegador = None  # Inicialize o navegador como None
container_status = None
text_status = None



class WhastApp(UserControl):

    def build(self, page):
        self.page = page
        self.text_status = Text("Desconectado", size= 20, weight= FontWeight.W_900, selectable=False);
        self.container_status = Container(
            content=self.text_status,
            height=30,
            expand=True,
            alignment=alignment.center,
            bgcolor='red300',
            border= border.all(2, colors.GREY_500),
        )
        self.button_qrcode = IconButton(
            icon=icons.QR_CODE_SCANNER_ROUNDED,
            icon_color="GREEN600",
            icon_size=80,
            tooltip="Iniciar Whatsapp",
            col={"sm": 6, "md": 4, "xl": 2},
            on_click=self.IniciaWhatsapp
        )
        return Container(
                           
                content=Column(

                controls=[
                ResponsiveRow(
                    
                       controls=[self.container_status]
                    
                ),
                ResponsiveRow(
                    [
                        Container(
                             height=100,
                            expand=True,
                            alignment=alignment.center,
                            bgcolor=colors.LIGHT_GREEN_100,
                            border=border.all(2, colors.GREY_500),
                            content=Column(
                            controls=[
                            ResponsiveRow(
                                controls=[
                                    self.button_qrcode,
                                    IconButton(
                                        icon=icons.PLAY_CIRCLE,
                                        icon_color="BLUE600",
                                        icon_size=80,
                                        tooltip="Iniciar envio",
                                        col={"sm": 6, "md": 4, "xl": 2},
                                    ),
                                    IconButton(
                                        icon=icons.STOP_CIRCLE_OUTLINED,
                                        icon_color="pink600",
                                        icon_size=80,
                                        tooltip="Parar",
                                        col={"sm": 6, "md": 4, "xl": 2},
                                    ),
                                ],
                            )]),
                         
                        )
                    ]
                )
                ])
            )
   

    def IniciaWhatsapp(self, e):
        self.navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.navegador.get("https://web.whatsapp.com/")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.text_status.value ='Conectado'
        self.text_status.update()
        self.container_status.bgcolor= 'green300'
        self.container_status.update()
        
   
        
        
       
   
def main(page: Page):                                                        
    page.window_width = 800
    page.window_height = 800
    page.window_resizable = False
    whats = WhastApp()
    page.add(whats.build(page))
    page.update()

flet.app(target=main)

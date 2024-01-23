from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
global navegador

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(service=service, options=options)

navegador.get("https://web.whatsapp.com/")


mensatem = """Teste 
 123"""
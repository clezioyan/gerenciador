from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurações
smart_tv_club_url = "https://smartclub.tv/pt/update-playlist/"
mac_address = "3328-c68a-8a88-b4fd"

# Inicializar o WebDriver (usando Chrome headless)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

try:
    # Navegar para a página de atualização do Smart TV Club
    driver.get(smart_tv_club_url)

    # Esperar a página carregar (você pode precisar ajustar o tempo de espera)
    time.sleep(5)

    # Encontrar o campo do MAC address e inserir o MAC
    mac_input = driver.find_element(By.NAME, "mac")
    mac_input.clear()
    mac_input.send_keys(mac_address)

    # Encontrar o botão de atualização e clicar nele
    update_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    update_button.click()

    # Esperar a página processar a atualização (ajuste conforme necessário)
    time.sleep(10)

finally:
    # Fechar o navegador
    driver.quit()

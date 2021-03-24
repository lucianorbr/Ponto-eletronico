from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

# Login/senha
login = "login"
password = "senha"

# Inicializacao do driver Chrome
driver = webdriver.Chrome()

# Abrindo a pagina folha de ponto
driver.get("http://portaldoconsultor.altran.com.br/login")

# Entrada do nome do usuário / email
elmnt = driver.find_element_by_id("user_session_email")
elmnt.send_keys(login)

# Entrada da senha
elmnt = driver.find_element_by_id("user_session_password")
elmnt.send_keys(password)

# Pressionando o botão de login
elmnt.send_keys(Keys.ENTER)

elmnt = driver.find_element_by_xpath('//*[@id="button_begin_period_one"]').click()
pyautogui.press(['enter'])

# Fechando o driver
driver.close()

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# Create your tests here.
class test_anonymoususerinfo(LiveServerTestCase):


    

  def test_anonymoususerinfo(self):
    selenium = webdriver.Chrome('D:\chromedriver_win32 (1)\chromedriver.exe')
    selenium.get("https://astrolove.herokuapp.com/")
    selenium.set_window_size(1853, 1053)
    selenium.find_element(By.CSS_SELECTOR, ".fal").click()
    selenium.find_element(By.ID, "id_info").click()
    selenium.find_element(By.ID, "id_info").send_keys("Venus")
    selenium.find_element(By.CSS_SELECTOR, ".page-link").click()
    selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > p").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > p").text == "Nombre: venus"
    selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(4) > p").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(4) strong").text == "¿Es un planeta?:"
    selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > p").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > p").text == "Masa: 4,86747*10^24 kg"
    selenium.find_element(By.CSS_SELECTOR, "h4").click()

  def test_registroylogout(self):
    selenium = webdriver.Chrome('D:\chromedriver_win32 (1)\chromedriver.exe')
    selenium.get("https://astrolove.herokuapp.com/")
    selenium.set_window_size(1552, 840)
    selenium.find_element(By.LINK_TEXT, "Registro").click()
    selenium.find_element(By.ID, "id_username").send_keys("Prueba3")
    selenium.find_element(By.ID, "id_first_name").send_keys("Luis")
    selenium.find_element(By.ID, "id_last_name").send_keys("Prueba")
    selenium.find_element(By.ID, "id_email").send_keys("test@exame")
    selenium.find_element(By.ID, "id_email").send_keys("test@example.com")
    selenium.find_element(By.ID, "id_password").send_keys("Jupiter96!")
    selenium.find_element(By.ID, "id_address").send_keys("Prueba")
    selenium.find_element(By.ID, "id_city").send_keys("Prueba")
    selenium.find_element(By.CSS_SELECTOR, ".btn").click()
    selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(7) > .nav-link").click()

  def test_testbuscarinfologeado(self):
    selenium = webdriver.Chrome('D:\chromedriver_win32 (1)\chromedriver.exe')
    selenium.get("https://astrolove.herokuapp.com/")
    selenium.set_window_size(1552, 840)
    selenium.find_element(By.LINK_TEXT, "Iniciar Sesión").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn").click()
    selenium.find_element(By.CSS_SELECTOR, ".fa-info-circle").click()
    selenium.find_element(By.ID, "id_info").click()
    selenium.find_element(By.ID, "id_info").send_keys("venus")
    selenium.find_element(By.CSS_SELECTOR, ".page-link").click()
    selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > p").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(3) strong").text == "Nombre:"
    selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(6) > p").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(6) strong").text == "Volumen:"
    selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(8) > p").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".row:nth-child(8) strong").text == "Densidad:"
    selenium.find_element(By.CSS_SELECTOR, ".fa-power-off").click()


  def test_funcionalidadPost(self):
    selenium = webdriver.Chrome('D:\chromedriver_win32 (1)\chromedriver.exe')
    selenium.get("https://astrolove.herokuapp.com/")
    selenium.set_window_size(1552, 840)
    selenium.find_element(By.LINK_TEXT, "Iniciar Sesión").click()
    selenium.find_element(By.ID, "id_username").send_keys("Termiluis3")
    selenium.find_element(By.XPATH, "//div[3]/input").click()
    selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    selenium.find_element(By.LINK_TEXT, "Nuevo post").click()
    selenium.find_element(By.CSS_SELECTOR, ".w-50:nth-child(2)").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".w-50:nth-child(2)").text == "Título"
    selenium.find_element(By.ID, "id_title").send_keys("Prueba")
    selenium.find_element(By.ID, "id_photo").send_keys(Keys.ENTER)
    selenium.find_element(By.ID, "id_title").send_keys("Prueba")
    selenium.find_element(By.XPATH, "//div[3]/input").click()
    selenium.find_element(By.LINK_TEXT, "0").click()
    selenium.find_element(By.ID, "id_content").send_keys("Test")
    selenium.find_element(By.CSS_SELECTOR, ".card-subtitle").click()
    assert selenium.find_element(By.CSS_SELECTOR, ".card-subtitle").text == "Luis Campos Iglesia / 31-08-2021 19:30"
    selenium.find_element(By.XPATH, "//div[2]/input").click()
    selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(7) > .nav-link").click()
  

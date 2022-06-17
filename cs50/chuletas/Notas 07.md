Instruccion en desuso para el chromedriver (v102)

increase = driver.find_element_by_id("increase")

Nueva instruccion

from selenium.webdriver.common.by import By
increase = driver.find_element(By.ID, "increase")
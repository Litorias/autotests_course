from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Найти кнопку Контакты и перейти в раздел')
    cont_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    assert cont_btn.is_displayed(), 'Элемент не отображается'
    cont_btn.click()
    sleep(4)

    print('Найти баннер "Тензор" и перейти по нему')
    logo = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    logo.click()

    print('Перейти в новое окно')
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)

    print('Найти раздел "Сила в людях" и перейти в него')
    power_block = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    assert power_block.is_displayed(), 'Элемент не отображается'

    print('Найти "Подробнее" и перейти в него')
    more_link = driver.find_element(By.CSS_SELECTOR, 'p [href="/about"]')
    driver.execute_script('return arguments[0].scrollIntoView(true);', more_link)
    more_link.click()
    sleep(7)

    assert driver.current_url == "https://tensor.ru/about"

finally:
    driver.quit()
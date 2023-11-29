from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
fix_site = 'https://fix-sso.sbis.ru/auth-online/?ret=/'

try:
    driver.get(fix_site)
    sleep(2)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == fix_site, 'Неверный адрес сайта'
    assert driver.title == 'Вход в личный кабинет'

    print('Авторизоваться')
    sleep(1)
    user_login, user_password = 'Баюн', 'Баюн1!'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(4)

    print('Навести курсор на раздел "Контакты" и сделать клик')
    contact_1 = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"]')
    contact_1.click()
    sleep(1)
    print('Навести курсор в всплывающем меню на "Контакты" и сделать клик')
    contact_2 = driver.find_element(By.CSS_SELECTOR, '[class="NavigationPanels-SubMenu__headTitle   NavigationPanels-SubMenu__title-with-separator NavigationPanels-Accordion__prevent-default"]')
    contact_2.click()
    sleep(4)

    print('Навести курсор на "+"')
    button = driver.find_element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]')
    button.click()
    sleep(5)

    print('Вводим ФИ для поиска')
    user = 'Баюн Литориас'
    find = driver.find_element(By.CSS_SELECTOR, '.controls-Render__field .controls-Field')
    find.send_keys(user, Keys.ENTER)
    sleep(1)

    print('Выбираем пользователя')
    user_tile = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    user_tile.click()
    sleep(2)

    print('Набираем сообщения')
    text_to_send = 'ДЗ Ануфриев'
    text_editor = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field')
    text_editor.send_keys(text_to_send)
    sleep(1)

    print('Отправляем сообщение')
    send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_btn.click()
    sleep(5)

    print('Проверяем: сообщение появилось в списке')
    find_msg = driver.find_element(By.CSS_SELECTOR, '.controls-Render__field .controls-Field')
    find_msg.send_keys(text_to_send, Keys.ENTER)
    sleep(3)
    eye = driver.find_element(By.CSS_SELECTOR, '[class="msg-entity-info__unread-icon icon-16 ws-flex-shrink-0 ws-flex-grow-0 ws-align-self-center icon-Show icon-hover"]')
    assert eye.is_displayed(), 'Сообщение не найдено'

    print('Удаляем сообщение')
    action_chains = ActionChains(driver)
    action_chains.context_click(eye)
    action_chains.perform()
    sleep(3)

    del_btn = driver.find_element(By.XPATH, '//*[@id="popup"]/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[6]')
    del_btn.click()
    sleep(3)

    print('Проверяем, что сообщение удалено')
    boy = driver.find_element(By.CSS_SELECTOR, '[data-qa="hint-Template__imageWrapper"]')
    assert boy.is_displayed(), 'Сообщение не было удалено'

    sleep(7)

finally:
    driver.quit()

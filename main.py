import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://fleet.yandex.ru'
driver = webdriver.Safari()
driver.get(url)
time.sleep(3)

elem = driver.find_element(By.CLASS_NAME, 'cQimAh')
elem.click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, 'Textinput-Box').send_keys("testovyi_akkaunt@yandextaxi.kz")
driver.find_element(By.ID, 'passp:sign-in').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').send_keys("zdW-45y-kkE-KnX")
driver.find_element(By.ID, 'passp:sign-in').click()

time.sleep(10)
driver.find_element(By.ID, 'react-select-7-input').click()
driver.find_element(By.XPATH, '//*[@id="react-select-7-option-3"]').click()

time.sleep(2)
pages = driver.find_elements(By.CLASS_NAME, 'rc-pagination-item')
for page in pages:
    page.click()
    time.sleep(5)
    table_body = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div[2]/main/div/table/tbody')
    table_rows = table_body.find_elements(By.TAG_NAME, 'tr')
    for row in table_rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        col_limit = columns[7].text
        col_driver = columns[3]
        if col_limit != '500 000,00' and col_limit != '-50,00':
            driver_url = col_driver.find_element(By.TAG_NAME, 'a').get_attribute('href')

            driver.execute_script("window.open('');")
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            driver.get(driver_url)
            time.sleep(12)

            (driver.find_element(By.NAME, 'accounts.balance_limit')
             .send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE,
                        Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, -50))
            driver.find_element(By.XPATH,
                                '//*[@id="root"]/div/div[1]/div/div[1]/div[2]/main/div/form/div[2]/button/span').click()

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

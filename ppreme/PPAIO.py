import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import keys
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
driver.get(keys['product_url'])
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
print("ℙℙ𝔸𝕀𝕆")
print("added to cart")
time.sleep(.2)
driver.find_element_by_partial_link_text('checkout now').click()
time.sleep(.1)
driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys['card_number'])
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
driver.find_element_by_xpath('//*[@id="pay"]/input').click()
time.sleep(999999)
print("SOLVE recaptcha")

print('when done just close the tab ;)')
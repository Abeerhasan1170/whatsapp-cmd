import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from qrcode import Qrcode
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
print("Started process")
print("Loading Chrome")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=~/.config/google-chrome/Default")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.get("https://web.whatsapp.com/")
#Qrcode(driver)

running = True
recipient = "###"
elem = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"' + recipient + '")]'))
)
elem.click()
js = "var scrollElem = document.querySelector('div._33LGR');scrollElem.onscroll = function(e){var msg = document.getElementsByClassName('_22AX6');console.log(msg[msg.length - 1].innerText)}"
while running:
	driver.execute_script(js)
	for i in driver.get_log('browser'):
		try:
			msg = i['message'].split("\"")[1].replace("\\n","\t")
			print(msg)
		except:
			continue

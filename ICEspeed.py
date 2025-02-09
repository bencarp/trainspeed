from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep
import re

service = Service(executable_path='./Downloads/geckodriver')
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(service=service, options=options)

try:
	while (True):
		driver.get('https://iceportal.de')

		sleep(5) # Typically long enough for javascript to run, yet not so long as to defeat the purpose

		for line in driver.page_source.split('\n'):
			if 'traininfoIntro-speedIndicatorText">' in line:
				speed = re.search(r'speedIndicatorText">([0-9]+)\skm/h</span>', line).group(1)
				print(speed + " km/h")

except KeyboardInterrupt:
	driver.quit()

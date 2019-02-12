from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import urllib
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com")
print("waiting for you to scan qr...")
time.sleep(10)
ahmed = driver.find_element_by_xpath("//*[contains(text(),'Ahmed El Namory Aast')]")
ahmed.click()
print("waiting for you to scroll to top...")
time.sleep(10)
images  = driver.find_elements_by_tag_name("img")
counter = 0
for image in images:

	if "blob:https://" in image.get_attribute('src')	:
		try:
				time.sleep(1)
				print("trying to download %d" %counter	)
				src = image.get_attribute('src')
				#urllib.urlretrieve(src, str(counter) +".jpeg")
				driver.get(src)
				driver.save_screenshot(counter + ".jpg")
				print("downloaded image %d" %counter)
				counter +=1
		except:
			print("error downloading image %d" %counter)
			counter += 1
			continue
	else:
		print("couldn't find blob :( ")
		counter +=1 
		continue

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from PIL import Image

def click_element(element):
	#WebDriverWait(driver, 100).until(
	#    lambda driver: driver.
	#)
	element.click()
	time.sleep(5)

if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("http://weather.naver.com")

	map_element = driver.find_element_by_xpath("//div[@class='main_map']")
	map_location = map_element.location
	map_size = map_element.size
	
	times = driver.find_element_by_xpath("//ul[@class='tab']")

	for i in range(2, 6):
		time_element = times.find_element_by_xpath("li[{0}]/a".format(i))
		click_element(time_element)
		driver.save_screenshot('{0}.png'.format(i))

		im = Image.open('{0}.png'.format(i))

		left = map_location['x']
		top = map_location['y']
		right = map_location['x'] + map_size['width']
		bottom = map_location['y'] + map_size['height']
		im = im.crop((left, top, right, bottom))
		im.save('{0}.png'.format(i))

	driver.close()
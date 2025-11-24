from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

chrome_option= webdriver.ChromeOptions()
driver= webdriver.Chrome(chrome_option)

driver.get ("https://moveek.com/")
driver.set_window_size(1024, 800)
sleep(3)

dropdown_Movie= driver.find_element (By.XPATH,'//*[@id="topNavMovies"]')
dropdown_Movie.click()
sleep(5)


List_movie= driver.find_element (By.XPATH,'//li[3]/ul')
movie_items= List_movie.find_elements (By.XPATH,'./li')

print("=== Danh sách Option ===")
for option in movie_items:
    print("-", option.text.strip())
for option in movie_items:
    if option.text.strip() == "Đang chiếu":
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()
        sleep (5)
        print (f"title:{driver.title}")
        break


Latest = driver.find_element (By.XPATH,'(//div[@class="row"]//a)[1]')
Latest.click()
sleep (2)
Latest_options= Latest.find_elements (By.XPATH, '(//div[@class="row"]//a)[1]/following-sibling::ul//a')
Latest_options[0].click()
sleep (2)

Act = driver.find_element (By.XPATH,'//div[@class="row"]/div[2]//a')
Act.click()
sleep (2)
Act_options= Act.find_elements (By.XPATH, '//div[@class="row"]/div[2]//a/following-sibling::ul//a')
Act_options[3].click()
sleep (2)

# Language= driver.find_element (By.XPATH,'//div[@class="row"]/div[3]//a')
# Language_options= Language.find_elements (By.XPATH, '//div[@class="row"]/div[3]//a/following-sibling::ul//a')
# Language_options[1].click()
# sleep (2)

# list of upcoming movies
List_name= driver.find_elements (By.XPATH,'//div[2][contains(@class,"md-10")]')
print("=== list of upcoming movies ===")
for movie_name in List_name:
    print("-", movie_name.text.strip())
sleep (3)

# Click the second movie
if len(List_name) >= 2:
    List_name[1].click()
    print("Click the second movie")
else:
    print("There is no second movie to click")
    sleep(3)

# select CGV
CGV_button= driver.find_element (By.XPATH,'//*[@id="showtimes"]//div/a[2]')
CGV_button.click()
sleep (3)

theater_list= driver.find_elements (By.XPATH,'//*[@id="showtime-cineplex-18784"]')
print("===CGV list===")
for theater in theater_list:
    print ("-",theater.text.strip())
    
for theater in theater_list:
    if theater.text.strip() == "CGV Vincom Đà Nẵng":
        actions = ActionChains(driver)
        actions.move_to_element(theater).click().perform()
        sleep (3)
theater_info= driver.find_element (By.XPATH,'//*[@id="showtimes"]//a[contains(@href, "cgv-vincom-da-nang")]')
theater_info.click()
sleep (5)

driver.quit()

# //div[contains(@class,"row")]//div[2][contains(@class,"md-10")]
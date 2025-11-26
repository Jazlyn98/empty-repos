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

Language= driver.find_element (By.XPATH,'//div[@class="row"]/div[3]//a[contains(text(), "Ngôn ngữ")]')
Language.click()
sleep (2)
# //*[@id="app"]/div[1]/div[2]/div/div[1]/div/div[3]/div/ul/li[2]/a
# //*[@id="app"]/div[1]/div[2]/div/div[1]/div/div[3]
Language_options= Language.find_elements (By.XPATH, './following-sibling::ul//a')
Language_options[1].click()
sleep (2)

# list of upcoming movies
list_movies= driver.find_elements(By.XPATH,'//*[@id="app"]//div[@class="row grid"]//div[contains(@class,"item")]')
# because this list is full list of movies, we need the below function to get the "visible" movies list
list_visible_movies = []
for movie in list_movies:
    style_attribute = movie.get_attribute('style')
    if style_attribute is None or 'display: none' not in style_attribute.lower():
        list_visible_movies.append(movie)

print("=== list of upcoming movies ===")
for movie_name in list_visible_movies:
    print("-", movie_name.text)
sleep (3)

# Click the second movie
if len(list_visible_movies) >= 2:
    second_movie_link = list_visible_movies[1].find_element(By.XPATH, './/img/..') # get <img> because only the <a> tag we want to click have it,
    # so we get the img then get the parent - it means the a tag we want to click on.
    # to get parent, we can use the './/img/parent::a' or './/img/..' <-- the ".." means parent.
    second_movie_link.click()
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
        # this click must follow the "if" to make sure we have CGV Vincom Đà Nẵng in list
        vincom_dn_theater_info= driver.find_element (By.XPATH,'//*[@id="showtimes"]//a[contains(@href, "cgv-vincom-da-nang")]')
        vincom_dn_theater_info.click()
    else:
        # if don't have CGV vincom DN, choose the first theatre - btw, should use "cinema" instead of "theater"
        theater_list[1].click() # practice: make this click works.
        first_theater_info= theater_list[1].find_element (By.XPATH,'//*[@id="showtimes"]//a')
        first_theater_info.click()
        sleep (5)

driver.quit()

# //div[contains(@class,"row")]//div[2][contains(@class,"md-10")]
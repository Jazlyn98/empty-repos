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
driver.set_window_size(1200, 1000)
sleep(3)

dropdown_Movie= driver.find_element (By.XPATH,'//*[@id="topNavMovies"]')
dropdown_Movie.click()
sleep(5)


List_movie= driver.find_element (By.XPATH,'//li[3]/ul')
movie_items= List_movie.find_elements (By.XPATH,'./li')

print("=== List Option ===")
for option in movie_items:
    print("-", option.text.strip())
for option in movie_items:
    if option.text.strip() == "Đang chiếu":
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()
        sleep (5)
        print (f"title:{driver.title}")
        break


latest = driver.find_element (By.XPATH,'(//div[@class="row"]//a)[1]')
latest.click()
sleep (2)
latest_options= latest.find_elements (By.XPATH, '(//div[@class="row"]//a)[1]/following-sibling::ul//a')
latest_options[0].click()
sleep (2)

act = driver.find_element (By.XPATH,'//div[@class="row"]/div[2]//a')
act.click()
sleep (2)
act_options= act.find_elements (By.XPATH, '//div[@class="row"]/div[2]//a/following-sibling::ul//a')
act_options[1].click()
sleep (2)

language= driver.find_element (By.XPATH,'//div[@class="row"]/div[3]//a[contains(text(), "Ngôn ngữ")]')
language.click()
sleep (2)
language_options= language.find_elements (By.XPATH, './following-sibling::ul//a')
language_options[0].click()
sleep (2)

# list of upcoming movies
list_movies= driver.find_elements(By.XPATH,'//*[@id="app"]//div[@class="row grid"]//div[contains(@class,"item")]')
# because this list is full list of movies, we need the below function to get the "visible" movies list
list_visible_movies = []
for movie in list_movies:
    style_attribute = movie.get_attribute('style')
    if style_attribute is None or 'display: none' not in style_attribute.lower():  #Convert all text in style to lowercase to avoid errors when the page is written in a different style
        list_visible_movies.append(movie)

print("=== list of upcoming movies ===")
for index, movie_name in enumerate(list_visible_movies):
    name = movie_name.text.strip()
    print(f'movie index: {index} , movie name: {name}')
sleep (3)

# Click the second movie
if len(list_visible_movies) >= 2:
    second_movie_link = list_visible_movies[0].find_element(By.XPATH, './/img/..') # get <img> because only the <a> tag we want to click have it,
    # so we get the img then get the parent - it means the a tag we want to click on.
    # to get parent, we can use the './/img/parent::a' or './/img/..' <-- the ".." means parent.
    print(f"type of the second movie element: {type(second_movie_link)}")
    print(f"Click the second movie: {second_movie_link.text}")
    second_movie_link.click()
else:
    print("There is no second movie to click")
    sleep(5)

location_dropdown= driver.find_element (By.XPATH,'//div[@class="row"]/div[@class="col"]')
location_dropdown.click()
sleep(3)
dn_option = driver.find_element(By.XPATH, "//select[contains(@class,'btn-select-region')]")
Select(dn_option).select_by_visible_text("Đà Nẵng")
print ("Select sucessful city:DN")
sleep(3)


# select CGV
cimemar_list= driver.find_element (By.XPATH,'//*[@id="showtimes"]')
if not cimemar_list:
    print("No cinemar are found")
sleep(3)

CGV_button= driver.find_element(By.XPATH,'//a[contains(@data-cineplex, "cgv-cineplex")]')
print(f"CGV button text: {CGV_button.text}")
CGV_button.click()
is_open = CGV_button.get_attribute("aria-expanded") == "true"
if not is_open:
    CGV_button.click()
    print("CLICK TO OPEN ")
else:
    print("ALREADY OPEN")
sleep (3)

CGV_cinema_list= driver.find_elements(By.XPATH,'//*[@id="showtime-cineplex-18784"]/div')
for index,cgv_cinema_name in enumerate(CGV_cinema_list):
    name = cgv_cinema_name.text
    print(f'CGV_cinema_list len: {len(CGV_cinema_list)}')
    print(f'cinema index: {index} , cinema name: {name}')
sleep (3)

print("===CGV list===")
found_vt = False     #flag to check (not found assign false)
for cinema in CGV_cinema_list:
    print ("-",cinema.text.strip())
    if cinema.text.strip() == "CGV Vĩnh Trung Plaza":
        actions = ActionChains(driver)
        actions.move_to_element(cinema).click().perform()
        print ("Click CGV Vĩnh Trung Plaza")
        sleep (3)
        vt_cinema_info= driver.find_element (By.XPATH,'//*[@id="showtimes"]//a[contains(@href, "cgv-vinh-trung-plaza")]')
        vt_cinema_info.click()
        sleep (5)
        found_vt = True   #set flag to true if found
        print("Found found_vt")
        break

# if don't have CGV Vĩnh Trung Plaza, choose the first "cinema"
if not found_vt:
    first_cinema= CGV_cinema_list[0]
    ActionChains(driver).move_to_element(first_cinema).click().perform()
    first_cinema_info= CGV_cinema_list[0].find_element (By.XPATH,'//*[@id="showtimes"]//a')
    first_cinema_info.click()
    print("NOT found found_vt")
    print(f"The real cinema which has been clicked: {first_cinema_info.text}")
    sleep (5)

print("Finish. Quit")
driver.quit()

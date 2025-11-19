from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

chrome_option= webdriver.ChromeOptions()
driver= webdriver.Chrome(chrome_option)

driver.get ("https://moveek.com/")
driver.set_window_size(1024, 800)
sleep(3)
print (f"main_title:{driver.title}")
sleep(10)

#Click on the “Rạp” dropdown arrow
dropdown_cinemas= driver.find_element(By.XPATH,'//*[@id="navbar"]//a[@href="/rap/"]')
dropdown_cinemas.click()
sleep(5)
modal = driver.find_element(By.XPATH, '//div[@id="cinemaModal"]//div[@class="modal-content"]')
if modal.is_displayed():
    print("Modal is displayed")
else:
    raise Exception("Modal not visible")

actions = ActionChains(driver) #use ActionChains to open Select box/Combobox to select item

select_box = modal.find_element(By.XPATH,'//select')
actions.click(select_box).perform()

child_elements = select_box.find_elements(By.XPATH, ".//*") 

# You can iterate through the child_elements list
for child in child_elements:
    if child.text == "Đà Nẵng":
        print(f" city: {child.text}")
        child.click()
sleep(3)

#All cinemas in Đà Nẵng are displayed
cinema_list = driver.find_elements(By.CSS_SELECTOR, "[data-name]")
cinema_names = []  # create an empty list to store theater names
for c in cinema_list:
    name = c.get_attribute("data-name") # get the name attribute
    if name:
        cinema_names.append(name)   # add name to the list
print("theater names")
for name in cinema_names:
    print("-", name)

#Select “Metiz Cinema” from the list
metiz_cinema= driver.find_element(By.XPATH,"//h4/a[contains(text(), 'Metiz Cinema')]")
metiz_cinema.click()
sleep(5)

# the parent element of date and list of movies
showtimes_element = driver.find_element(By.XPATH,'//*[@id="showtimes"]/div')

#Print the selected date
selected_date=showtimes_element.find_element(By.XPATH,'.//div[@id="dates"]/a[contains(@class, "active")]') #the selected date will have class "active"
date_str= selected_date.get_attribute("data-date")
weekday= selected_date.find_element(By.XPATH,".//span").text.strip()
print(f"selected date: {date_str},{weekday}")
sleep(2)

#Get the name of the first movie in the list
first_movie_today= showtimes_element.find_element(By.XPATH,'./div[3]') # ignore div[1] - the "dates" and the div[2] - "sponsor movie"
print (f"11111 first_movie_today:{first_movie_today.text}")
sleep(2)

#Select the earliest available time
time_list_today = first_movie_today.find_elements(By.XPATH, './/a[contains(@class, "showtime")]') # locate the showtimes of first movie
earliest_time_today = time_list_today[0] # get the first time in list
print(f"Earliest showtime today: {earliest_time_today.text.strip()}")
try:
    earliest_time_today.click()
    print("Clicked the earliest showtime today.")
except Exception:
    print("Earliest showtime today has passed — cannot click")
    print("try tomorrow")
    
#get the earliest time of the next day (tomorrow)
tomorrow = showtimes_element.find_element(By.XPATH,'.//div[@id="dates"]/a[2]') # a[1] is the first date in list, a[2] is tomorrow
tomorrow.click()
sleep(3)
    
#Get back the showtime list after moving to tomorrow
showtimes_element = driver.find_element(By.XPATH,'//*[@id="showtimes"]/div')
first_movie_tomorrow= showtimes_element.find_element(By.XPATH,'.//div[3]')
sleep(2)

# get first movie again, because element change and tomorrow movies list may change
time_list_tomorrow = first_movie_tomorrow.find_elements(By.XPATH, './/a[contains(@class, "showtime")]') # locate the first showtime of first movie
earliest_time_tomorrow = time_list_tomorrow[0]
print(f"Earliest showtime tomorrow: {earliest_time_tomorrow.text.strip()}")
try:
    earliest_time_tomorrow.click()
    print("Clicked the earliest showtime tomorrow.")
except Exception:
    print("Error — cannot click")
sleep(3)

driver.quit() # always have this to quit the test correctly

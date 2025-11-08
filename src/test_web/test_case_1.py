from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

chrome_option= webdriver.ChromeOptions()
driver= webdriver.Chrome(chrome_option)

driver.get ("https://moveek.com/")
sleep(3)
print (f"main_title:{driver.title}")
sleep(3)

#Click on the “Rạp” dropdown arrow
dropdown_cinames= driver.find_element(By.XPATH,"//a[@href='/rap/']")
dropdown_cinames.click()
sleep(5)
modal = driver.find_element(By.XPATH, "//div[@id='cinemaModal']//div[@class='modal-content']")
if modal.is_displayed():
    print("Modal is displayed")
else:
    raise Exception("Modal not visible")

#In the search box, type “Đà Nẵng”

combobox= driver.find_element (By.XPATH,"//span[@role='combobox']")
combobox.click()
sleep(2)
Search_box= driver.find_element (By.XPATH,"//span[1]/input[@type='search']")
Search_box.send_keys("Đà Nẵng",Keys.ENTER)
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
metiz_cinema= driver.find_elements(By.XPATH,"//h4/a[contains(text(), 'Metiz Cinema')]")
for cinema in metiz_cinema:
    cinema.click()
    break
sleep(5)

#Print the selected date
selected_date=driver.find_elements(By.XPATH,"//*[@id='dates']/a[1]")
for date in selected_date:
    date_str= date.get_attribute("data-date")
    weekday= date.find_element(By.XPATH,"//*[@id='dates']/a[1]/span").text.strip()
    print(f"selected date: {date_str},{weekday}")
    break
sleep(2)

#Get the name of the first movie in the list
first_movie= driver.find_elements(By.XPATH,"//div[2]/div/div/div[2]/h4[@class='card-title mb-1 name']/a") #ko bk rút gọn hơn
for movie in first_movie:
    movie_name= movie.text
    print (f"first movie name:{movie_name}")
    break
sleep(2)

#Select the earliest available time
# locate the firsr movie
time_container = movie.find_element(By.XPATH, "//*[@id='showtimes']/div/div[2]/div/div/div[2]/div/div") #ko bk rút gọn dong nay
# Get all time
time_slots = time_container.find_elements(By.XPATH, ".//span[contains(@class,'time')]")

if time_slots:
    earliest_time = time_slots[0].text.strip()  # get the text of the first time
    print(f"Earliest showtime: {earliest_time}")  
    time_slots[0].click()  
sleep(3)
  

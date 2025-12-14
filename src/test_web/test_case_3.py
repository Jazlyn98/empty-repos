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

book_movie_tickets = driver.find_element(By.XPATH,'//*[@id="navbar"]//a[contains(@href,"/mua-ve/")]')
book_movie_tickets.click()
sleep(3)

list_movies = driver.find_elements(By.XPATH,'//div[contains(@class,"slick-active")]') #Should be find_elements
# without "s" it will return only the first movie in list and the code below cannot run.

movies_names = []  
for c in list_movies:
    name = c.get_attribute("id") # If we want to get "name", we cannot get "id" --> it will print out the list of movie's ids. Fix it.
    if name:
        movies_names.append(name) 
print("movies names")
for name in movies_names:
    print("-", name)

first_movie = driver.find_element(By.XPATH,'//*[@id="slick-slide00"]')
first_movie.click()
sleep(3)

evaluate_tab= driver.find_element (By.XPATH,'//*[@id="app"]//li[3]')
evaluate_tab.click()
print (f"main_title:{driver.title}")
sleep(3)

percent_el= driver.find_element(By.XPATH,'//span[contains(@class,"rating-percentage")]')
print(f"percent_el: {percent_el.text}%")
sleep(2)

review_list = driver.find_element (By.XPATH,'//*[@id="app"]//div[contains(@class,"card-infinite")]')
reviews= review_list.find_elements (By.XPATH,'.//div[contains(@class,"article")]')
if len(reviews): # if there is review in the review list, print the first one. 
    # Practice: check if there is >2 reviews, print the first and second reviews.
    print(f'The first review: {reviews[0].text}')

evaluate_button= driver.find_element (By.XPATH,'//a[contains(@title,"Write a review")]') #if we want to write review, maybe we need to login first, but you've not yet logged in. Fix it.
# you create a free account to do the login here
# or remove the write review part and replace by other actions
evaluate_button.click()
sleep(2)

evaluate_modal = driver.find_element(By.XPATH, '//div[@id="ratingModal"]//div[@class="modal-content"]')
if evaluate_modal.is_displayed():
    print("Modal is displayed")
else:
    raise Exception("Modal not visible")

rating_star= evaluate_modal.find_elements (By.XPATH,'//*[@id="movie_rating_form"]/div[1]/div)')
if len(rating_star)>=10:
    rating_star[8].click()
    print("select rating star successfull")
    sleep(2)

review_box = evaluate_modal.find_element (By.XPATH,'//*[@id="movie_rating_message"]')
post_button= evaluate_modal.find_element (By.XPATH,'//*[@id="movie_rating_save"]')

review_box.clear()
review_box.send_keys("Good") # < 10 chars
post_button.click()
sleep(3)

error_el = driver.find_element(By.XPATH, '//*[contains(text(),"error.rating_form_limit_characters")]')
assert error_el.is_displayed(), "Error should appear but NOT displayed!"
print(f"Error shows: {error_el.text}")


review_box.clear()
review_box.send_keys("Great movie, very enjnoynable")
post_button.click()

driver.quit()
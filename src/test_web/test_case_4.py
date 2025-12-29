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

news_dropdown = driver.find_element (By.XPATH,'//*[@id="topNavNews"]')
news_dropdown.click()
sleep(3)
list_news = driver.find_element (By.XPATH,'//li[5]/ul')
news_items= list_news.find_elements(By.TAG_NAME, "li")
print ("=== List News option===")
for option in news_items:
    print("-", option.text.strip())
for option in news_items:
    if option.text.strip() == "Tv Series":
        option.click()
        sleep(3)
        print (f"title:{driver.title}")
        break

list_movies = driver.find_elements(By.XPATH,"//div[contains(@class,'glide__slide')]//a[@title]")
movie_names = []
for movie in list_movies:
    name = movie.get_attribute("title")
    if name:
        movie_names.append(name)
print("Movie names:")
for name in movie_names:
    print("-", name)
sleep (3)

# ASSERT film number
try:
    assert len(movie_names) <= 8, f"Expected max 8 movies, but got {len(movie_names)}"
    print("PASS: Max 8 movies displayed")
except AssertionError as e:
    print("FAIL:", e)
sleep (3)

first_movie = driver.find_element (By.XPATH,'//*[@id="app"]//div[1]/div/h3')
first_movie.click()
print (f"title:{driver.title}")
sleep(3)

related_articles = driver.find_element (By.XPATH,'//div[contains(@class,"card-article")]/div[2]')
names_articles = related_articles.find_elements (By.XPATH,'.//div[2]//h4')

print ("Related articles:")
for article in names_articles:
    print ("-",article.text.strip())

# Click the second article
if len(names_articles) >= 2:
    second_article = names_articles[1]
    second_article.click()
    print(f"Clicked article: {second_article.text.strip()}") # cannot see the new page, It just prints title
    sleep(5)
else:
    print("There is no second article to click")

driver.quit()


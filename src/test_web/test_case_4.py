from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_option= webdriver.ChromeOptions()
driver= webdriver.Chrome(chrome_option)
wait = WebDriverWait(driver, 10)

driver.get ("https://moveek.com/")
driver.maximize_window()
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
        wait.until(EC.element_to_be_clickable(option)).click()
        print (f"title:{driver.title}")
        break

list_movies = driver.find_elements(By.XPATH,"//div[contains(@class,'glide__slide')]//a[@title]")
movie_names = []   #create an empty list
for movie in list_movies:   #loop through each movie element
    name = movie.get_attribute("title")  
    if name:
        movie_names.append(name)   #add the movie name to list if it exists
print("Movie names:")
for name in movie_names:
    print("-", name)
sleep (3)

# ASSERT film number
try:   
    assert len(movie_names) >=2, f"Expected at least 2 movies, but got {len(movie_names)}"
    print("PASS: At least 2 movies displayed")
except AssertionError as e:    
    print("FAIL:", e)

movies = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'glide__slide')]//a[@title]")))
first_movie = movies[0]
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", first_movie)
driver.execute_script("arguments[0].click();", first_movie)
print(f"title: {driver.title}")


#articles
try:
    names_articles = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"card-article")]//h4')))
except TimeoutException:
    print("STOP TEST: No articles displayed on the page")
    raise SystemExit

print("Related articles:")
for article in names_articles:
    print("-", article.text.strip())


# Click the second article
if len(names_articles) >= 2:
    second_article = names_articles[1]
    article_title = second_article.text.strip()
    wait.until(EC.element_to_be_clickable(second_article))
    second_article.click()
    print(f"Clicked article: {article_title}")
else:
    print("There is no second article to click")

driver.quit()


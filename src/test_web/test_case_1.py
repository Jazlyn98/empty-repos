from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

chrome_option= webdriver.ChromeOptions()
driver= webdriver.Chrome(chrome_option)
sleep(1)
driver.get ("https://www.staging.littlelives.com/signin")
sleep(3)
print (f"main_title:{driver.title}")
sleep(3)

#kiem tra nut sign in disable
signin_button= driver.find_element (By.ID,"btn-submit-sign-in")
is_disabled = not signin_button.is_enabled() 
if is_disabled:
    print("Nút 'Login' bị vô hiệu hóa khi không nhập email và password.")
else:
    print("Nút 'Login' không bị vô hiệu hóa khi không nhập email và password.")
sleep(3)

email= driver.find_element (By.XPATH,"/html/body/div[1]/div/div/main/div/div/div/div/div/form/div[1]/div/input")
email.send_keys ("sunny.trainc_w81017_admin@mailinator.com")
sleep(3)
password= driver.find_element (By.XPATH,"/html/body/div[1]/div/div/main/div/div/div/div/div/form/div[2]/div/input")
password.send_keys ("Traninc@456")
sleep(3)
#kiem tra nut sign in enable
is_enabled = signin_button.is_enabled()
if is_enabled:
    print("Nút 'Login' đã được kích hoạt khi nhập email và password.")
else:
    print("Nút 'Login' chưa được kích hoạt dù đã nhập email và password.")
sleep(5)
# verify login success
signin_button.click ()
sleep(5)
expected_title ="Dashboard"
assert expected_title in driver.title, "Đăng nhập thất bại, tiêu đề không khớp"
print ("SUCCESS")
ori_windown= driver.current_window_handle
assert len (driver.window_handles) ==1, print (f"assert isWindowsNumberPassed FAILED")
print ("PASSED")
import pytest
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = r"https://jw.ahu.edu.cn"

student_id = "E22814520"                # input your student.id 
password = "12345678"                   # input your student.password
select_class_name = "ZX36268"           # input the class id you select
target_class_id = "202520262-ZX36268.001" # input the course's class_id
target_teacher = "王逍"                  # input the course's teacher
start_time = "2026-03-09 16:58:00"      # input the time when the course start to select

# base message
print("select class:", select_class_name)
print("target class id:", target_class_id)
print("target teacher:", target_teacher)


@pytest.fixture
def driver():
    # Setup 
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    
    driver.assert_result = "" 
    
    yield driver 
    
    # Teardown
    if driver.assert_result == "选课成功":
        sleep(3)
    else:
        sleep(10)
    driver.quit()

def test_grapclick(driver):
    #login
    driver.find_element(By.CSS_SELECTOR, "#terminals > div:nth-child(1) > label > input[type=radio]").click()
    driver.find_element(By.CSS_SELECTOR, "body > div > section > div.sw-login-wrapper > div > div > ul > li:nth-child(4)").click()
    username = driver.find_element(By.CSS_SELECTOR, "body > div > section > div.sw-login-wrapper > div > div > div:nth-child(4) > form > div:nth-child(1) > div:nth-child(1) > div > div > input")
    username.send_keys(student_id)
    pw = driver.find_element(By.CSS_SELECTOR, "input[placeholder='密码']")
    pw.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "body > div > section > div.sw-login-wrapper > div > div > div:nth-child(4) > form > div:nth-child(4) > div:nth-child(2) > div > button").click()
    
    #notice clear
    try:
        classbutton = driver.find_element(By.CSS_SELECTOR, "#e-top-menu > li > a")
    except Exception:
        print("please clear the notice")
        
    ActionChains(driver).move_to_element(classbutton).perform()
    driver.find_element(By.CSS_SELECTOR, r"#drop_01\.04\.01").click()  
    driver.switch_to.frame("e-home-iframe-1")
    driver.find_element(By.XPATH, '//*[@id="course-select-app"]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/button').click()
    driver.switch_to.window(driver.window_handles[-1])
    
    #select class
    select_class = driver.find_element(By.CSS_SELECTOR, "#programs > div.programs-head > div.programs-search.search-form > div > div:nth-child(1) > div.el-input.el-input--mini.el-input--suffix > input")
    select_class.send_keys(select_class_name)
    row0 = driver.find_elements(By.CSS_SELECTOR, "tr.course-item")
    select_btn = row0[0].find_element(By.CSS_SELECTOR, "button.course-select")
    select_btn.click()
    
    #start select
    row = driver.find_element(By.CSS_SELECTOR, "#programs > div:nth-child(3) > div > div > div > section > div > div > div > div.lesson-head > form > div > div:nth-child(2) > div.el-input.el-input--mini.el-input--suffix > input")
    row.send_keys(target_class_id)
    rows = driver.find_element(By.CSS_SELECTOR,"#programs > div:nth-child(3) > div > div > div > section > div > div > div > div.lesson-head > form > div > div:nth-child(3) > div.el-input.el-input--mini.el-input--suffix > input")
    rows.send_keys(target_teacher)
    driver.find_element(By.CSS_SELECTOR,"#programs > div:nth-child(3) > div > div > div > section > div > div > div > div.lesson-head > form > div > div:nth-child(16) > button.el-button.el-button--primary.el-button--mini").click()
    startselect = driver.find_element(By.XPATH,'//*[@id="programs"]/div[3]/div/div/div/section/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr/td[1]/div/button')

    #time check
    print("\nTime before start select:", start_time)
    recent_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    while recent_time < start_time:
        sleep(1)
        recent_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(recent_time)
    startselect.click()   
             
#    #assert
    i=2
    while i:
        i-=1
        try:
            assertresult=driver.find_element(By.CSS_SELECTOR,"#programs > div:nth-child(3) > div > div > div > section > div > div > div > div:nth-child(3) > div > div.el-dialog__body > div > span").text
            assert assertresult == "选课成功"
            print("选课成功")
        except:
            print(assertresult)
            pass

          
                 
        
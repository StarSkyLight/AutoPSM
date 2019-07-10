import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# calculate numbers of score 0
def score_0(list_of_score_number):
    list_of_score_number[0] = list_of_score_number[0] + 1
    return list_of_score_number


# calculate numbers of score 1
def score_1(list_of_score_number):
    list_of_score_number[1] = list_of_score_number[1] + 1
    return list_of_score_number


# calculate numbers of score 2
def score_2(list_of_score_number):
    list_of_score_number[2] = list_of_score_number[2] + 1
    return list_of_score_number


# calculate numbers of score 3
def score_3(list_of_score_number):
    list_of_score_number[3] = list_of_score_number[3] + 1
    return list_of_score_number


# calculate numbers of score 4
def score_4(list_of_score_number):
    list_of_score_number[4] = list_of_score_number[4] + 1
    return list_of_score_number


# calculate numbers of scores
def scoring(list_of_score_number, num_score):
    scores = {
        0: score_0,
        1: score_1,
        2: score_2,
        3: score_3,
        4: score_4
    }

    method = scores.get(num_score, 0)
    if method:
        return method(list_of_score_number)


# method to test.py the password strength meter of reddit.com
def test_reddit():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')

    prefs = {"profile.managed_default_content_settings.images": 2}  # do not load images
    chrome_options.add_experimental_option("prefs", prefs)

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"  # do not wait for completion of loading the web page

    driver = webdriver.Chrome('D:\\software\\ChromeDriver\\chromedriver', options=chrome_options,
                              desired_capabilities=desired_capabilities)

    # wait = WebDriverWait(driver, 20, 0.5)

    driver.get('file:///C:/Users/ziyi/Desktop/reddit_%20the%20front%20page%20of%20the%20internet.html')

    # wait.until(EC.presence_of_element_located((By.ID, 'regPassword')))

    sleep(5)  # wait for the browser loading elements that we need

    driver.execute_script("window.stop();")  # stop loading the web page

    driver.switch_to.frame(5)  # 5 means the 6th frame

    file_score = open('C:/Users/ziyi/Desktop/score.txt', 'w', encoding='utf-8')

    file_passwd = open("C:/Users/ziyi/Desktop/test.py.txt", encoding='utf-8')
    line = file_passwd.readline()

    num_of_passwds = 0
    list_of_score_numbers = [0, 0, 0, 0, 0]  # a list of every score's number, score ranges from 0 to 4

    # if EC.presence_of_element_located((By.ID, 'regPassword')):
    passwd_input = driver.find_element_by_id("regPassword")  # find the text box to input password

    # if EC.presence_of_element_located((By.CLASS_NAME, 'PasswordMeter')):
    password_meter = driver.find_element_by_class_name('PasswordMeter')

    while line:
        password = re.findall(r'\t(.+)', line)  # choose the part after a tab in a line as the password
        file_score.write(str(password) + '\t')
        num_of_passwds = num_of_passwds + 1

        passwd_input.send_keys(password)  # input password

        # get score of the password
        score = password_meter.get_attribute('data-strength')
        file_score.write(str(score) + "\n")

        # calculate the number of this score
        list_of_score_numbers = scoring(list_of_score_numbers, int(str(score)))

        passwd_input.clear()
        line = file_passwd.readline()

    file_score.write('\n\nNumber of tasted passwords' + '\t' + str(num_of_passwds) + '\n\n')
    file_score.write('Score range\t0 to 4\n')
    file_score.write('Score' + '\t' + 'Number of passwords' + '\n')
    file_score.write('0' + '\t\t' + str(list_of_score_numbers[0]) + '\n')
    file_score.write('1' + '\t\t' + str(list_of_score_numbers[1]) + '\n')
    file_score.write('2' + '\t\t' + str(list_of_score_numbers[2]) + '\n')
    file_score.write('3' + '\t\t' + str(list_of_score_numbers[3]) + '\n')
    file_score.write('4' + '\t\t' + str(list_of_score_numbers[4]) + '\n')

    driver.close()


test_reddit()

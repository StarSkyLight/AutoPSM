import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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


# calculate numbers of scores
def scoring(list_of_score_number, num_score):
    scores = {
        '危险': score_0,
        '一般': score_1,
        '安全': score_2
    }

    method = scores.get(num_score, 0)
    if method:
        return method(list_of_score_number)


# method to test.py the password strength meter of reddit.com
def test_12306():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')

    prefs = {"profile.managed_default_content_settings.images": 2}  # do not load images
    chrome_options.add_experimental_option("prefs", prefs)

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"  # do not wait for completion of loading the web page

    upper_lavel_dir = os.path.abspath('..')

    driver = webdriver.Chrome(upper_lavel_dir + '/chromedriver', options=chrome_options,
                              desired_capabilities=desired_capabilities)

    # wait = WebDriverWait(driver, 20, 0.5)

    current_dir = os.path.abspath('.')

    driver.get('file:///' + current_dir + '/中国铁路12306.html')

    # wait.until(EC.presence_of_element_located((By.ID, 'regPassword')))

    sleep(5)  # wait for the browser loading elements that we need

    driver.execute_script("window.stop();")  # stop loading the web page

    file_score = open(current_dir + '/score.txt', 'w', encoding='utf-8')

    file_passwd = open(current_dir + "/7k7k-1.txt", encoding='utf-8')
    line = file_passwd.readline()

    for i in range(1, 61721):
        line = file_passwd.readline()

    num_of_passwds = 0
    list_of_score_numbers = [0, 0, 0]  # a list of every score's number, score ranges from 0 to 2

    # if EC.presence_of_element_located((By.ID, 'regPassword')):
    passwd_input = driver.find_element_by_id("passWord")  # find the text box to input password

    # if EC.presence_of_element_located((By.CLASS_NAME, 'PasswordMeter')):
    password_meter = driver.find_element_by_id('_div_password_rank')

    while line:
        password = re.findall(r'\t(.+)', line)  # choose the part after a tab in a line as the password
        file_score.write(str(password[0]) + '\t')
        num_of_passwds = num_of_passwds + 1

        passwd_input.send_keys(password[0])  # input password

        # get score of the password
        score = password_meter.get_attribute('title')
        file_score.write(str(score) + "\n")

        # calculate the number of this score
        list_of_score_numbers = scoring(list_of_score_numbers, str(score))

        passwd_input.clear()
        line = file_passwd.readline()

    file_score.write('\n\nNumber of tasted passwords' + '\t' + str(num_of_passwds) + '\n\n')
    file_score.write('Score range\t危险\t一般\t安全\n')
    file_score.write('Score' + '\t' + 'Number of passwords' + '\n')
    file_score.write('危险(Dangerous)' + '\t\t' + str(list_of_score_numbers[0]) + '\n')
    file_score.write('一般(Ordinary)' + '\t\t' + str(list_of_score_numbers[1]) + '\n')
    file_score.write('安全(Safe)' + '\t\t' + str(list_of_score_numbers[2]) + '\n')

    driver.close()


test_12306()

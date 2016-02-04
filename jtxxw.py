from selenium import webdriver
import time
import logging
import sys  

def login():
	time.sleep(1)
	driver.find_element_by_class_name("login_select_01").click()
	driver.find_element_by_class_name("login_select_01").click()
	driver.find_element_by_class_name("login_select_01").click()
	time.sleep(1)
	driver.find_element_by_id("320300").click()

	inputId = driver.find_element_by_name("loginId")
	inputId.send_keys("identification card number")

	inputId = driver.find_element_by_name("authCode")
	inputId.send_keys("123233")

	inputId = driver.find_element_by_name("passwd")
	inputId.send_keys("123456")

	login_button = driver.find_element_by_class_name("login_buton")
	login_button.click()

def isLoginPage():
	login_select = driver.find_element_by_class_name("login_select_01")
	if isinstance(login_select, webdriver.remote.webelement.WebElement):
		return True
	else:
		return False
		
def isNextEnable():
	nextPage = driver.find_element_by_class_name("dfss_down")
	if isinstance(nextPage, webdriver.remote.webelement.WebElement):
		return True
	else:
		return False

def get_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
    file_handler = logging.FileHandler("jtxxw.log")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    #logger.error("fuckgfw")
    #logger.removeHandler(stream_handler)
    #logger.error("fuckgov")
    return logger

if __name__ == "__main__":
        logger = get_logger()
	driver = webdriver.Ie()
	driver.get("http://www.jsjtxx.com/spage/Continuing-Education-Login.html")

	if isLoginPage:
		login()
	
	continuelearn = driver.find_element_by_class_name("btn_iskt2")
	continuelearn.click()
	
        last_time = time.time()
	last_num_tag_a = 0
	while True:
		time.sleep(2)

		
		dfss_page = driver.find_element_by_class_name("dfss_page")
		num_tag_li = len(dfss_page.find_elements_by_tag_name("li"))
		curr_num_tag_a = len(dfss_page.find_elements_by_tag_name("a"))
		if last_num_tag_a != curr_num_tag_a:
			logger.debug("num_tag_li = %d, curr_num_tag_a = %d, last_num_tag_a = %d" % (num_tag_li, curr_num_tag_a, last_num_tag_a))
		if last_num_tag_a == 0:
			last_num_tag_a = curr_num_tag_a
			logger.debug("num_tag_li = %d, curr_num_tag_a = %d, last_num_tag_a = %d" % (num_tag_li, curr_num_tag_a, last_num_tag_a))
		
		if curr_num_tag_a <= num_tag_li and last_num_tag_a < curr_num_tag_a:
			logger.info("found next enable")
			last_num_tag_a = curr_num_tag_a
			logger.debug("num_tag_li = %d, curr_num_tag_a = %d, last_num_tag_a = %d" % (num_tag_li, curr_num_tag_a, last_num_tag_a))
			
			time.sleep(10)
			if isNextEnable():
                                c_line01 = driver.find_elements_by_class_name("c_line01")
                                video_title0 = c_line01[7].find_element_by_tag_name("span").text
                                #video_title1 = c_line01[8].find_element_by_tag_name("span").text
                                video_title2 = c_line01[9].find_element_by_tag_name("span").text

				driver.find_element_by_class_name("dfss_down").click()
				logger.info("click next")
                                end_time = time.time()
                                logger.info("play " + video_title0 + ": " + video_title2 + " spend time %f" % (end_time - last_time))
                                last_time = end_time
		
		if curr_num_tag_a < last_num_tag_a:
			last_num_tag_a = curr_num_tag_a
			logger.debug("num_tag_li = %d, curr_num_tag_a = %d, last_num_tag_a = %d" % (num_tag_li, curr_num_tag_a, last_num_tag_a))
		

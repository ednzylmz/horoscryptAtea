from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

site_url = 'https://tartuulikool-my.sharepoint.com/:v:/g/personal/karlmv_ut_ee/Eb_w5Gj4N0lIv3sIgmalcjQBWjktodUT3JRiO3GWkRAqCw?e=YfASkt'

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')
print ("Headless Chrome Initialized")
params = {'behavior': 'allow', 'downloadPath': r'./'}


driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
driver.get(site_url)
driver.find_element_by_class_name('vjs-big-play-button').click()
WebDriverWait(driver, 2)
el = driver.find_element_by_id('appRoot')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el,100, 1845).click()

WebDriverWait(driver, 2)
action.move_to_element_with_offset(el,123, 1370).click()

# driver.find_element_by_id('DownloadTranscriptButton').click()
driver.close()
print ("Download button clicked")
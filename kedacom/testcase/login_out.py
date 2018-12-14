# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from kedacom.testcase import get_config


def pmc_login(ip, username="admin", password='kedacom#123'):
    browser = webdriver.Chrome()
    browser.get('http://%s/' % ip)
    browser.implicitly_wait(30)
    browser.find_element_by_css_selector('#btnPMCLogin').click()
    browser.find_element_by_id('userName').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)

    # 获取验证码
    code = browser.find_element_by_css_selector('#code > div').text
    browser.find_element_by_id('inputCode').send_keys(code)
    browser.find_element_by_id('pmcSubmit').click()
    return browser


def pmc_logout(browser):
    elements = browser.find_element_by_id('curUser')
    ActionChains(browser).move_to_element(elements).perform()
    browser.find_element_by_id('aLogout').click()
    browser.find_element_by_xpath('/html/body/div[6]/div[11]/div/button[1]/span').click()
    browser.close()

if __name__ == "__main__":
    config = get_config.Config()
    browser = pmc_login(config.ip)
    pmc_logout(browser)
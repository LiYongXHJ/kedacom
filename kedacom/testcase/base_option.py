# coding=utf-8

class BaseOption(object):
    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def close(self):
        self.driver.close()

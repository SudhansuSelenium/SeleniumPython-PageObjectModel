from utilities.baseClass import baseClass


class commonUtil(baseClass):

    def click(self, locator):
        self.locator = locator
        self.driver.find_element_by_xpath(self.locator).click()


commonUtil = commonUtil()
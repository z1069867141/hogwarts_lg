class BasePage:
    def find(self, by):
        return  driver.find_element(by)
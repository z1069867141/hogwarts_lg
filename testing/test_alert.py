from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from testing.base import Base


class TestAlert(Base):
    def testAlert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element(By.CSS_SELECTOR, "#draggable")
        drop = self.driver.find_element(By.CSS_SELECTOR, "#droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(2)

        print("点击 alert 确认")

        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, "#submitBTN").click()
        sleep(5)
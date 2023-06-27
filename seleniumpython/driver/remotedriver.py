from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# it will run the code in different systems by using below steps

driver=webdriver.Remote(
                command_executor='http://33.33.33.1:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("")

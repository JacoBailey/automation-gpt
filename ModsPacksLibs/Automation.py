from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Automation:
    
    def __init__(self, browser, secondsToTimeout, findBy) -> None:
        self.__browser = browser
        self.__secondsToTimeout = secondsToTimeout
        self.__findBy = findBy

    def findElement(self, element):
            try:
                WebDriverWait(self.__browser, self.__secondsToTimeout).until(EC.presence_of_element_located((self.__findBy, element)))
            except:
                print('\'FindElement\' method requires passing of html element string argument and creation of \'elementFinder\' object.')

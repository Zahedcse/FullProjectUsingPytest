from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "div:nth-child(1) > input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input#exampleInputPassword1")
    check = (By.CSS_SELECTOR, "form > div.form-check > label")
    gender = (By.CSS_SELECTOR, "select#exampleFormControlSelect1")
    radio = (By.CSS_SELECTOR, "div:nth-child(7) > div:nth-child(2) > label")
    form_submit = (By.CSS_SELECTOR, "form > input")
    success_text = (By.CSS_SELECTOR, "form-comp > div > div:nth-child(2) > div")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPass(self):
        return self.driver.find_element(*HomePage.password)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getRadio(self):
        return self.driver.find_element(*HomePage.radio)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.form_submit)

    def getText(self):
        return self.driver.find_element(*HomePage.success_text)

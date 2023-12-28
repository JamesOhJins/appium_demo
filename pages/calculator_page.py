from appium.webdriver.common.appiumby import AppiumBy

class CalculatorPage:
    
    digit_buttons = {digit: (AppiumBy.ID, f"com.sec.android.app.popupcalculator:id/calc_keypad_btn_{digit:02}") for digit in range(10)}
    
    add_button = (AppiumBy.ACCESSIBILITY_ID, "더하기")
    subtract_button = (AppiumBy.ACCESSIBILITY_ID, "빼기")
    multiply_button = (AppiumBy.ACCESSIBILITY_ID, "곱하기")
    divide_button = (AppiumBy.ACCESSIBILITY_ID, "나누기")
    equals_button = (AppiumBy.ACCESSIBILITY_ID, "계산")
    
    

    result_field = (AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_edt_formula")
    

    def __init__(self, driver):
        self.driver = driver

    def press_digit(self, digit):
        if not 0 <= digit <= 9:
            raise ValueError("Digit must be between 0 and 9")
        try:
            digit_button = self.digit_buttons[digit]
            self.driver.find_element(*digit_button).click()
        except Exception as e:
            raise Exception(f"Error clicking digit {digit}: {str(e)}")

    def press_add(self):
        try:
            self.driver.find_element(*self.add_button).click()
        except Exception as e:
            raise Exception("Error clicking add button: " + str(e))
    
    def press_subtract(self):
        try:
            self.driver.find_element(*self.subtract_button).click()
        except Exception as e:
            raise Exception("Error clicking subtract button: " + str(e))
    
    def press_multiply(self):
        try:
            self.driver.find_element(*self.multiply_button).click()
        except Exception as e:
            raise Exception("Error clicking multiply button: " + str(e))
    
    def press_divide(self):
        try:
            self.driver.find_element(*self.divide_button).click()
        except Exception as e:
            raise Exception("Error clicking divide button: " + str(e))

    def press_equals(self):
        try:
            self.driver.find_element(*self.equals_button).click()
        except Exception as e:
            raise Exception("Error clicking equals button: " + str(e))

    def get_result(self):
        try:
            return self.driver.find_element(*self.result_field).text
        except Exception as e:
            raise Exception("Error retrieving result: " + str(e))

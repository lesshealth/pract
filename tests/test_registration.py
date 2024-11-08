import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class RegistrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get('http://127.0.0.1:5000')
        cls.driver.implicitly_wait(10)

    def test_successful_registration(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000')
        
        # Заполнение полей
        driver.find_element(By.ID, "name").send_keys("test user")
        driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        driver.find_element(By.ID, "password").send_keys("testpass")
        
        # Отправка формы
        driver.find_element(By.ID, "submitBtn").click()
        
        # Ожидание ответа и проверка результата
        time.sleep(2)
        alert_text = driver.switch_to.alert.text
        self.assertIn("User registered successfully", alert_text)
        driver.switch_to.alert.accept()

    def test_empty_name_field(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000')
        
        driver.find_element(By.ID, "name").clear()
        driver.find_element(By.ID, "email").send_keys("test@gmail.com")
        driver.find_element(By.ID, "password").send_keys("testpass")
        
        driver.find_element(By.ID, "submitBtn").click()
        
        time.sleep(2)
        name_error = driver.find_element(By.ID, "nameError").text
        self.assertEqual(name_error, "Поле 'Имя' обязательно.")

    def test_invalid_email_format(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000')
        
        driver.find_element(By.ID, "name").send_keys("test user")
        driver.find_element(By.ID, "email").send_keys("notemailforsure")
        driver.find_element(By.ID, "password").send_keys("testpass")
        
        driver.find_element(By.ID, "submitBtn").click()
        
        time.sleep(2)
        email_error = driver.find_element(By.ID, "emailError").text
        self.assertEqual(email_error, "Введите корректный email.")

    def test_password_too_short(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000')
        
        driver.find_element(By.ID, "name").send_keys("test user")
        driver.find_element(By.ID, "email").send_keys("test@gmail.com")
        driver.find_element(By.ID, "password").send_keys("test")
        
        driver.find_element(By.ID, "submitBtn").click()
        
        time.sleep(2)
        password_error = driver.find_element(By.ID, "passwordError").text
        self.assertEqual(password_error, "Пароль должен содержать минимум 8 символов.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



# testing, testing, attention please

# testing, testing, attention please


# testing, testing, attention please
import random
import re
import string
import time

import mailslurp_client
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from base_class import BaseClass


class TestStoreSettings(BaseClass):

    def test_login(self):
        self.driver.get("https://oldtest.bumblebeeeee.com/login")
        self.driver.find_element(By.NAME, "username").send_keys("tester")
        self.driver.find_element(By.NAME, "password").send_keys("Raqz3Ts0D2fN")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[text()='New Workspace']").is_displayed())

    def test_register(self):
        configuration = mailslurp_client.Configuration()  # create a mail-slurp configuration
        configuration.api_key['x-api-key'] = "9c9f1a5e8203d8db15ff02b7a60b315fb6b14f4036c42d538b26a9a87debfce4"
        api_client = mailslurp_client.ApiClient(configuration)  # create a mail-slurp client
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)  # create an inbox
        inbox = inbox_controller.create_inbox()
        email_address = inbox.email_address
        wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)

        self.driver.get("https://oldtest.bumblebeeeee.com/login")  # open website
        self.driver.find_element(By.XPATH, "//span[text()='Create an account']").click()  # click create new account
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(
            email_address)  # insert new unregistered email address
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("P@ssw0rd")  # insert password

        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()  # click register
        self.email_content = wait_for_controller.wait_for_latest_email(inbox_id=inbox.id,
                                                                       timeout=30000)  # receive email
        otp = re.search('<p>OTP: <b>([0-9]{6})</b></p>', self.email_content.body).group(1)  # extract OTP from the email
        self.driver.find_element(By.XPATH, "//input[@placeholder='Verification code']").send_keys(otp)
        self.driver.find_element(By.XPATH, "//button[text()='Verify']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='First name']").send_keys("yahia")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last name']").send_keys("soliman")
        domain = ''.join(random.choices(string.ascii_lowercase, k=4))
        self.driver.find_element(By.XPATH, "//input[@placeholder='Domain name']").send_keys(domain)
        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='This domain name is available']")
        self.driver.find_element(By.XPATH, "//button[text()='Create Tenant']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[text()='Demo Dashboard']").is_displayed())

    def test_search_table_drag_drop(self):
        self.driver.get("https://oldtest.bumblebeeeee.com/login")

        self.driver.find_element(By.NAME, "username").send_keys("tester")
        self.driver.find_element(By.NAME, "password").send_keys("Raqz3Ts0D2fN")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[text()='New Workspace']").is_displayed())
        table_element = self.driver.find_element(By.XPATH,
                                                 "//ul[@class='MuiList-root MuiList-padding css-inu1m2']/li[2]")
        table_element.click()  # click on table icon
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("test")  # insert search query
        search_result_first_item = self.driver.find_element(By.XPATH, "//div[@class='ndt']")
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(search_result_first_item).click_and_hold(search_result_first_item).pause(
            1).release().perform()
        self.assertTrue(self.driver.find_element(By.XPATH, "//table/tbody/tr").is_displayed())

    def test_view_all_search_data(self):
        self.driver.get("https://oldtest.bumblebeeeee.com/login")

        self.driver.find_element(By.NAME, "username").send_keys("tester")
        self.driver.find_element(By.NAME, "password").send_keys("Raqz3Ts0D2fN")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[text()='New Workspace']").is_displayed())
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("test")  # insert search query
        self.driver.find_element(By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-1ontqvh']")
        self.driver.find_element(By.XPATH, "//span[text()='See All Data ']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[@role='presentation' and text()='Name']"))

    def test_search_filters(self):
        self.driver.get("https://oldtest.bumblebeeeee.com/login")
        self.driver.find_element(By.NAME, "username").send_keys("tester")
        self.driver.find_element(By.NAME, "password").send_keys("Raqz3Ts0D2fN")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[text()='New Workspace']").is_displayed())
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("test")  # insert search query
        self.driver.find_element(By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-1ontqvh']")
        self.driver.find_element(By.XPATH, "//span[text()='See All Data ']").click()
        self.driver.find_element(By.ID, "tasks-advanced-search").click()  # click on filter icon
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type']").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='Items']")  # wait for list to be displayed
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type']").send_keys("item")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type']").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//span[text()='Search']").click()
        time.sleep(5) # wait for list to be filtered
        list_of_items_types = self.driver.find_elements(By.XPATH, "//tbody/tr/td[8]")
        i = 1
        while i < len(list_of_items_types):
            actual_value = list_of_items_types[i].text
            self.assertTrue('Item', actual_value)
            i = i + 1

import time

from selenium.webdriver import ActionChains, Keys

from elementsSelectors import Selectors


class Interactions:

    @staticmethod
    def insert_login_username(driver, username):
        driver.find_element(*Selectors.login_username).send_keys(username)

    @staticmethod
    def insert_login_password(driver, password):
        driver.find_element(*Selectors.login_password).send_keys(password)

    @staticmethod
    def click_login(driver):
        driver.find_element(*Selectors.login_button).click()

    @staticmethod
    def is_new_workspace_button_displayed(driver):
        return driver.find_element(*Selectors.new_workspace_button).is_displayed()

    @staticmethod
    def click_create_new_account_button(driver):
        driver.find_element(*Selectors.create_account_button).click()

    @staticmethod
    def insert_unregistered_email_address(driver, email_address):
        driver.find_element(*Selectors.email_input_text).send_keys(email_address)

    @staticmethod
    def insert_new_account_password(driver, password):
        driver.find_element(*Selectors.new_account_password).send_keys(password)

    @staticmethod
    def click_register_button(driver):
        driver.find_element(*Selectors.register_button).click()

    @staticmethod
    def insert_otp(driver, otp):
        driver.find_element(*Selectors.otp_input_text).send_keys(otp)

    @staticmethod
    def click_verify_button(driver):
        driver.find_element(*Selectors.verify_button).click()

    @staticmethod
    def insert_first_name(driver, first_name):
        driver.find_element(*Selectors.first_name_input_text).send_keys(first_name)

    @staticmethod
    def insert_last_name(driver, last_name):
        driver.find_element(*Selectors.last_name_input_text).send_keys(last_name)

    @staticmethod
    def insert_domain(driver, domain):
        driver.find_element(*Selectors.domain_input_text).send_keys(domain)

    @staticmethod
    def find_domain_confirmation_icon(driver):
        driver.find_element(*Selectors.domain_confirmation_icon)

    @staticmethod
    def click_create_tenant(driver):
        driver.find_element(*Selectors.create_tenant_button).click()

    @staticmethod
    def is_demo_dashboard_title_displayed(driver):
        return driver.find_element(*Selectors.demo_dashboard_title).is_displayed()

    @staticmethod
    def click_side_menu_table_icon(driver):
        driver.find_element(*Selectors.side_menu_table_icon).click()

    @staticmethod
    def insert_search_query(driver, search_query):
        driver.find_element(*Selectors.search_input_text).send_keys(search_query)

    @staticmethod
    def drag_drop_search_result_first_item(driver):
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(driver.find_element(*Selectors.search_result_item)).click_and_hold(driver.find_element(*Selectors.search_result_item)).pause(
            1).release().perform()

    @staticmethod
    def is_table_first_raw_displayed(driver):
        return driver.find_element(*Selectors.table_first_row).is_displayed()

    @staticmethod
    def find_search_result_summary_container(driver):
        driver.find_element(*Selectors.search_result_summary_items_list_container)

    @staticmethod
    def click_see_all_data_button(driver):
        driver.find_element(*Selectors.see_all_search_results_data_button).click()

    @staticmethod
    def is_table_column_name_title_displayed(driver):
        return driver.find_element(*Selectors.table_name_column_title).is_displayed()

    @staticmethod
    def click_filter_icon(driver):
        driver.find_element(*Selectors.filter_icon).click()

    @staticmethod
    def click_type_filter_input_box(driver):
        driver.find_element(*Selectors.type_filter_input).click()

    @staticmethod
    def find_typs_list_container(driver):
        driver.find_element(*Selectors.list_of_types_container)

    @staticmethod
    def insert_value_into_type_filter_box(driver, type_value):
        driver.find_element(*Selectors.type_filter_input).send_keys(type_value)
        time.sleep(3)

    @staticmethod
    def click_enter_on_type_filter_box(driver):
        driver.find_element(*Selectors.type_filter_input).send_keys(Keys.ENTER)
        time.sleep(3)

    @staticmethod
    def click_search_button(driver):
        driver.find_element(*Selectors.search_button).click()
        time.sleep(8)  # wait for list to be filtered

    @staticmethod
    def get_list_of_table_items_types(driver):
        return driver.find_elements(*Selectors.table_item_types)











from baseClass import BaseClass
from interactions import Interactions
from testData import TestData


class TestStoreSettings(BaseClass):

    def test_login(self):
        self.driver.get(TestData.url)
        Interactions.insert_login_username(self.driver, TestData.username)
        Interactions.insert_login_password(self.driver, TestData.password)
        Interactions.click_login(self.driver)
        self.assertTrue(Interactions.is_new_workspace_button_displayed(self.driver))

    def test_register(self):
        inbox, wait_for_controller = TestData.create_new_email_inbox()
        self.driver.get(TestData.url)  # open website
        Interactions.click_create_new_account_button(self.driver)
        Interactions.insert_unregistered_email_address(self.driver, inbox.email_address)
        Interactions.insert_new_account_password(self.driver, TestData.new_account_password)
        Interactions.click_register_button(self.driver)
        self.email_content = wait_for_controller.wait_for_latest_email(inbox_id=inbox.id, timeout=30000)
        otp = TestData.get_otp_from_email_content(self.email_content.body)
        Interactions.insert_otp(self.driver, otp)
        Interactions.click_verify_button(self.driver)
        Interactions.insert_first_name(self.driver, TestData.new_account_first_name)
        Interactions.insert_last_name(self.driver, TestData.new_account_last_name)
        domain = TestData.generate_domain_name()
        Interactions.insert_domain(self.driver, domain)
        Interactions.find_domain_confirmation_icon(self.driver)
        Interactions.click_create_tenant(self.driver)
        self.assertTrue(Interactions.is_demo_dashboard_title_displayed(self.driver))

    def test_search_table_drag_drop(self):
        self.driver.get(TestData.url)
        Interactions.insert_login_username(self.driver, TestData.username)
        Interactions.insert_login_password(self.driver, TestData.password)
        Interactions.click_login(self.driver)
        self.assertTrue(Interactions.is_new_workspace_button_displayed(self.driver))
        Interactions.click_side_menu_table_icon(self.driver)
        Interactions.insert_search_query(self.driver, TestData.search_query)
        Interactions.drag_drop_search_result_first_item(self.driver)
        self.assertTrue(Interactions.is_table_first_raw_displayed(self.driver))

    def test_view_all_search_data(self):
        self.driver.get(TestData.url)
        Interactions.insert_login_username(self.driver, TestData.username)
        Interactions.insert_login_password(self.driver, TestData.password)
        Interactions.click_login(self.driver)
        self.assertTrue(Interactions.is_new_workspace_button_displayed(self.driver))
        Interactions.insert_search_query(self.driver, TestData.search_query)
        Interactions.find_search_result_summary_container(self.driver)
        Interactions.click_see_all_data_button(self.driver)
        self.assertTrue(Interactions.is_table_column_name_title_displayed(self.driver))

    def test_search_filters(self):
        self.driver.get(TestData.url)
        Interactions.insert_login_username(self.driver, TestData.username)
        Interactions.insert_login_password(self.driver, TestData.password)
        Interactions.click_login(self.driver)
        self.assertTrue(Interactions.is_new_workspace_button_displayed(self.driver))
        Interactions.insert_search_query(self.driver, TestData.search_query)
        Interactions.find_search_result_summary_container(self.driver)
        Interactions.click_see_all_data_button(self.driver)
        Interactions.click_filter_icon(self.driver)
        Interactions.click_type_filter_input_box(self.driver)
        Interactions.find_typs_list_container(self.driver)
        Interactions.insert_value_into_type_filter_box(self.driver, TestData.type_filter_value)
        Interactions.click_enter_on_type_filter_box(self.driver)
        Interactions.click_search_button(self.driver)
        list_of_items_types = Interactions.get_list_of_table_items_types(self.driver)
        i = 1
        while i < 10:
            actual_value = list_of_items_types[i].text
            self.assertEqual(TestData.type_filter_value, actual_value.lower())
            i = i + 1

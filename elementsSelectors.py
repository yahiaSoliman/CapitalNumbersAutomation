from selenium.webdriver.common.by import By


class Selectors:
    login_username = (By.NAME, "username")
    login_password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    new_workspace_button = (By.XPATH, "//div[text()='New Workspace']")
    create_account_button = (By.XPATH, "//span[text()='Create an account']")
    email_input_text = (By.XPATH, "//input[@type='email']")
    new_account_password = (By.XPATH, "//input[@type='password']")
    register_button = (By.XPATH, "//button[text()='Register']")
    otp_input_text = (By.XPATH, "//input[@placeholder='Verification code']")
    verify_button = (By.XPATH, "//button[text()='Verify']")
    first_name_input_text = (By.XPATH, "//input[@placeholder='First name']")
    last_name_input_text = (By.XPATH, "//input[@placeholder='Last name']")
    domain_input_text = (By.XPATH, "//input[@placeholder='Domain name']")
    domain_confirmation_icon = (By.CSS_SELECTOR, "[aria-label='This domain name is available']")
    create_tenant_button = (By.XPATH, "//button[text()='Create Tenant']")
    demo_dashboard_title = (By.XPATH, "//div[text()='Demo Dashboard']")
    side_menu_table_icon = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-inu1m2']/li[2]")
    search_input_text = (By.XPATH, "//input[@placeholder='Search']")
    search_result_item = (By.XPATH, "//div[@class='ndt']")
    table_first_row = (By.XPATH, "//table/tbody/tr")
    search_result_summary_items_list_container = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-1ontqvh']")
    see_all_search_results_data_button = (By.XPATH, "//span[text()='See All Data ']")
    table_name_column_title = (By.XPATH, "//div[@role='presentation' and text()='Name']")
    filter_icon = (By.ID, "tasks-advanced-search")
    type_filter_input = (By.XPATH, "//input[@placeholder='Type']")
    list_of_types_container = (By.XPATH, "//div[@aria-label='Items']")
    search_button = (By.XPATH, "//span[text()='Search']")
    table_item_types = (By.XPATH, "//tbody/tr/td[8]")












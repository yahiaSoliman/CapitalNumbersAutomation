import random
import re
import string

import mailslurp_client


class TestData:
    url = "https://oldtest.bumblebeeeee.com/login"
    username = "tester"
    password = "Raqz3Ts0D2fN"
    new_account_password = "P@ssw0rd"
    new_account_first_name = "yahia"
    new_account_last_name = "soliman"
    search_query = "test"
    type_filter_value = "item"

    # new email to be used in registration
    @staticmethod
    def create_new_email_inbox():
        configuration = mailslurp_client.Configuration()  # create a mail-slurp configuration
        configuration.api_key['x-api-key'] = "9c9f1a5e8203d8db15ff02b7a60b315fb6b14f4036c42d538b26a9a87debfce4"
        api_client = mailslurp_client.ApiClient(configuration)  # create a mail-slurp client
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)  # create an inbox
        email_inbox = inbox_controller.create_inbox()
        wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
        return email_inbox, wait_for_controller

    # otp to be used in registration
    @staticmethod
    def get_otp_from_email_content(email_content):
        return re.search('<p>OTP: <b>([0-9]{6})</b></p>', email_content).group(1)

    # domain name to be used in registration
    @staticmethod
    def generate_domain_name():
        return ''.join(random.choices(string.ascii_lowercase, k=4))




from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open soft.reelly page_')
def open_soft_reelly(context):
    context.app.main_page.open_main()
    sleep(5)


@when('Input name field')
def input_fields(context):
    context.app.login_page.input_fields()


@then('Input phone field')
def input_fields_phone(context):
    context.app.login_page.input_fields_phone()


@then('Input pwd field')
def input_fields_pwd(context):
    context.app.login_page.input_fields_pwd()


@then('Input comp_web field')
def input_fields_comp_web(context):
    context.app.login_page.input_fields_comp_web()


@then('Choose role field')
def dropdown_menu_role(context):
    context.app.login_page.dropdown_menu_role()


@then('Choose country field')
def dropdown_menu_country(context):
    context.app.login_page.dropdown_menu_country()


@then('Choose comp_size field')
def dropdown_menu_comp_size(context):
    context.app.login_page.dropdown_menu_comp_size()


@then('Press_on_the_button')
def click_create_account(context):
    context.app.login_page.click_create_account()


@then('Verify expected URL')
def verify_page(context):
    context.app.login_page.verify_page('https://soft.reelly.io/sign-up')


@then('Verify_the_button')
def verify_the_button(context):
    context.app.login_page.verify_the_button()


@given('Login to the page_')
def input_credentials(context):
    context.app.login_page.input_credentials()


@given('Click on continue button_')
def click_search_icon(context):
    context.app.login_page.click_sign_in()


@given('Click on settings open__')
def click_on_settings__(context):
    context.app.login_page.click_on_settings_()


@given('Click on Edit profile option_')
def edit_profile(context):
    context.app.login_page.edit_profile()


@given('Enter some test information in the input fields_')
def input_fields(context):
    context.app.login_page.input_fields_()
    sleep(3)


@given('Check the right information is present in the input fields')
def verify_input_fields(context):
    context.app.login_page.verify_input_fields_()


@given('Click on Save changes_')
def click_on_save_(context):
    context.app.login_page.click_save_changes_()


@given('Click on “Connect the company”')
def click_on_page_company(context):
    context.app.login_page.click_on_page_company()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print("Current:", context.original_window)
    print('All windows: ', context.driver.window_handles)


@given('Switch to new window')
def click_on_page_company(context):
    context.app.login_page.switch_to_new_window()


@given('Verify the right tab opens')
def verify_new_tab_page(context):
    expected_url = 'https://soft.reelly.io/book-presentation'
    actual_url = context.app.login_page.verify_new_tap_page(expected_url)
    assert actual_url == expected_url, f"Expected URL {expected_url}, but got {actual_url}"


@given('Close the current page and switch back')
def close_and_switch_back(context):
    # Close the current window
    context.driver.close()
    # Switch back to the original window
    context.driver.switch_to.window(context.original_window)


@given('Login to the page')
def input_credentials(context):
    context.app.login_page.input_credentials()


@given('Click on continue button')
def click_search_icon(context):
    context.app.login_page.click_sign_in()



@given('Click on Edit profile option')
def edit_profile(context):
    context.app.login_page.edit_profile()


@given('Enter some test information in the input fields')
def input_fields(context):
    context.app.login_page.input_fields()
    sleep(3)


@then('Click on Close_')
def click_on_close_(context):
    context.app.login_page.click_on_close_()

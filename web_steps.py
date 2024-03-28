from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("https://example.com")  # Replace with the URL of your web application

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    button_locator = (By.XPATH, f"//button[text()='{button_text}']")
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(button_locator)).click()

@then('I should see "{expected_text}"')
def step_impl(context, expected_text):
    assert expected_text in context.driver.page_source

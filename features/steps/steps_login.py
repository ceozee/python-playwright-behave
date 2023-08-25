from behave import step
from behave.api.async_step import async_run_until_complete
from pages.login_page import LoginPage


@step('user is in login page')
@async_run_until_complete
async def step_imp(context):
    context.login_page = LoginPage(context.page)

    await context.login_page.visit_login_page()


@step('user enters "{username}" username')
@async_run_until_complete
async def step_impl(context, username):
    await context.login_page.enter_username(username)


@step('user enters "{password}" password')
@async_run_until_complete
async def step_impl(context, password):
    await context.login_page.enter_password(password)


@step('click login')
@async_run_until_complete
async def step_impl(context):
    await context.login_page.click_login_button()


@step('error message "{message}" is displayed')
@async_run_until_complete
async def step_impl(context, message):
    await context.login_page.assert_error_message(message)


@step('user is redirected to inventory page')
@async_run_until_complete
async def step_impl(context):
    await context.login_page.assert_url(f'{context.login_page.URL}inventory.html')

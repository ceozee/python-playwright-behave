from playwright.async_api import Page, expect

class LoginPage:

    def __init__(self, page:Page) -> None:
        self.page = page
        self.URL = 'https://www.saucedemo.com/'

        # Locators
        self.username_field = page.locator('id=user-name')
        self.password_filed = page.locator('id=password')
        self.login_button = page.locator('id=login-button')
        self.login_error_message = page.locator('data-test=error')

        # Actions

    async def visit_login_page(self) -> None:
        await self.page.goto(self.URL, timeout=5000)

    async def enter_username(self, username) -> None:
        await self.username_field.fill(username)

    async def enter_password(self, password) -> None:
        await self.password_filed.fill(password)

    async def click_login_button(self) -> None:
        await self.login_button.click()

    async def assert_error_message(self, message) -> None:
        await expect(self.login_error_message).to_contain_text(message)

    async def assert_url(self, current_url) -> None:
        await expect(self.page).to_have_url(current_url)




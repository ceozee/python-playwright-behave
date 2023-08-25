from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright


@fixture
async def browser_chromium(context):
    start_playwright = await async_playwright().start()
    browser = await start_playwright.chromium.launch(headless=False, channel="chromium")
    context.page = await browser.new_page()


@async_run_until_complete
async def before_scenario(context, args):
    await use_fixture(browser_chromium, context)


@async_run_until_complete
async def after_scenario(context, args):
    await context.page.close()

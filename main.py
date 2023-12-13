import time as t
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import pyautogui as pg

expect.set_options(timeout=10_000)

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Altere o valor de headless para False
    page = browser.new_page()
    page.goto("https://www.youtube.com")
    page.get_by_placeholder("Pesquisar").fill("python")
    page.get_by_role("button", name="Pesquisar", exact=True).dblclick()
    page.get_by_role("button", name="Pesquisar", exact=True).dblclick()
    #page.get_by_role("button", name="Pesquisar", exact=True).click(position={ "x": 0, "y": 0})
    input()

    """
    # screeshot example
    page.screenshot(path="example.png")
    """
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(headless=False,args=["--start-maximized"])
page = browser.new_page(no_viewport=True)

page.goto("https://finance.naver.com/")

##################################################
page.get_by_role("link", name="삼성전자").nth(1).click()
page.wait_for_selector(".no_up", state="attached")
price = page.locator(".no_up .blind").first.inner_text()
print("삼성전자 시가:", price)

page.fill(".search_input", "애플")
page.press(".search_input", "Enter")

page.screenshot(path = "search_result.png")

browser.close()
##################################################
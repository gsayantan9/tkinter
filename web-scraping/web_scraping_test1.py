# import asyncio
# from playwright.async_api import async_playwright, Playwright

# async def run(playwright: Playwright):
#     iphone_13 = playwright.devices['iPhone 13']
#     browser = await playwright.webkit.launch(headless=False)
#     # context = await browser.new_context(
#     #     **iphone_13,
#     context = await browser.new_context(geolocation={"longitude": 41.890221, "latitude": 12.492348},
#                                         permissions=["geolocation"]
#   )

# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)
# asyncio.run(main())
# import cv2
# import easyocr
# import matplotlib.pyplot as plt
# from selenium import webdriver

# part_number = "49058"
# page_url = f"https://shop.advanceautoparts.com/web/SearchResults?searchTerm={part_number}&storeId=10151&catalogId=10051&langId=-1"
# browser = webdriver.ChromeOptions()
# browser.add_argument('--headless')
# driver = webdriver.Chrome(options=browser)
# driver.get(page_url)
# driver.save_screenshot(f"{part_number}.jpeg")
# image_path = "/workspaces/tkinter/web-scraping/advance_auto_49058.jpeg"
# img = cv2.imread(image_path)
# reader = easyocr.Reader(["en"],gpu=False)
# text_list = reader.readtext(img)
# for t in text_list:
#     print(t)


import asyncio
import time
from playwright.async_api import async_playwright 
part_number = 49058
target_url = 'https://shop.advanceautoparts.com/web/StoreLocatorDetailView?stAddressId=7750'  # Replace with the actual URL
async def take_screenshot():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(target_url) # load the page
        await page.wait_for_timeout(5000)
        print("*****************taking screenshot of the page after entering the url********************")
        await page.screenshot(path="page_screenshot.png",full_page=True)
        button = await page.query_selector('button[aria-label="Make My Store"]')
        await page.wait_for_timeout(5000)
        if button:
                button_class = await button.get_attribute('class')
                aria_disabled = await button.get_attribute('aria-disabled')
                await page.wait_for_timeout(5000)
                if 'outline css-1qb2vam' in button_class and aria_disabled == 'false':
                # Click the button if the conditions are met
                    await button.click()
                    print("**************Initiate the store selection******************")
                    await page.wait_for_timeout(5000)
                    elements = await page.locator("#search-input").fill(f"{part_number}") 
                    await page.keyboard.press("Enter")
                    await page.wait_for_timeout(5000)
                    await page.screenshot(path="parts_set.jpg",full_page=True)
                else:
                    print("***********Store already set***************")
                    elements = await page.locator("#search-input").fill(f"{part_number}") 
                    await page.keyboard.press("Enter")
                    await page.wait_for_timeout(5000)
                    await page.screenshot(path="parts_set.jpg",full_page=True)
        else:
            print("button not found!")

loop = asyncio.get_event_loop()
start_time = time.time()
loop.run_until_complete(take_screenshot())
end_time = time.time()
print(end_time-start_time)


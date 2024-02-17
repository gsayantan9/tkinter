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
import cv2
import easyocr
import matplotlib.pyplot as plt
from selenium import webdriver

# part_number = "49058"
# page_url = f"https://shop.advanceautoparts.com/web/SearchResults?searchTerm={part_number}&storeId=10151&catalogId=10051&langId=-1"
# browser = webdriver.ChromeOptions()
# browser.add_argument('--headless')
# driver = webdriver.Chrome(options=browser)
# driver.get(page_url)
# driver.save_screenshot(f"{part_number}.jpeg")
image_path = "/workspaces/tkinter/web-scraping/advance_auto_49058.jpeg"
img = cv2.imread(image_path)
reader = easyocr.Reader(["en"],gpu=False)
text_list = reader.readtext(img)
for t in text_list:
    print(t)

      
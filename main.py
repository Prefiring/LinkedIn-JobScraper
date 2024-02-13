from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.chrome.service import Service

s = Service("D:\Selenium\chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.get("https://www.linkedin.com/jobs/search?keywords=Business%20Analysis&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

job_listings = driver.find_elements(By.XPATH, '//*[@id="main-content"]/section[2]/ul/li')

with open('job_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Job Title', 'Address', 'Job Link'])    #write the header row


    for listing in job_listings:
        job_title_element = listing.find_element(By.CLASS_NAME, 'sr-only')
        job_title = job_title_element.text
        print("Job Title:", job_title)
        address_element = listing.find_element(By.CLASS_NAME, 'base-search-card__metadata')
        address = address_element.text

        print("Address:", address)
        link_element = listing.find_element(By.CLASS_NAME, 'base-card__full-link')
        job_link = link_element.get_attribute('href')

        print("Job Link:", job_link)
        print("-" * 50)
        csv_writer.writerow([job_title, address, job_link])  #write rows

driver.quit()  #close the browser

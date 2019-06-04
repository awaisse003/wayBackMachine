import csv
import datetime
import os
import requests
from selenium import webdriver

mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
if not os.path.exists(mydir):
    os.makedirs(mydir)
f = open(mydir+'/notfound.txt','w')
domain = []
notfound = []
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=';')
    for row in readCSV:

        domain.append(row[1])
i = 1


def do_actions(domain):
    link = resp.json()["archived_snapshots"]["closest"]["url"]
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    driver.set_page_load_timeout(65)
    try:
        driver.get(link)
        screenshot = driver.save_screenshot(mydir + '/' + domain[i] + '.png')
    finally:
        screenshot = driver.save_screenshot(mydir + '/' + domain[i] + '.png')
        notfound.append(domain[i])
        driver.quit()

while i < len(domain):
    url = 'http://archive.org/wayback/available?url=https://'+domain[i]
    try:
        resp = requests.get(url)
    except:
        resp = requests.get(url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    try:
        do_actions(domain)

    except:
        notfound.append(domain[i])


    i += 1
str1 = " ".join(str(x) for x in notfound)
f.write('Error sites are :' + str(str1))
f.close()


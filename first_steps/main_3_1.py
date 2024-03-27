import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

# # Your provided information
# username = "dfddf"
# password = "232323"
# redirect = ["./ucp.php?mode=login", "index.php"]
# sid = "76c2b0eeff9d43b5d2f67c2b50f4c761"
# login = "Вход"  # Assuming this is the login button label

# # Create a dictionary with the data
# data = {
#     'username': username,
#     'password': password,
#     'redirect': redirect,
#     'sid': sid,
#     'login': login
# }

data = {
    
    'username': 'argentinavs1984', 
    'password' : '123456',
    'redirect': ["./ucp.php?mode=login", "index.php"],
    'sid': "76c2b0eeff9d43b5d2f67c2b50f4c761",
    'login': "Вход"
}
link = 'https://ribalovers.ru/forum/ucp.php?mode=login'

# username=dfddf&password=232323&redirect=.%2Fucp.php%3Fmode%3Dlogin&sid=76c2b0eeff9d43b5d2f67c2b50f4c761&redirect=index.php&login=%D0%92%D1%85%D0%BE%D0%B4

user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

responce = session.post(link, data=data, headers=header)
# print(responce)

profile_info = 'https://ribalovers.ru/forum/ucp.php?i=profile&mode=reg_details'
profile_responce = session.get(profile_info, headers=header).text

# print(profile_responce)

with open("2.html", "w", encoding="utf-8") as file:
    file.write(profile_responce)

# Session
#Authorization
# Get/set cookies

# https://pornolab.net/forum/login.php
# http://forum.ru-board.com/misc.cgi
# login_username=argentinavs1984&login_username=123456&login=%C2%F5%EE%E4
# lesson_test: 12345678

# link  = 
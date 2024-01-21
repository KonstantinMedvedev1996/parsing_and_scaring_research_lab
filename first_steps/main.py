import requests

# link  = 'https://icanhazip.com/'
link = 'https://browser-info.ru/'

# responce = requests.get(link)
responce = requests.get(link).text
# responce = requests.get(link).content




# print(responce.text)
# print(responce.status_code)

with open("1.html", "w", encoding="utf-8") as file:
    file.write(responce)
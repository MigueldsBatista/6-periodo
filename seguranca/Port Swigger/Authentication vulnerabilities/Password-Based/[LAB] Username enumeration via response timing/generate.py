import pathlib

WORKSPACE = pathlib.Path(__file__).parent

ips = [
    f"127.0.0.{num}" for num in range(1, 101)
]

with open(WORKSPACE / "ips.txt", "w") as f:
    f.writelines("\n".join(ips))
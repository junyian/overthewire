from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit10", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell["strings data.txt | base64 -d"]
    txt = txt.decode().split()  # split multiline result
    txt = txt[-1].split()  # get last line and split based on separators
    return txt[-1]


if __name__ == "__main__":
    print(main("FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey"))

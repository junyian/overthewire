from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit11", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell[
        "strings data.txt | tr ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    ]
    txt = txt.decode().split()  # split multiline result
    txt = txt[-1].split()  # get last line and split based on separators
    return txt[-1]


if __name__ == "__main__":
    print(main("dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr"))

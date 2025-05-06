from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit7", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell["cat data.txt | grep millionth"]
    return txt.decode().split()[1]


if __name__ == "__main__":
    print(main("morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj"))

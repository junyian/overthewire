from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit1", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell["cat ./-"]
    return txt.decode()


if __name__ == "__main__":
    print(main("ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If"))

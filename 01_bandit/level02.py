from pwn import ssh


def main(password: str) -> str | None:
    shell = ssh("bandit2", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell[r"cat ./spaces\ in\ this\ filename"]
    return txt.decode()


if __name__ == "__main__":
    print(main("263JGJPfgU6LtdEvgfWU1XP5yac29mFx"))

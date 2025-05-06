from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit5", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell["find ./inhere -size 1033c"]
    txt = shell[f"cat {txt.decode()}"]
    return txt.decode()


if __name__ == "__main__":
    print(main("4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw"))

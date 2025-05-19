from pwn import ssh


def main(password: str) -> str:
    with ssh(
        "bandit14", "bandit.labs.overthewire.org", 2220, password=password
    ) as shell:
        io = shell.process(["nc", "localhost", "30000"])
        io.sendline(password.encode())
        txt = io.recv()

    txt = txt.split()
    return txt[-1].decode()


if __name__ == "__main__":
    print(main("MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS"))

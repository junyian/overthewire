from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit13", "bandit.labs.overthewire.org", 2220, password=password)
    shell.download("sshkey.private")
    shell.close()
    shell = ssh(
        "bandit14", "bandit.labs.overthewire.org", 2220, keyfile="sshkey.private"
    )
    txt = shell["cat /etc/bandit_pass/bandit14"]
    return txt.decode()


if __name__ == "__main__":
    print(main("FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn"))

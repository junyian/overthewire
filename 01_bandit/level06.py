from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit6", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell[
        'find / -size 33c -printf "%u %g %p\\n" 2>/dev/null | grep "bandit7 bandit6"'
    ]
    txt = shell[f"cat {txt.decode().split(' ')[2]}"]
    return txt.decode()


if __name__ == "__main__":
    print(main("HWasnPhtq9AVKe0dmk45nxy20cvUa6EG"))

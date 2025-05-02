from pwn import ssh
import re


def main() -> str | None:
    shell = ssh("bandit0", "bandit.labs.overthewire.org", 2220, password="bandit0")
    txt = shell["cat ./readme"]
    m = re.match(r".*The password you are looking for is: (\w+).*", str(txt))
    if m is not None:
        return m.group(1)
    else:
        return None


if __name__ == "__main__":
    print(main())

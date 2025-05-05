from pwn import ssh
import re


def main(password: str) -> str | None:
    shell = ssh("bandit4", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell["ls -la ./inhere"]
    lines = txt.splitlines()
    for line in lines:
        m = re.match(r".*( .*)$", line.decode())
        if m is not None:
            filename = m.group(1).strip()
            if len(filename) > 2:
                txt = shell[f"cat ./inhere/{filename}"]
                try:
                    m2 = re.match(r"\w+", txt.decode())
                    if m2 is not None:
                        return m2.group(0)
                except UnicodeDecodeError:
                    pass
    return None


if __name__ == "__main__":
    print(main("2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ"))

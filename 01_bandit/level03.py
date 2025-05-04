from pwn import ssh
import re

def main(password: str) -> str | None:
    shell = ssh("bandit3", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell[r"ls -la ./inhere"]
    lines = txt.splitlines()
    for line in lines:
        m = re.match(r".*( \..*)$", line.decode())
        if m is not None:
            filename = m.group(1).strip()
            if len(filename) > 2:
                txt = shell[f"cat ./inhere/{filename}"]
                return txt.decode()
    return None

if __name__ == "__main__":
    print(main("MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx"))

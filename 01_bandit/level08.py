from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit8", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell['sort data.txt | uniq -c | grep "1 "']
    return txt.decode().split()[1]


if __name__ == "__main__":
    print(main("dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc"))

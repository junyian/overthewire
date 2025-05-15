from pwn import ssh


def main(password: str) -> str:
    shell = ssh("bandit12", "bandit.labs.overthewire.org", 2220, password=password)
    txt = shell["mktemp -d"]
    cmds = []
    cmds.append(f"cp data.txt {txt.decode()}")
    cmds.append(f"cd {txt.decode()}")
    cmds.append("xxd -r data.txt data2.bin.gz")
    cmds.append("gunzip data2.bin.gz")
    cmds.append("bunzip2 data2.bin")
    cmds.append("mv data2.bin.out data4.bin.gz")
    cmds.append("gunzip data4.bin.gz")
    cmds.append("tar xvf data4.bin")
    cmds.append("tar xvf data5.bin")
    cmds.append("bunzip2 data6.bin")
    cmds.append("tar xvf data6.bin.out")
    cmds.append("mv data8.bin data8.bin.gz")
    cmds.append("gunzip data8.bin.gz")
    cmds.append("strings data8.bin")
    txt = shell[";".join(cmds)]

    print(txt.decode())
    txt = txt.decode().split()  # split multiline result
    txt = txt[-1].split()  # get last line and split based on separators
    return txt[-1]


if __name__ == "__main__":
    print(main("7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4"))

from pwn import ssh


def main(password: str) -> str:
    with ssh(
        "bandit15", "bandit.labs.overthewire.org", 2220, password=password
    ) as shell:
        io = shell.process(["openssl", "s_client", "localhost:30001"])
        print(io.recvuntil(b"read R BLOCK"))
        print(io.recvuntil(b"read R BLOCK"))
        io.sendline(password.encode())
        print(io.recv())
        txt = io.recv()

    return txt.split()[1].decode()


if __name__ == "__main__":
    print(main("8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo"))

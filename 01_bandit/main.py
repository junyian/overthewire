import level00
import level01


def main() -> None:
    print("Hello from overthewire!")
    nextpass = level00.main()
    print(f"Level 0 -> Level 1: {nextpass}")

    if nextpass is not None:
        nextpass = level01.main(nextpass)
        print(f"Level 1 -> Level 2: {nextpass}")
    else:
        return


if __name__ == "__main__":
    main()

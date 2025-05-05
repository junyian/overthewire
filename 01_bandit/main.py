import level00
import level01
import level02
import level03
import level04


def main() -> None:
    print("Hello from OvertheWire!")
    nextpass = level00.main()
    print(f"Level 0 -> Level 1: {nextpass}")

    if nextpass is not None:
        nextpass = level01.main(nextpass)
        print(f"Level 1 -> Level 2: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level02.main(nextpass)
        print(f"Level 2 -> Level 3: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level03.main(nextpass)
        print(f"Level 3 -> Level 4: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level04.main(nextpass)
        print(f"Level 4 -> Level 5: {nextpass}")
    else:
        return


if __name__ == "__main__":
    main()

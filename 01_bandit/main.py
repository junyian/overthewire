import level00
import level01
import level02
import level03
import level04
import level05
import level06
import level07
import level08
import level09
import level10
import level11
import level12
import level13
import level14
import level15


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

    if nextpass is not None:
        nextpass = level05.main(nextpass)
        print(f"Level 5 -> Level 6: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level06.main(nextpass)
        print(f"Level 6 -> Level 7: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level07.main(nextpass)
        print(f"Level 7 -> Level 8: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level08.main(nextpass)
        print(f"Level 8 -> Level 9: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level09.main(nextpass)
        print(f"Level 9 -> Level 10: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level10.main(nextpass)
        print(f"Level 10 -> Level 11: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level11.main(nextpass)
        print(f"Level 11 -> Level 12: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level12.main(nextpass)
        print(f"Level 12 -> Level 13: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level13.main(nextpass)
        print(f"Level 13 -> Level 14: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level14.main(nextpass)
        print(f"Level 14 -> Level 15: {nextpass}")
    else:
        return

    if nextpass is not None:
        nextpass = level15.main(nextpass)
        print(f"Level 15 -> Level 16: {nextpass}")
    else:
        return


if __name__ == "__main__":
    main()

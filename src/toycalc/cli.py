import argparse

from toycalc.core import add, fib


def main():
    parser = argparse.ArgumentParser(prog="toycalc")
    sub = parser.add_subparsers(dest="cmd", required=True)

    addp = sub.add_parser("add")
    addp.add_argument("a", type=int)
    addp.add_argument("b", type=int)

    fibp = sub.add_parser("fib")
    fibp.add_argument("n", type=int)

    args = parser.parse_args()
    if args.cmd == "add":
        print(add(args.a, args.b))
    elif args.cmd == "fib":
        print(fib(args.n))


if __name__ == "__main__":
    main()

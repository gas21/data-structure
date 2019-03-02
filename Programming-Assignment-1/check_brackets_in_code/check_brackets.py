# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i))

        if next in ")]}":
            opened = opening_brackets_stack.pop()
            if not are_matching(opened[0], next):
                print(i+1)
                return
    if opening_brackets_stack:
        print(opening_brackets_stack.pop()[1] + 1)
    else:
        print("Success")


def main():
    text = input()
    find_mismatch(text)


if __name__ == "__main__":
    main()

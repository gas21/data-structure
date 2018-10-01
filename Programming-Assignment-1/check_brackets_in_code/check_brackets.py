# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    opening_brackets_stack = []
    j = True
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            a = Bracket(next, i)
            opening_brackets_stack.append(a)
        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                print(i+1)
                j = False
                break
            else:
                b = opening_brackets_stack.pop()
                if b.Match(next) is False:
                    print(i+1)
                    j = False
                    break
    if j is True and not opening_brackets_stack:
        print("Success")
        j = False
    if j is True:
        print(opening_brackets_stack[0].position+1)
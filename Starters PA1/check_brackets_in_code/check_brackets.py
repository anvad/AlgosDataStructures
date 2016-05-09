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
    for i, next in enumerate(text):
        #print("i, next", i, next)
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                bracket = opening_brackets_stack.pop()
                if not bracket.Match(next):
                    print(i+1)
                    break
            else:
                print(i+1)
                break
            pass

    # Printing answer, write your code here
    if (len(text) == i+1):
        if (len(opening_brackets_stack) > 0):
            bracket = opening_brackets_stack.pop()
            print(bracket.position)
        else:
            print("Success")

def check_brackets(_text: str) -> str:
    brackets = {'(': ')', '{': '}', '[': ']'}
    open_brackets_stack = []

    def is_open_bracket(_c: str):
        return c in brackets.keys()

    def is_close_bracket(_c: str):
        return c in brackets.values()

    for c in _text:
        if is_open_bracket(c):
            open_brackets_stack.append(c)

        elif is_close_bracket(c):
            if not open_brackets_stack:
                return "False"

            last_open_bracket = open_brackets_stack.pop()

            if c != brackets[last_open_bracket]:
                return "False"

    return "True"


if __name__ == '__main__':
    text = input()
    print(check_brackets(text))

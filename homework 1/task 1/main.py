def check_brackets():
    brackets = {'(': ')', '{': '}', '[': ']'}
    open_brackets_stack = []

    def is_open_bracket(c):
        return c in brackets.keys()

    def is_close_bracket(c):
        return c in brackets.values()

    text = input()

    for c in text:
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
    print(check_brackets())

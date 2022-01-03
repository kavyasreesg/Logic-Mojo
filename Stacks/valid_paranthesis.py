"""
Check if input paranthesis is valid or not
"""


def check_validity(string):
    stack = list()
    if len(string) % 2 != 0:
        return False
    for character in string:
        if character == '{':
            stack.append('}')
        elif character == '[':
            stack.append(']')
        elif character == '(':
            stack.append(')')
        else:
            if not stack or stack.pop() != character:
                return False
    return not stack


str_in = '{()}[{}]'
print(check_validity(str_in))

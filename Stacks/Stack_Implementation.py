import unittest


class Stack(object):
    """
    Last In First Out Operation
    """
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    def pop(self):
        if len(self.stack) <= 0:
            return "No elements to Pop"
        element = self.stack.pop()
        return element


class Test(unittest.TestCase):
    def test_stack1(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        popped_element = stack.pop()
        self.assertEqual(popped_element, 20)

    def test_stack2(self):
        stack2 = Stack()
        stack2.push(11)
        stack2.push(19)
        expected = [11, 19]
        self.assertEqual(expected, stack2.stack)


unittest.main(verbosity=2)  # or python3 -m unittest testfile.py -vvv

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# Test 1: Empty stack
stack = Stack()
assert stack.is_empty() is True

# Test 2: Push elements
stack.push(10)
stack.push(20)
assert stack.is_empty() is False

# Test 3: LIFO order
assert stack.pop() == 20
assert stack.pop() == 10

# Test 4: Empty stack error
try:
    stack.pop()
    raise AssertionError("Expected IndexError")
except IndexError:
    pass

print("PASS: Data Structures - 4/4 tests")
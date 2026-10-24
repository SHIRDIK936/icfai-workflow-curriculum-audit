import sqlite3


# Exercise 1: Computer Programming
def find_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


# Exercise 2: Data Structures
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]


# Exercise 3: Database Management Systems
def test_sql():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE orders (
            order_id INTEGER,
            customer_id INTEGER,
            amount INTEGER
        )
    """)

    cursor.executemany(
        "INSERT INTO orders VALUES (?, ?, ?)",
        [
            (1, 101, 200),
            (2, 101, 300),
            (3, 102, 150),
        ],
    )

    cursor.execute("""
        SELECT customer_id, SUM(amount)
        FROM orders
        GROUP BY customer_id
        ORDER BY customer_id
    """)

    result = cursor.fetchall()
    connection.close()

    assert result == [(101, 500), (102, 150)]


# Exercise 4: Machine Learning
def test_data_leakage():
    # Demonstrates the correct order of operations.
    # This checks a split-first workflow, not a trained ML model.
    dataset = list(range(10))

    train = dataset[:8]
    test = dataset[8:]

    assert len(train) == 8
    assert len(test) == 2
    assert set(train).isdisjoint(set(test))

    train_mean = sum(train) / len(train)

    # The mean is calculated from training data only.
    assert train_mean == 3.5


# Exercise 5: Deep Learning
def convolution_output(size, kernel, stride, padding):
    return ((size + 2 * padding - kernel) // stride) + 1


def run_test(name, test_function):
    try:
        test_function()
        print(f"PASS: {name}")
        return True
    except Exception as error:
        print(f"FAIL: {name} - {error}")
        return False


def test_programming():
    assert find_max([4, 9, 2]) == 9
    assert find_max([-5, -2, -8]) == -2
    assert find_max([7]) == 7


def test_stack():
    stack = Stack()
    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.pop() == 10

    try:
        stack.pop()
        raise AssertionError("Expected an empty-stack error")
    except IndexError:
        pass


def test_convolution():
    assert convolution_output(32, 3, 1, 0) == 30


if __name__ == "__main__":
    tests = [
        ("Computer Programming", test_programming),
        ("Data Structures", test_stack),
        ("Database Management Systems", test_sql),
        ("Machine Learning", test_data_leakage),
        ("Deep Learning", test_convolution),
    ]

    results = [
        run_test(name, test_function)
        for name, test_function in tests
    ]

    print()
    print(f"Results: {sum(results)}/{len(results)} tests passed")

    if not all(results):
        raise SystemExit(1)
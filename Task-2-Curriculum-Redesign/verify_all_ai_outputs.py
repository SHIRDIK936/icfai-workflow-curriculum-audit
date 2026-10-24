from pathlib import Path
import sqlite3
from datetime import datetime

BASE = Path(__file__).resolve().parent
DATE = datetime.now().strftime("%d %B %Y")

results = []


def check(subject, name, condition):
    if not condition:
        raise AssertionError(f"{subject}: {name}")
    results.append((subject, name, "PASS"))


# ==================================================
# EXERCISE 1: COMPUTER PROGRAMMING
# ==================================================

def find_max(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


check("Computer Programming", "Positive numbers",
      find_max([1, 5, 3]) == 5)

check("Computer Programming", "Negative numbers",
      find_max([-8, -2, -10]) == -2)

check("Computer Programming", "Single element",
      find_max([7]) == 7)

check("Computer Programming", "Duplicate values",
      find_max([4, 4, 4]) == 4)


# ==================================================
# EXERCISE 2: DATA STRUCTURES
# ==================================================

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


stack = Stack()

check("Data Structures", "Initially empty",
      stack.is_empty())

stack.push(10)
stack.push(20)

check("Data Structures", "Push operations",
      not stack.is_empty())

check("Data Structures", "LIFO order",
      stack.pop() == 20 and stack.pop() == 10)

raised = False

try:
    stack.pop()
except IndexError:
    raised = True

check("Data Structures", "Empty-stack exception",
      raised)


# ==================================================
# EXERCISE 3: DATABASE MANAGEMENT SYSTEMS
# ==================================================

sql_query = """
SELECT lab_id, COUNT(*) AS approved_count
FROM bookings
WHERE status = 'APPROVED'
GROUP BY lab_id;
"""

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY,
    lab_id TEXT,
    status TEXT
)
""")

cursor.executemany(
    "INSERT INTO bookings VALUES (?, ?, ?)",
    [
        (1, "LAB-A", "APPROVED"),
        (2, "LAB-A", "APPROVED"),
        (3, "LAB-A", "REJECTED"),
        (4, "LAB-B", "APPROVED"),
        (5, "LAB-B", "PENDING"),
    ]
)

db_results = dict(cursor.execute(sql_query).fetchall())

check("DBMS", "LAB-A approved count",
      db_results.get("LAB-A") == 2)

check("DBMS", "LAB-B approved count",
      db_results.get("LAB-B") == 1)

check("DBMS", "Exclude non-approved records",
      sum(db_results.values()) == 3)

connection.close()


# ==================================================
# EXERCISE 4: MACHINE LEARNING
# ==================================================

# AI explanation being evaluated:
#
# Data leakage occurs when information unavailable
# at prediction time enters model training.
#
# Example:
# Fitting a scaler on the complete dataset before
# splitting into training and testing sets.
#
# Prevention:
# Split data first, then fit preprocessing steps
# only on the training data.

ml_explanation = {
    "definition": (
        "Data leakage occurs when information unavailable "
        "at prediction time influences model training."
    ),
    "example": (
        "Fitting a scaler on the complete dataset "
        "before splitting into training and test sets."
    ),
    "prevention": (
        "Split the data first and fit preprocessing "
        "only on the training data."
    )
}

check("Machine Learning", "Definition recorded",
      bool(ml_explanation["definition"]))

check("Machine Learning", "Example recorded",
      bool(ml_explanation["example"]))

check("Machine Learning", "Prevention recorded",
      bool(ml_explanation["prevention"]))


# ==================================================
# EXERCISE 5: DEEP LEARNING
# ==================================================

# Formula:
# Output = floor((Input + 2*Padding - Kernel)/Stride) + 1

input_size = 32
kernel = 3
padding = 0
stride = 1
filters = 16

output_height = ((input_size + 2 * padding - kernel) // stride) + 1
output_width = ((input_size + 2 * padding - kernel) // stride) + 1

check("Deep Learning", "Output height",
      output_height == 30)

check("Deep Learning", "Output width",
      output_width == 30)

check("Deep Learning", "Output channels",
      filters == 16)


# ==================================================
# PRINT RESULTS
# ==================================================

print("\nAI OUTPUT VERIFICATION RESULTS")
print("=" * 50)

for subject, name, status in results:
    print(f"{subject}: {name} - {status}")

print("=" * 50)
print(f"Total: {len(results)}/{len(results)} checks passed")


# ==================================================
# GENERATE VERIFICATION REPORT
# ==================================================

report = f"""# AI Output Verification Report

**Institution:** ICFAI Tech, Hyderabad
**Programme:** B.Tech Artificial Intelligence and Machine Learning
**Verification Date:** {DATE}

## Important Evidence Note

The responses below were supplied or discussed using
ChatGPT (GPT-6) during a guided academic exercise.

The Python and SQL reference outputs were tested locally.

The Machine Learning explanation received a structural
completeness check and a manual conceptual review.
The automated checks do not establish its factual correctness.

These are limited verification exercises, not proof of
complete model reliability.

---

## Exercise 1: Computer Programming

**AI Model:** ChatGPT (GPT-6)

**Prompt:**
Write a Python function to find the maximum number
in a non-empty list without using max().

**Recorded Output:**

```python
def find_max(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
    ```

**Verification:** Four Python test cases.

**Result:** PASS - 4/4.

---

## Exercise 2: Data Structures

**AI Model:** ChatGPT (GPT-6)

**Prompt:** Implement a Stack with push, pop, and is_empty.

**Recorded Output:** Stack implementation tested in this project.

**Verification:** Empty stack, push, LIFO, and exception handling.

**Result:** PASS - 4/4.

---

## Exercise 3: Database Management Systems

**AI Model:** ChatGPT (GPT-6)

**Prompt:** Count approved bookings for each laboratory.

**Recorded Output:**

```sql
SELECT lab_id, COUNT(*) AS approved_count
FROM bookings
WHERE status = 'APPROVED'
GROUP BY lab_id;
```

**Verification:** SQLite database with synthetic records.

**Result:** PASS - 3/3.

---

## Exercise 4: Machine Learning

**AI Model:** ChatGPT (GPT-6)

**Prompt:** Explain data leakage and how to prevent it.

**Recorded Output:**

Definition: {ml_explanation["definition"]}

Example: {ml_explanation["example"]}

Prevention: {ml_explanation["prevention"]}

**Verification:** Three structural completeness checks.

**Result:** PASS - 3/3 structural checks.

---

## Exercise 5: Deep Learning

**AI Model:** ChatGPT (GPT-6)

**Prompt:** Calculate convolution output dimensions for
32x32 input, 3x3 kernel, stride 1, padding 0,
and 16 filters.

**Recorded Output:**

Output = floor((Input + 2*Padding - Kernel)/Stride) + 1

Output shape = 30 x 30 x 16

**Verification:** Three mathematical checks.

**Result:** PASS - 3/3.

---

## Limitations

- Synthetic test data was used.
- Tests cover only selected examples.
- Machine Learning checks verify the presence of explanation components, not factual correctness.
- AI-generated examples were provided through a guided ChatGPT interaction.
- The reported verification date is the execution date.
"""

output = BASE / "ai_output_verification.md"
output.write_text(report, encoding="utf-8")

print(f"\nReport generated: {output}")
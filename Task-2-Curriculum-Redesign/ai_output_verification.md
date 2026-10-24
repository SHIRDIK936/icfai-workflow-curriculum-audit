# AI Output Verification Report

**Institution:** ICFAI Tech, Hyderabad
**Programme:** B.Tech Artificial Intelligence and Machine Learning
**Verification Date:** 24 October 2026

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

Definition: Data leakage occurs when information unavailable at prediction time influences model training.

Example: Fitting a scaler on the complete dataset before splitting into training and test sets.

Prevention: Split the data first and fit preprocessing only on the training data.

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

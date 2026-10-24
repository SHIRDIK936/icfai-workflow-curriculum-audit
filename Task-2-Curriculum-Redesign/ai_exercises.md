# AI-Assisted Exercise Evaluation

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission batch:** 2023–2027  
**Prepared:** 24 October 2026

## Objective

Evaluate how AI assistance can support learning in five existing curriculum courses while identifying risks such as incorrect answers, fabricated claims, and overreliance on generated solutions.

All examples use synthetic inputs. No student records, confidential institutional data, or personal information are required.

**Evaluation status:** The exercises below are proposed test cases. AI-generated responses and actual execution results must be recorded before they can be described as completed experiments.

## Exercise 1 — Computer Programming

**Task:** Write a Python function that returns the largest number in a list.

**AI prompt:**

> Write a Python function to find the maximum value in a non-empty list without using Python's built-in max() function. Explain the logic.

**Expected solution characteristics:**

- Initialize the largest value using the first list element.
- Compare each subsequent element.
- Return the largest value.
- Explain how empty lists should be handled.

**Verification cases:**

| Input | Expected output |
|---|---:|
| `[4, 9, 2]` | 9 |
| `[-5, -2, -8]` | -2 |
| `[7]` | 7 |

**Potential AI failure:** Initializing the maximum to zero gives incorrect results for all-negative lists.

**Human verification:** Review the initialization and execute all three tests.

## Exercise 2 — Data Structures

**Task:** Implement a stack using Python.

**AI prompt:**

> Implement a stack using a Python list with push, pop, and peek operations. Explain the time complexity of each operation.

**Expected solution characteristics:**

- Push adds an item to the end of the list.
- Pop removes the last item.
- Peek returns the last item without removing it.
- Empty-stack operations are handled safely.

**Verification cases:**

| Operation | Expected result |
|---|---|
| Push 10, push 20, pop | 20 |
| Push 10, push 20, peek | 20 |
| Pop on empty stack | Defined error or safe empty response |

**Potential AI failure:** Incorrect handling of empty stacks.

**Human verification:** Execute normal and boundary cases.

## Exercise 3 — Database Management Systems

**Task:** Write an SQL aggregation query.

**AI prompt:**

> Given a table `orders(order_id, customer_id, amount)`, write an SQL query to calculate the total order amount for each customer.

**Expected SQL:**

```sql
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;
```

**Synthetic input:**

| order_id | customer_id | amount |
|---|---|---:|
| 1 | 101 | 200 |
| 2 | 101 | 300 |
| 3 | 102 | 150 |

**Expected output:**

| customer_id | total_amount |
|---|---:|
| 101 | 500 |
| 102 | 150 |

**Potential AI failure:** Omitting `GROUP BY` or incorrectly grouping by `order_id`.

**Human verification:** Execute the query against a temporary test database.

## Exercise 4 — Machine Learning

**Task:** Identify data leakage.

**AI prompt:**

> Explain why fitting a StandardScaler on the entire dataset before splitting into training and test sets causes data leakage. Provide a corrected scikit-learn approach.

**Expected answer characteristics:**

- Explain that test-set statistics must not influence model training.
- Split the data before fitting preprocessing operations.
- Fit preprocessing using training data only.
- Prefer a pipeline for cross-validation.

**Verification approach:** Review the generated code to ensure preprocessing is fitted only on training folds.

**Potential AI failure:** Presenting code that still fits the scaler on the complete dataset.

## Exercise 5 — Deep Learning

**Task:** Calculate output dimensions after convolution.

**AI prompt:**

> A convolutional layer receives a 32×32 image and uses a 3×3 kernel, stride 1, and zero padding. What is the output spatial dimension? Explain the calculation.

**Expected calculation:**

\[
\text{Output}=\left\lfloor\frac{N+2P-K}{S}\right\rfloor+1
\]

For \(N=32\), \(P=0\), \(K=3\), and \(S=1\):

\[
\text{Output}=\frac{32-3}{1}+1=30
\]

**Expected result:** 30×30.

**Potential AI failure:** Confusing zero padding with same padding and incorrectly reporting 32×32.

**Human verification:** Check the formula manually and optionally confirm using a deep learning framework.

## Evaluation Summary

| Course | AI-assisted task | Verification method | Status |
|---|---|---|---|
| Computer Programming | Maximum in a list | Python test cases | Pending execution |
| Data Structures | Stack implementation | Boundary tests | Pending execution |
| Database Management Systems | SQL aggregation | SQLite test database | Pending execution |
| Machine Learning | Data leakage prevention | Code review and pipeline check | Pending execution |
| Deep Learning | Convolution dimensions | Formula verification | Pending execution |

## Educational Recommendations

1. Require students to submit their original AI prompts.
2. Require students to identify at least one possible AI error.
3. Include executable tests or independent calculations.
4. Grade explanations and verification, not just generated code.
5. Require disclosure of AI assistance.

## Limitations

These are proposed AI-assisted exercises with independently specified expected answers. They do not constitute evidence that an AI tool produced correct or incorrect responses.

Actual AI responses, test outcomes, and dates should be appended after execution. No classroom deployment or faculty approval is claimed.
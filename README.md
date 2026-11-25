# 🎓 Python Week 1 — Grade Calculator

A beginner-friendly Python project covering **core Week 1 fundamentals**:
functions, loops, and dictionaries.

---

## 📚 Concepts Covered

| Concept | Usage in this project |
|---|---|
| **Dictionary** | `GRADE_BOUNDARIES` maps letter grades to minimum scores; `students` maps names to score lists |
| **Functions** | Modular functions for input, calculation, and display |
| **`for` loop** | Iterating over grades, scores, and student records |
| **`while` loop** | Continuous input collection until the user is done |
| **`if / else`** | Input validation and grade boundary checks |
| **f-strings** | Formatted, aligned console output |
| **`try / except`** | Handles invalid numeric input gracefully |

---

## 🚀 How to Run

Make sure you have **Python 3.x** installed.

```bash
python grade_calculator.py
```

No external libraries needed — pure Python!

---

## 💡 Features

- Enter **multiple students** with any number of subject scores
- Automatically assigns a **letter grade** (A+ through F) based on score boundaries
- Shows a **formatted grade report** with per-student averages
- Calculates the overall **class average**
- Input validation with clear error messages

---

## 📊 Grade Boundaries

| Grade | Minimum Score |
|-------|--------------|
| A+    | 95%          |
| A     | 85%          |
| B+    | 75%          |
| B     | 65%          |
| C+    | 55%          |
| C     | 45%          |
| D     | 35%          |
| F     | 0%           |

---

## 📋 Sample Output

```
=======================================================
                   GRADE CALCULATOR
=======================================================
Grade Boundaries:
-------------------------
  A+    >=  95%
  A     >=  85%
  ...

Student name (or 'done'): Alice
    Score: 92
    Score: 78
    Score: 88
    Score:

Student name (or 'done'): Bob
    Score: 55
    Score: 60
    Score:

Student name (or 'done'): done

=======================================================
                     GRADE REPORT
=======================================================
Student              Average  Grade  Scores
-------------------------------------------------------
Alice                  86.0%      A  [92, 78, 88]
Bob                    57.5%     C+  [55, 60]
=======================================================
Class Average:         71.8%     B+
=======================================================
```

---

## 🗂️ Project Structure

```
pythonweek1/
└── grade_calculator.py   # Main script
└── README.md             # Project documentation
```

---

## 👤 Author

**Bhavesh** — Python Week 1 Practice Project

---

> Built as part of a Python fundamentals learning series.

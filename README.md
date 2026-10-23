# Student Grade Processor

A modular Python script built to process student academic records, calculate grade statistics, and enforce strict score boundaries using custom domain exceptions and type annotations.

This project focuses on writing clean, production-grade Python: zero monolithic scripts, pure separation of concerns, and defensive data validation.

Developed as part of the **Elevvo Internship Program**.

---

In entry-level scripts, input handling, business logic, and printing usually sit in one giant loop. Here, the architecture is intentionally split into two distinct layers:

1. **`grade_processor.py`**  
   Contains zero `print()` or `input()` calls. It accepts data, transforms it, and either returns new records or raises domain-specific exceptions. Because it doesn't touch the terminal directly, you can import this module into a web API, a background worker, or a CLI without changing a single line of logic.

2. **`main.py`**  
   Handles standard output formatting and intercepts exceptions. It tests both the happy path (valid records) and the edge cases (corrupt/out-of-bound scores).

---

### Architectural Decisions

- **Custom Exception Propagation (`InvalidScoreError`)**:  
  Rather than relying on generic `ValueError` or printing error strings inside processing functions, the engine raises an explicit `InvalidScoreError`. Errors propagate up the call stack so the caller (`main.py`) decides how to handle them.
- **Immutability First**:  
  When generating pass/fail statuses, dictionaries are not mutated in place. We produce fresh records using dictionary unpacking (`{**student, "status": ...}`), preventing side effects across downstream consumers.
- **Type Safety with `TypedDict`**:  
  Instead of generic `dict` structures where keys can easily be misspelled, records use `Student(TypedDict)` to guarantee contract predictability (`name: str`, `score: float`).
- **$O(N)$ Min/Max Lookup**:  
  Finding highest and lowest scores relies on Python's built-in `min()` and `max()` with `key=lambda`, avoiding the performance penalty of sorting the entire list just to pull two values.

---

### Repository Layout

```text
student-grade-processor/
├── grade_processor.py   # Pure processing module & domain exceptions
├── main.py              # CLI test harness & report runner
└── README.md            # Documentation
```

---

### How to Run

Clone the repository and run the runner file with Python 3.9+:

```bash
python -m main.py
```

### What You'll See

The runner executes two distinct scenarios:

1. **Normal Flow**: Calculates the class average, finds top/bottom performers, and tabulates pass/fail records against a threshold.
2. **Defensive Validation Flow**: Injects scores outside the $0 - 100$ boundary (e.g., `150.0`) to demonstrate graceful exception interception without application crashes.

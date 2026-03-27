# Code Review AI Environment

## Overview

This project implements a real-world OpenEnv environment where an AI agent performs automated code reviews.

The agent analyzes code, identifies issues, explains them, and suggests improvements — similar to how a human developer reviews code.

---

## Motivation

Code review is a critical task in software development. This environment allows training and evaluating AI agents on realistic code review scenarios.

---

## Environment Design

### Observation Space

* `code`: The code snippet to review
* `difficulty`: easy / medium / hard

### Action Space

* `issue`: Identified problems in the code
* `explanation`: Explanation of the issues

### Reward System

* Partial rewards based on:

  * Correct issue detection
  * Quality of explanation
* Penalty for incorrect or poor responses

Reward range: **-0.2 to 1.0**

---

## Tasks

### Easy

* Single bug detection
* Example: assignment vs comparison

### Medium

* Security-related issues
* Example: hardcoded passwords

### Hard

* Multiple issues
* Example: authentication flaws, missing validation

---

## Grading Logic

* Score based on number of correctly identified issues
* Additional score for explanation quality
* Normalized between 0.0 and 1.0

---

## How to Run

### Local

```bash
python inference.py
```

### Docker

```bash
docker build -t code-review-env .
docker run code-review-env
```

---

## Baseline Behavior

* Uses OpenAI API if API key is provided
* Falls back to a default action if not

---

## Future Improvements

* Multi-language support (Python, C++, JS)
* More realistic datasets
* Advanced grading using semantic similarity

---

## Author

Rohi Jagli
Rohan Leo
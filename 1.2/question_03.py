# DigolTech — Python Internship Assessment
# Part 3 — Hard (Questions 9–10)

# ==========================================
# Q9. Student Result Debugging
# Error Type: Logical error (2 issues)
# Issue 1: total = mark overwrote total instead of accumulating (total += mark).
# Issue 2: Hardcoded 500 instead of dynamic max marks (len(marks) * 100).
# ==========================================
def q9():
    marks = [80, 75, 90, 65, 70]

    total = 0

    for mark in marks:
        total += mark

    max_marks = len(marks) * 100
    percentage = (total / max_marks) * 100 if max_marks > 0 else 0

    if percentage >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    print("Total:", total)
    print("Percentage:", percentage)
    print("Result:", result)


# ==========================================
# Q10. Shopping Cart Debugging
# Error Type: Logical error
# Issue: total = item[1] overwrote total instead of accumulating (total += item[1]).
# ==========================================
def q10():
    cart = [
        ["Keyboard", 800],
        ["Mouse", 400],
        ["USB Cable", 200]
    ]

    total = 0

    for item in cart:
        total += item[1]

    if total >= 1000:
        discount = total * 10 / 100
    else:
        discount = 0

    final_amount = total - discount

    print("Total:", total)
    print("Discount:", discount)
    print("Final Amount:", final_amount)


if __name__ == "__main__":
    print("--- Q9 ---")
    q9()
    print("--- Q10 ---")
    q10()

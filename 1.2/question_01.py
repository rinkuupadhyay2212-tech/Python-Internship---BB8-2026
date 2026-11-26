# DigolTech — Python Internship Assessment
# Part 1 — Easy (Questions 1–5)

# ==========================================
# Q1. Syntax Error
# Error Type: Syntax error
# Issue: Missing closing parenthesis ')' on line 2.
# ==========================================
def q1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    total_sum = a + b
    print("Sum:", total_sum)


# ==========================================
# Q2. Incorrect Variable Usage
# Error Type: Logical error
# Issue: Used addition (+) instead of multiplication (*) for area.
# ==========================================
def q2():
    length = 10
    width = 5

    area = length * width
    print("Area:", area)


# ==========================================
# Q3. Loop Error
# Error Type: Logical error
# Issue: range(1, 10) stops at 9; changed to range(1, 11) to include 10.
# ==========================================
def q3():
    for i in range(1, 11):
        print(i)


# ==========================================
# Q4. Incorrect Condition
# Error Type: Logical error
# Issue: Swapped "Even" and "Odd" outputs for number % 2 == 0.
# ==========================================
def q4():
    number = 15

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# ==========================================
# Q5. List Index Error
# Error Type: Runtime error (IndexError)
# Issue: Index 4 is out of bounds for a 4-item list; used -1 for last item.
# ==========================================
def q5():
    fruits = ["Apple", "Banana", "Mango", "Orange"]
    print(fruits[-1])


if __name__ == "__main__":
    print("--- Q1 ---")
    # q1()  # Uncomment to run interactive input
    print("--- Q2 ---")
    q2()
    print("--- Q3 ---")
    q3()
    print("--- Q4 ---")
    q4()
    print("--- Q5 ---")
    q5()

# DigolTech — Python Internship Assessment
# Part 2 — Medium (Questions 6–8)

# ==========================================
# Q6. Function + Return Error
# Error Type: Logical error
# Issue: Function did not return the computed result.
# ==========================================
def square(number):
    result = number * number
    return result


def q6():
    print(square(6))


# ==========================================
# Q7. List Calculation Error
# Error Type: Logical error
# Issue: Checked number % 2 == 1 (odd) instead of number % 2 == 0 (even).
# ==========================================
def q7():
    numbers = [10, 15, 20, 25, 30, 35]

    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    print("Even Sum:", total)


# ==========================================
# Q8. Exception Handling
# Error Type: Runtime error (ZeroDivisionError, NameError) & Logical error
# Issue: Added ZeroDivisionError handler, matched exact error strings,
#        and moved print("Result:", result) inside the try block.
# ==========================================
def q8():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = a / b
        print("Result:", result)

    except ValueError:
        print("Invalid input.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")


if __name__ == "__main__":
    print("--- Q6 ---")
    q6()
    print("--- Q7 ---")
    q7()
    print("--- Q8 ---")
    # q8()  # Uncomment to run interactive input

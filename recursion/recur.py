#recursion is a function which calls itself.
#it is used to directly use a mathametical formula as function.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"Factorial of this number is: {factorial(n)}")



#infinte recursion: this is basically wrong:

def infinite_recursion():
    # This function calls itself
    # There is NO stopping condition (base case)
    # So it will keep calling itself again and again

    print("Function is calling itself...")
    infinite_recursion()   # recursive call

# Function call
infinite_recursion()

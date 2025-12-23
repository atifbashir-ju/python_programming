#WAP using function to find greatest of three numbers
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c   # handles the remaining case

a = 34
b = 4
c = 89

print(greatest(a, b, c))

#WAP using function  to convert celsius into fahrenheit
def f_to_c(f):
    return 5 * (f - 32) / 9

f = float(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)

print(f"Temperature in Celsius: {c:.2f}")

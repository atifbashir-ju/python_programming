def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

pattern(5)


# Write a python function to remove given word from list and strip it at the same time

def remove_and_strip(words, remove_word):
    new_list = []
    for word in words:
        stripped_word = word.strip()
        if stripped_word != remove_word:
            new_list.append(stripped_word)
    return new_list

# given list
words = ["  Atif  ", " Banana ", " apple ", " Banana "]

# function call
print(remove_and_strip(words, "Banana"))

from collections import deque

def is_palindrome(input_string):
    cleaned_string = " ".join(char.lower() for char in input_string if char.isalnum())
    char_deque = deque(cleaned_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

if __name__ == "__main__":
    test_strings = [
        "1234321",
        "1234567",
        "Сіно ніс",
        "Пилип",
        "Сир і рис.",
        "Кому думок?",
        "Це не паліндром.",
        "Я несу гусеня."
    ]

    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {'Паліндром' if result else 'НЕ паліндром'}")
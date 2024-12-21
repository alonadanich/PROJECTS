def are_delimiters_symmetric(expression):
    matching_pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []

    for char in expression:
        if char in matching_pairs.keys():
            stack.append(char)
        elif char in matching_pairs.values():
            if stack and matching_pairs[stack[-1]] == char:
                stack.pop()
            else:
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

if __name__ == "__main__":
    test_cases = [
        "(){[ 6 ]( 4 - 2 )( ){ }}",
        "( 45 ( 3 + 2);",
        "(5765765}",
        "{ [ [ ( ) ] ] }",
        "( { [ ( ] } )",
        "(11}",
        "( { [ ( ( ] ] } ) )"
    ]

    for test in test_cases:
        result = are_delimiters_symmetric(test)
        print(f"'{test}' -> {result}")
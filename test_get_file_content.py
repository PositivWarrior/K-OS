from functions.get_file_content import get_file_content

def run_tests():
    # Test Truncation
    print("Testing lorem.txt (Truncation check):")
    lorem_result = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(lorem_result)}")
    if "truncated" in lorem_result:
        print("Successfully truncated.")
    print("-" * 30)

    # Test main.py
    print("get_file_content('calculator', 'main.py'):")
    print(get_file_content("calculator", "main.py"))
    print("-" * 30)

    # Test nested file
    print("get_file_content('calculator', 'pkg/calculator.py'):")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("-" * 30)

    # Test Path escape
    print("get_file_content('calculator', '/bin/cat'):")
    print(get_file_content("calculator", "/bin/cat"))
    print("-" * 30)

    # Test Missing file
    print("get_file_content('calculator', 'pkg/does_not_exist.py'):")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    run_tests()
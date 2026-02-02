from functions.run_python_file import run_python_file

def run_tests():
    # Test 1: Basic execution (Usage info)
    print("--- Test 1: main.py (No args) ---")
    print(run_python_file("calculator", "main.py"))
    print("-" * 30)

    # Test 2: Execution with arguments
    print("--- Test 2: main.py (3 + 5) ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("-" * 30)

    # Test 3: Running internal tests
    print("--- Test 3: tests.py ---")
    print(run_python_file("calculator", "tests.py"))
    print("-" * 30)

    # Test 4: Security Escape
    print("--- Test 4: Outside Directory ---")
    print(run_python_file("calculator", "../main.py"))
    print("-" * 30)

    # Test 5: Missing file
    print("--- Test 5: Nonexistent file ---")
    print(run_python_file("calculator", "nonexistent.py"))
    print("-" * 30)

    # Test 6: Wrong file type
    print("--- Test 6: Non-Python file ---")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    run_tests()
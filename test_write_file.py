from functions.write_files import write_file

def run_tests():
    # Test 1: Overwriting existing file
    print('write_file("calculator", "lorem.txt", ...):')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("-" * 30)

    # Test 2: Creating a new file in a new subdirectory
    print('write_file("calculator", "pkg/morelorem.txt", ...):')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("-" * 30)

    # Test 3: Security block for outside directory
    print('write_file("calculator", "/tmp/temp.txt", ...):')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    run_tests()
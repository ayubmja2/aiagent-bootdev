from functions.get_file_content import get_file_content

def test() -> None:
    # Test 1: Large file truncation (lorem.txt)
    print("Testing lorem.txt truncation...")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    # Test 2: Valid file in root
    print('get_file_content("calculator", "main.py"):')
    print(get_file_content("calculator", "main.py"))
    print("")

    # Test 3: Valid file in subdirectory
    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("")

    # Test 4: Outside permitted directory
    print('get_file_content("calculator", "/bin/cat"):')
    print(get_file_content("calculator", "/bin/cat"))
    print("")

    # Test 5: Non-existent file
    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("")

if __name__ == "__main__":
    test()

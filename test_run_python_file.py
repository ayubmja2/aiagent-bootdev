from functions.run_python_file import run_python_file

def test() -> None:
    # Test 1: Run main.py without args (Usage instructions)
    print('run_python_file("calculator", "main.py"):')
    print(run_python_file("calculator", "main.py"))
    print("-" * 40)

    # Test 2: Run main.py with args (Calculation)
    print('run_python_file("calculator", "main.py", ["3 + 5"]):')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("-" * 40)

    # Test 3: Run tests.py
    print('run_python_file("calculator", "tests.py"):')
    print(run_python_file("calculator", "tests.py"))
    print("-" * 40)

    # Test 4: Attempt to run outside working directory
    print('run_python_file("calculator", "../main.py"):')
    print(run_python_file("calculator", "../main.py"))
    print("-" * 40)

    # Test 5: Non-existent file
    print('run_python_file("calculator", "nonexistent.py"):')
    print(run_python_file("calculator", "nonexistent.py"))
    print("-" * 40)

    # Test 6: File that is not a Python file
    print('run_python_file("calculator", "lorem.txt"):')
    print(run_python_file("calculator", "lorem.txt"))
    print("-" * 40)

if __name__ == "__main__":
    test()

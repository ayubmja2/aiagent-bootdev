from functions.get_files_info import get_files_info


def test() -> None:
    # Test 1: Current directory
    print('get_files_info("calculator", "."):')
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    # Indent the list of files
    print("\n".join([f"  {line}" for line in result.splitlines()]))
    print("")

    # Test 2: Subdirectory 'pkg'
    print('get_files_info("calculator", "pkg"):')
    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    # Indent the list of files
    print("\n".join([f"  {line}" for line in result.splitlines()]))
    print("")

    # Test 3: Outside directory /bin
    print('get_files_info("calculator", "/bin"):')
    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    # Indent the error message
    print(f"    {result}")
    print("")

    # Test 4: Outside directory ../
    print('get_files_info("calculator", "../"):')
    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    # Indent the error message
    print(f"    {result}")
    print("")


if __name__ == "__main__":
    test()

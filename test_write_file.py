from functions.write_file import write_file

def test() -> None:
    # Case 1: Overwriting an existing file in the root
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("")

    # Case 2: Writing to a file in a subdirectory (creates dir if missing)
    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("")

    # Case 3: Attempting to write outside the permitted directory
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("")

if __name__ == "__main__":
    test()

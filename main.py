def get_book_test(file_path: str) -> str:
    with open(file_path,'r') as file:
        file_contents = file.read()
    
    return file_contents

def main() -> None:
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_test(file_path)
    print(file_contents)

if __name__ == '__main__':
    main()
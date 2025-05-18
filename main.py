from stats import get_num_words, get_char_map, get_sorted_char_nums


def get_book_test(file_path: str) -> str:
    with open(file_path,'r') as file:
        file_contents = file.read()
    
    return file_contents

def build_report(word_count: int, char_map: dict) -> str:
    title: str = "============ BOOKBOT ============"
    description: str = "Analyzing book found at books/frankenstein.txt..."
    word_count_header: str = "----------- Word Count ----------"
    word_count_str: str = f"Found {word_count} total words"
    char_count_header: str = "--------- Character Count -------"
    char_count_str: str = ""
    sorted_char_nums: list[dict] = get_sorted_char_nums(char_map)
    for e in sorted_char_nums:
        char_count_str += f"{e['char']}: {e['num']}\n"
    ending_str: str = "============= END ==============="

    return '\n'.join([title, description, word_count_header, word_count_str, char_count_header, char_count_str + ending_str])





def main() -> None:
    file_path: str = 'books/frankenstein.txt'
    file_contents: str = get_book_test(file_path)
    word_count: int = get_num_words(file_contents)
    char_map: dict = get_char_map(file_contents)
    report: str = build_report(word_count, char_map)
    print(report)
    

if __name__ == '__main__':
    main()
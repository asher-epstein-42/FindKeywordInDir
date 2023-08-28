import os
import docx
import argparse


def main():
    keyword, dir_path, create_txt_file = menu()
    matching_lines = search_files_with_keywords(dir_path, keyword)

    if create_txt_file:
        write_lines_to_file(matching_lines, keyword)
    else:
        print_lines_to_console(matching_lines, keyword)


# search for files with the keyword in their content
def search_files_with_keywords(path_dir: str, keyword: str):
    matching_lines = []

    for foldername, subfolders, filenames in os.walk(path_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if filename.endswith(".txt"):
                matching_lines.extend(search_keyword_in_txt(keyword, file_path))

            elif filename.endswith(".docx"):
                matching_lines.extend(search_keyword_in_docx(keyword, file_path))

    return matching_lines


# search lines with the keyword in a txt file
def search_keyword_in_txt(keyword: str, file_path: str):
    matching_txt_lines = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # The utf-8 encoding is for reading non-ASCII characters
            for line_number, line in enumerate(file, start=1):
                if keyword in line:
                    matching_txt_lines.append(f"{file_path} - {line.strip()}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return matching_txt_lines


# search lines with the keyword in a docx file
def search_keyword_in_docx(keyword: str, file_path: str):
    matching_docx_lines = []

    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            if keyword in paragraph.text:
                matching_docx_lines.append(f"{file_path} - {paragraph.text}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return matching_docx_lines


# create a text file with all the lines with the keywords
def write_lines_to_file(matching_lines: list, keyword: str):
    if matching_lines:
        with open(f'Lines_with_{keyword}.txt', "w",
                  encoding='utf-8') as f:  # The utf-8 encoding is for reading non-ASCII characters
            f.write(f"Lines containing the keyword '{keyword}':\n")
            for line in matching_lines:
                f.write(f'{line}\n')
    else:
        print(f"No lines containing the keyword '{keyword}' were found.")


# print all the lines to the console
def print_lines_to_console(matching_lines: list, keyword: str):
    if matching_lines:
        print(f"Lines containing the keyword {keyword} :")
        for line in matching_lines:
            print(line)
    else:
        print(f"No lines containing the keyword {keyword} were found.")


def menu():
    parser = argparse.ArgumentParser(
        description="Search for a keyword in any language recursively in docx and txt files in a directory")
    parser.add_argument("keyword", help="The keyword to search for")
    parser.add_argument("dir_path", help="The directory path to search in")
    parser.add_argument("-f", "--file", action="store_true",
                        help="create a text file with all the lines with the keyword")
    args = parser.parse_args()
    return args.keyword, args.dir_path, args.file


if __name__ == '__main__':
    main()

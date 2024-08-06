BOOK_FILE_NAME = "encrypted_book.txt"


def get_book_content(file_path):
  with open(file_path, "r") as handle:
    return handle.read()


def main():
  encrypted_book = get_book_content(BOOK_FILE_NAME)
  print(encrypted_book[:500])


if __name__ == "__main__":
  main()

from src.files.finder import Finder
from src.files.utils.list import list_files_recursive


if __name__ == "__main__":
    files = list_files_recursive("./src")
    finder = Finder(files=files, regexp="baba")
    for result in finder:
        print(result)

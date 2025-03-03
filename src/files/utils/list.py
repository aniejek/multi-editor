import os


def _is_binary_file(file_path):
    """
    Checks if a file is binary by reading its first 1024 bytes and looking for a null byte.
    """
    try:
        with open(file_path, "rb") as file:
            chunk = file.read(1024)
            if b"\0" in chunk:
                return True
    except Exception:
        pass
    return False


def list_files_recursive(path, ignore_hidden=True, ignore_binary=True):
    """
    Recursively lists files in the given directory 'path'.

    Parameters:
      - ignore_hidden: If True, ignores hidden files and directories (starting with '.').
      - ignore_binary: If True, ignores files identified as binary.

    Returns:
      A list of file paths.
    """
    files = []
    for entry in os.listdir(path):
        if ignore_hidden and entry.startswith("."):
            continue
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            files.extend(list_files_recursive(full_path, ignore_hidden, ignore_binary))
        else:
            if ignore_binary and _is_binary_file(full_path):
                continue
            files.append(full_path)
    return files

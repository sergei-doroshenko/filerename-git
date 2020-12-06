# Disk usage
# !/usr/bin/python3
import os
import sys
import time


def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if not os.path.islink(entry):
                if entry.is_file():
                    # if it's a file, use stat() function
                    total += entry.stat().st_size
                elif entry.is_dir():
                    # if it's a directory, recursively call this function
                    total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:05.2f}Y{suffix}"


def du(scan_path):
    """Disk usage in human readable format (e.g. '2,1GB')"""
    print(f"Scanning {scan_path} ...")
    start = time.time()
    total_size = 0
    result = []

    for entry in os.scandir(scan_path):
        path = entry.path
        size = get_directory_size(path)
        total_size += size
        result.append((path, size))

    result.sort(key=lambda _: _[1], reverse=True)

    for tup in result:
        print('{0:100} - {1}'.format(tup[0], get_size_format(tup[1])))

    end = time.time()
    print(f"Total {scan_path} size={get_size_format(total_size)}, Scan time={end - start:.2f}sec")


if __name__ == "__main__":
    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Argument List: {str(sys.argv)}")

    if len(sys.argv) < 2:
        raise Exception("Provide scan root, please. E.g.: F:\\")
    du(sys.argv[1])

    # du("E://")

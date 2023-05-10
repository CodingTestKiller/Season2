from collections import defaultdict


def main():
    N, M = map(int, input().split())
    file_info = defaultdict(lambda: ([], []))

    for _ in range(N + M):
        parent, name, is_folder = input().split()
        is_folder = int(is_folder)

        if is_folder:
            file_info[parent][0].append(name)
        else:
            file_info[parent][1].append(name)

    Q = int(input())
    for _ in range(Q):
        query = input()

        if query not in file_info:
            print(0, 0)
        else:
            folder_files = file_info[query][1]
            unique_files = len(set(folder_files))
            total_files = len(folder_files)
            print(unique_files, total_files)


if __name__ == "__main__":
    main()

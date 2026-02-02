import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    document = {}

    for i in range(1, n + 1):
        parts = input_data[i].split()
        cmd = parts[0]
        key = parts[1]

        if cmd == "set":
            document[key] = parts[2]
        elif cmd == "get":
            if key in document:
                print(document[key])
            else:
                print(f"KE: no key {key} found in the document")

if __name__ == "__main__":
    solve()
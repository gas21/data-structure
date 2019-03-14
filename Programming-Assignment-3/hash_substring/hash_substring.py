# python3


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    hashes, patt, total, index, compare, sol = [], 0, 0, len(pattern), 0, []
    for i in text:
        hashes.append(hash(i) % 201251)
    for i in range(index):
        patt = (patt + hash(pattern[i])) % 201251
        compare = (compare + hash(text[i])) % 201251
    for i in range(len(text)-index):
        if compare == patt:
            if text[i:i+index] == pattern:
                sol.append(i)
        compare += hashes[i + index + 1]


    if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

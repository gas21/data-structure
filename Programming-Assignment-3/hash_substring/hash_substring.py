# python3


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    hashes, patt, total, index, compare, sol = [], 0, 0, len(pattern), 0, []
    for i in text:
        hashes.append(hash(i))
    for i in range(index):
        patt = patt + hash(pattern[i])
        compare = compare + hash(text[i])
    for i in range(len(text)-index+1):
        if compare == patt:
            if text[i:i+index] == pattern:
                sol.append(i)
        try:
            compare = compare + hashes[i + index]
            compare = compare - hashes[i]
        except IndexError:
            break
    return sol


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

# python3


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    hashes, pattern_hash, index, hash_compare, results = [], 0, len(pattern), 0, []
    for i in text:
        hashes.append(hash(i))
    for i in range(index):
        pattern_hash += hash(pattern[i])
        hash_compare += hash(text[i])
    for i in range(len(text)-index+1):
        if hash_compare == pattern_hash:
            if text[i:i+index] == pattern:
                results.append(i)
        try:
            hash_compare += hashes[i + index]
            hash_compare -= hashes[i]
        except IndexError:
            break
    return results


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

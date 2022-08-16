from dictionary import read_dictionary
from timer import timing


def all_concatenations_for_length(length, dictionary):
    wordset = {w for w in dictionary if len(w) < length}
    possible_targets = [w for w in dictionary if len(w) == length]

    for target in possible_targets:
        for prefix, suffix in _possible_splits(target):
            if prefix in wordset and suffix in wordset:
                yield (prefix, suffix, target)


def _possible_splits(word):
    return ((word[:i], word[i:])
            for i in range(1, len(word) - 1))


if __name__ == '__main__':
    d = read_dictionary()
    with timing():
        results = tuple(all_concatenations_for_length(6, d))
        print(len(results))

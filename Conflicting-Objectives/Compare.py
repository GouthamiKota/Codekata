import faster
import readable
from dictionary import read_dictionary
from timer import timing


def main():
    dictionary = read_dictionary()
    print('running faster:')
    with timing():
        faster_result = tuple(faster.all_concatenations_for_length(6, dictionary))
    print('running readable:')
    with timing():
        readable_result = tuple(readable.all_concatenations_for_length(6, dictionary))
    print('same results:', set(readable_result) == set(faster_result))


if __name__ == '__main__':
    main()

import sys
import gzip


def main(wordlist_path):
    """
    Finds anagrams by making use of the fact that if you
    sort the letters of two words in an anagram, then the
    sorted letters will be the same. The sorted letters are
    used as a key to a hashmap that keeps a list of words
    in the anagram.
    See: http://stackoverflow.com/questions/19600442/anagram-algorithm-using-a-hashtable-and-or-tries
    """

    anagrams = {}

    # load all the words into a dictonary keyed by a
    # set of the letters in the word.
    with gzip.open(wordlist_path) as wordlist:
        for word in wordlist:
            word = word.strip()
            key = "".join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

    num_anagrams = 0
    for _, wordlist in anagrams.iteritems():
        if len(wordlist) > 1:
            print(" ".join(wordlist))
            num_anagrams += 1
    print("-" * 20)
    print(num_anagrams)

if __name__ == '__main__':
    main(sys.argv[1])

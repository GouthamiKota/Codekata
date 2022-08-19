import sys
import gzip


def main(wordlist_path):
    

    anagrams = {}

    # Insert all  words into a dictonary keyed by a
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

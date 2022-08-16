import sys
import re
import urllib2
import string
import gzip
import bitarray
import hashlib


class BloomFilter(object):
    """
    Implements a simple bloom filter with the given size (m in the literature)
    and list of hash functions (h_k in the literature).
    """
    def __init__(self, size, hashers):
        self.size = size
        self.data = bitarray.bitarray(self.size)
        self.hashers = hashers

    def add(self, word):
        for hasher in self.hashers:
            self.data[self._hash_to_index(hasher, word)] = True

    def __contains__(self, item):
        return all(self.data[self._hash_to_index(hasher, item)] for hasher in self.hashers)

    def _hash_to_index(self, hasher, word):
        """
        Here we take a hexidecimal hash value and return an index into the
        binary array.
        There is a discussion on how to do this uniformly here using the hex
        representation of a hash.  This works well with the hashlib module in
        Python because it gives hex values.
        http://stats.stackexchange.com/questions/26344/how-to-uniformly-project-a-hash-to-a-fixed-number-of-buckets
        """

        # First we convert the first n hex characters into an integer.
        # We then mod that integer by the size of the array to get an index into the array.
        return int(hasher(word).hexdigest(), 16) % self.size

if __name__ == '__main__':
    dictionary = BloomFilter(500000, [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256])

    print("Loading dictionary...")
    i = 0
    with gzip.open(sys.argv[1]) as wordlist:
        for word in wordlist:
            dictionary.add(word.strip().lower())
    print("Done.")

    url = sys.argv[2]
    print("Reading Webpage: %s" % url)
    webpage_text = urllib2.urlopen(url).read()

    # Remove script and style tags.
    # This is a bit hackish and I'm not actually sure how these work.
    webpage_text = re.sub(r'<(script|style).*?</\1>(?s)', '', webpage_text,
                          flags=re.IGNORECASE | re.MULTILINE)

    # Remove html tags
    webpage_text = re.sub(r'<[^>]*?>', '', webpage_text)

    # Remove entities
    webpage_text = re.sub(r'&(([A-Za-z]+)|(#[0-9]+));', '', webpage_text)

    # Strip off punctuation and remove empty strings.
    def _wordfilter(w):
        # Ignore empty strings
        if not w:
            return False

        # Ignore numbers
        try:
            float(w)
            return False
        except ValueError:
            return True

    wordlist = filter(_wordfilter, (w.strip(string.punctuation) for w in webpage_text.split()))

    print("Done.")

    print

    print("Possibly misspelled words:")
    print("-" * 25)
    for word in wordlist:
        if word.lower() not in dictionary:
            print(word)

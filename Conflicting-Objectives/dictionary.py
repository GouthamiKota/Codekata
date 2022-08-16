def read_dictionary():
    with open('/usr/share/dict/american-english', encoding='utf8') as f:
        return [w.lower().strip() for w in f]

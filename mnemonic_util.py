from __future__ import with_statement
import collections

# Create 10-letter keys made up of every permutation of mnemonics
def create_key (lettersets, sofar) :
    if len(lettersets) == 0 :
        yield sofar
    else :
        letterset, leftover = lettersets[0], lettersets[1 :]
        for letter in letterset :
            for key in create_key(leftover, sofar + letter) :
                yield key
    return

# Create a defaultdict(list) from an iterator
def defaultdict(iter):
    d = collections.defaultdict(list)
    for key in iter:
        d["".join(sorted(key))].append(key)
    return d

def create_mnemonic_candidates():    
    mnemonics = [ "IM", "E", "SCN", "EGI", "CH", "E", "S", "T", "F", "T" ]
    return defaultdict(create_key(mnemonics, ""))

def create_word_candidates(word_len):
    if not (type(word_len) == list or type(word_len) == tuple):
        word_len = [ word_len ]
    filename = r'g:\words\words(3).txt'
    with open(filename) as f:
        candidates = [ str.strip().upper() for str in f.readlines() if len(str.strip()) in word_len]    
    return defaultdict(candidates)

# Create a defaultdict(int) from a string
def create_collections_dict(key):
    dk = collections.defaultdict(int)
    for k in key:
        dk[k] += 1
    return dk

# Score the similarity of a defaultdict(int) against a string (which is temporarily converted to a defaultdict(int))
def score(dk, cand) :
    dc = create_collections_dict(cand)
    return sum(min(dk[k], dc[k]) for k in dk.keys() if k in dc)

# Make a key composed of 'long_key' keys with all repeated occurrences of 'short_key' keys removed
def diff(long_key, short_key) :
    ld = create_collections_dict(long_key)
    sd = create_collections_dict(short_key)
    s = [ (k * (ld[k] - (sd[k] if k in sd else 0))) for k in ld.keys() ]
    return "".join(sorted(s))

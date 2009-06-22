from __future__ import with_statement
import collections

def create_key (lettersets, sofar) :
    if len(lettersets) == 0 :
        yield sofar
    else :
        letterset, leftover = lettersets[0], lettersets[1 :]
        for letter in letterset :
            for key in create_key(leftover, sofar + letter) :
                yield key
    return

def create_mnemonic_candidates():    
    mnemonics = [ "IM", "E", "SCN", "EGI", "CH", "E", "S", "T", "F", "T" ]
    d = collections.defaultdict(list)
    for key in create_key(mnemonics, ""):
        sorted_key = "".join(sorted(key))
        d[sorted_key].append(key)
    return d

def create_word_candidates(word_len):
    filename = r'g:\words\words(3).txt'
    with open(filename) as f:
        candidates = [ str.strip() for str in f.readlines() if len(str.strip()) == word_len]
    
    w = collections.defaultdict(list)
    for c in candidates:
        key = c.upper()
        sorted_key = "".join(sorted(key))
        w[sorted_key].append(key)
    return w

def create_word_candidates2(word_lens):
    filename = r'g:\words\words(3).txt'
    with open(filename) as f:
        candidates = [ str.strip() for str in f.readlines() if len(str.strip()) in word_lens]
    
    w = collections.defaultdict(list)
    for c in candidates:
        key = c.upper()
        sorted_key = "".join(sorted(key))
        w[sorted_key].append(key)
    return w

def create_collections_dict(key):
    dk = collections.defaultdict(int)
    for k in key:
        dk[k] += 1
    return dk

def score(dk, cand) :
    dc = create_collections_dict(cand)
    return sum(min(dk[k], dc[k]) for k in dk.keys() if k in dc)
    
def diff(long_key, short_key) :
    ld = create_collections_dict(long_key)
    sd = create_collections_dict(short_key)
    s = [ (k * (ld[k] - (sd[k] if k in sd else 0))) for k in ld.keys() ]
    return "".join(sorted(s))


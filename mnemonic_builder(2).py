from __future__ import with_statement
import collections

FIRST_FIT = 5
SECOND_FIT = 10 - FIRST_FIT

def create_key (lettersets, sofar) :
    if len(lettersets) == 0 :
        yield sofar
    else :
        letterset, leftover = lettersets[0], lettersets[1 :]
        for letter in letterset :
            for key in create_key(leftover, sofar + letter) :
                yield key
    return

def create_word_candidates():
    filename = r'g:\words\words(3).txt'
    with open(filename) as f:
        candidates = [ str.strip() for str in f.readlines() if len(str.strip()) in (FIRST_FIT, SECOND_FIT)]
    
    w = collections.defaultdict(list)
    for c in candidates:
        key = c.upper()
        sorted_key = "".join(sorted(key))
        w[sorted_key].append(key)
    return w

def create_mnemonic_candidates():    
    mnemonics = [ "IM", "E", "SCN", "EGI", "CH", "E", "S", "T", "F", "T" ]
    d = collections.defaultdict(list)
    for key in create_key(mnemonics, ""):
        sorted_key = "".join(sorted(key))
        d[sorted_key].append(key)
    return d

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

if __name__ == "__main__" :
    d = create_mnemonic_candidates()
    w = create_word_candidates()
    
    for k in d.keys() :
        dk = create_collections_dict(k)
        sk = set(k)
        for kk in w.keys():
            x = score(dk, kk)
            if x == FIRST_FIT :
                kk2 = diff(k, kk)
                #if kk2 in w and (kk < kk2) :
                if kk2 in w and score(dk, kk2) == SECOND_FIT :
                    print k, kk, kk2, w[kk], w[kk2]

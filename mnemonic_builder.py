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

def create_word_candidates():
    filename = r'g:\words\words(3).txt'
    with open(filename) as f:
        candidates = [ str.strip() for str in f.readlines() if len(str) == 11]
    
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
    
d = create_mnemonic_candidates()
w = create_word_candidates()

for k in d.keys() :
    dk = create_collections_dict(k)
    max_score = -1
    match = None
    for kk in w.keys():
        x = score(dk, kk)
        if x > max_score :
            max_score, match = x, [ kk ]
        elif x == max_score:
            match.append(kk)
    if max_score >= 9:
        print k, d[k], max_score
        for m in sorted(match):
            print "\t", m, w[m]

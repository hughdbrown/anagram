try:
    import psyco
    psyco.full()
except ImportError:
    pass

from mnemonic_util import *

if __name__ == "__main__" :
    FIRST_FIT = 5
    SECOND_FIT = 10 - FIRST_FIT
    wordlens = (FIRST_FIT, SECOND_FIT)
    d = create_mnemonic_candidates()
    w = create_word_candidates(wordlens)
    
    for k in d.keys() :
        dk = create_collections_dict(k)
        sk = set(k)
        for kk in w.keys():
            x = score(dk, kk)
            if x == FIRST_FIT :
                kk2 = diff(k, kk)
                if kk2 in w and score(dk, kk2) == SECOND_FIT :
                    print k, kk, kk2, w[kk], w[kk2]

try:
    import psyco
    psyco.full()
except ImportError:
    pass

from mnemonic_util import *

if __name__ == "__main__" :
    d = create_mnemonic_candidates()
    w = create_word_candidates(7)
    the = sorted("THE")
    for k in d.keys() :
        dk = create_collections_dict(k)
        if score(dk, the) == 3:
            k2 = diff(k, the)
            if k2 in w.keys() :
                print d[k], k, k2, "THE", w[k2]

from mnemonic_util import *

if __name__ == "__main__" :
    d = create_mnemonic_candidates()
    w = create_word_candidates(10)
    
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

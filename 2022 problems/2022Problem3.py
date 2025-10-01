#!/usr/bin/env python3
# Problem 3 — Football Scores
# Count number of combinations to reach total using {2,3,6,7,8} (order doesn't matter)
# Also print combination with the fewest scoring plays (and lexicographically smallest among ties)

import sys

SCORES = [2,3,6,7,8]

from functools import lru_cache

@lru_cache(None)
def ways(total, max_score_index):
    # count combinations (non-decreasing scores by index up to max_score_index)
    if total == 0:
        return 1
    if total < 0 or max_score_index < 0:
        return 0
    # include at least 0 of SCORES[max_score_index]
    return ways(total, max_score_index-1) + ways(total - SCORES[max_score_index], max_score_index)


def find_min_combo(total):
    # dynamic programming to find the combo (multiset) with minimal number of plays
    # dp[t] = (min_num_plays, combo_list_as_counts)
    INF = 10**9
    maxT = total
    # dp_num[t] minimal plays, dp_choice[t] last score used index
    dp_num = [INF] * (maxT+1)
    dp_choice = [-1] * (maxT+1)
    dp_num[0] = 0
    # dp_num[t] = minimal number of plays to reach t
    # dp_combo[t] = lexicographically smallest tuple (sorted ascending) achieving dp_num[t]
    dp_combo = [None] * (maxT+1)
    dp_num[0] = 0
    dp_combo[0] = tuple()
    for s in sorted(SCORES):
        for t in range(s, maxT+1):
            if dp_num[t-s] >= INF:
                continue
            cand_num = dp_num[t-s] + 1
            # candidate combo: merge dp_combo[t-s] with s and keep sorted tuple
            prev = dp_combo[t-s]
            cand_combo = tuple(sorted(prev + (s,)))
            if cand_num < dp_num[t]:
                dp_num[t] = cand_num
                dp_combo[t] = cand_combo
            elif cand_num == dp_num[t]:
                # tie: choose lexicographically smaller multiset
                if dp_combo[t] is None or cand_combo < dp_combo[t]:
                    dp_combo[t] = cand_combo
    if dp_num[total] >= INF:
        return None
    return list(dp_combo[total])


def main():
    out_lines = []
    for line in sys.stdin:
        line=line.strip()
        if line=="":
            continue
        n = int(line)
        if n<0:
            break
        w = ways(n, len(SCORES)-1)
        if w == 0:
            out_lines.append("0")
        else:
            combo = find_min_combo(n)
            if combo is None:
                out_lines.append(str(w))
            else:
                out_lines.append(str(w) + " {" + ",".join(str(x) for x in combo) + "}")
    sys.stdout.write("\n".join(out_lines))

if __name__=='__main__':
    main()

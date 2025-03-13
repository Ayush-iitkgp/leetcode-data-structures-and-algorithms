from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser_count = {}
        for m in matches:
            if m[0] not in looser_count:
                looser_count[m[0]] = 0
            looser_count[m[1]] = looser_count.get(m[1], 0) + 1
        # print(looser_count)
        all_winner = []
        one_looser = []
        for p in looser_count:
            if looser_count[p] == 0:
                all_winner.append(p)
            elif looser_count[p] == 1:
                one_looser.append(p)
        return [sorted(all_winner), sorted(one_looser)]

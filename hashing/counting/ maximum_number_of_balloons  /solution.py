class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Step 1: Create a count with frequency of letters in the input text
        Step 2: The number of instances of "balloon" in the input is len(input)//7
        Step 3: Iterate until the maximum instances and find if letters in balloon are present in the count.
        Step 4: If all the letters are present then increment the ans by 1. If one of the letters is not present,
        return the ans
        """
        maximum = len(text) // 7
        print(maximum)
        count = {}
        for t in text:
            count[t] = count.get(t, 0) + 1

        i = 1
        ans = 0
        while i <= maximum:
            for x in "balloon":
                if x not in count or count[x] <= 0:
                    # print(f"returning here {x}")
                    # print(count)
                    return ans
                else:
                    count[x] -= 1
            ans += 1
            # print(ans)

        # print(count)
        return ans

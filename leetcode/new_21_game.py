"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.



Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
"""

class Solution:
    def new21Game(self, N, K, maxPts):
        # Corner cases
        if K == 0:
            return 1.0
        if N >= K - 1 + maxPts:
            return 1.0

        # dp[i] is the probability of getting point i.
        dp = [0.0] * (N + 1)

        probability = 0.0  # dp of N or less points.
        windowSum = 1.0  # Sliding required window sum
        dp[0] = 1.0
        for i in range(1, N + 1):
            dp[i] = windowSum / maxPts

            if i < K:
                windowSum += dp[i]
            else:
                probability += dp[i]

            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        return probability
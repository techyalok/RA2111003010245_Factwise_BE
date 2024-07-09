#Q7
def maxScore(cardPoints, k):
    n = len(cardPoints)

    window_sum = sum(cardPoints[:k])
    max_score = window_sum

    for i in range(k):
        window_sum = window_sum - cardPoints[k - i - 1] + cardPoints[n - i - 1]
        max_score = max(max_score, window_sum)

    return max_score

cardPoints = list(map(int, input().split()))
k = int(input())

result = maxScore(cardPoints, k)
print(result)

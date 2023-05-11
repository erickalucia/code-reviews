def two_sum(number, t):
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[j] == t - number[i]:
                return [i, j]

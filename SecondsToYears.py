n = int(input())
times = [60, 3600, 86400, 604800, 2592000, 31536000]
word = ["minute", "hour", "day", "week", "month", "year"]
words = ["minutes", "hours", "days", "weeks", "months", "years"]
i = 5
for i in reversed(range(0, 5)):
    current = n // times[i]
    if current != 0:
        if current == 1:
            print(current, word[i])
        else:
            print(current, words[i])
    n -= current * times[i]
print(n, "seconds")

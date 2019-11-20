import re


def search(regex, text):
    if re.search(regex, text):
        print("{} is valid".format(text))
    else:
        print("{} is invalid".format(text))


def slowestKey(times):
    max_time = times[0][1]
    ind = times[0][0]
    prev = 0

    for i in range(len(times)):
        prev = times[i][1] - prev
        if prev > max_time:
            max_time = prev
            ind = times[i][0]

    return chr(ind+97)

if __name__ == "__main__":
    regex = "^[a-z]{1,6}[_]?\d{0,4}@hackerrank.com$"
    search(regex, "hello_123@hackerrank.com")
    search(regex, "_123@hackerrank.com")
    search(regex, "@hackerrank.com")
    search(regex, "julia@gmail.com")

    print(slowestKey([[0, 2], [1, 5], [0, 9], [2, 15]]))
    print(slowestKey([[0, 1], [0, 3], [4, 5], [5, 6], [4, 10] ]))
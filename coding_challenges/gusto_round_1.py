def compressedString(message):
    output = ""
    prev = message[0]
    count = 1
    for i in range(1, len(message)):
        if prev != message[i]:
            output += prev
            if count > 1:
                output += str(count)
            prev = message[i]
            count = 1
        elif prev == message[i]:
            count += 1

    output += prev
    if count > 1:
        output += str(count)

    return output


def usernamesSystem(u):
    usernames = set()
    return_usernames = []

    for username in u:
        if username not in usernames:
            usernames.add(username)
            return_usernames.append(username)
        elif username in usernames:
            og = username
            count = 1
            username += str(count)
            while username in usernames:
                count += 1
                username = og + str(count)
            usernames.add(username)
            return_usernames.append(username)

    return return_usernames


def rec(a, b, c, d):
    if a == c and b == d:
        return True
    if c < a or d < b:
        return False
    return rec(a, a+b, c, d) or rec(a+b, b, c, d)


def isPossible(a, b, c, d):
    if rec(a, b, c, d):
        return "Yes"
    return "No"


if __name__ == "__main__":
    print(compressedString("abc")) # abc
    print(compressedString("alaasass")) # ala2sas2

    print(usernamesSystem(['bob', 'alice', 'bob', 'alice']))

    print(isPossible(1, 4, 5, 9))
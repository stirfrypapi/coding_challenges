

def get_string_encode(letter):
    if ord(letter) >= ord('a') and ord(letter) <= ord('i'):
        return str(ord(letter) - 96)
    return str(ord(letter) - 96) + '#'

def frequency(s):
    count = {}
    answer = ""

    for char in s:
        if char not in count:
            count[char] = 1
            answer += get_string_encode(char)
        else:
            answer += "({})".format(get_string_encode(char))

    return answer

if __name__ == "__main__":
    print(frequency())
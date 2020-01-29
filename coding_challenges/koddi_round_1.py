
def sum_digits(num):
    sum = 0

    while num:
        digit = num % 10
        num = int(num / 10)
        sum += digit

    return sum


def get_sum_digits(arr):
    ans = [sum_digits(ticket) for ticket in arr]
    return ans


def lotteryCoupons(n):
    ticket_nums = [i for i in range(1, n+1)]
    sum_ticket_num = get_sum_digits(ticket_nums)

    counts = [0 for i in range(0, n+1)]
    for sum in sum_ticket_num:
        counts[sum] += 1

    max_sum = max(counts)

    ans = 0
    for i in range(1, n+1):
        if counts[i] == max_sum:
            ans += 1

    return ans



if __name__ == "__main__":
    print(get_sum_digits([123, 1, 2, 3, 900]))
    print(lotteryCoupons(3))
    print(lotteryCoupons(11))
    print(lotteryCoupons(22))

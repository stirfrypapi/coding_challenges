VALID_COINS = [1, 5, 10, 25]
input_coins = '25, 25, 25, 5, 5, 25, 25, 25, 5, 1, 10, 10, 5, 25, 1, 5'
RIDE_PRICE = 75

'''
Output as many fares as possible and the optimal change
input: a total of 160 cents
output:
OPEN
OPEN
[10]

160 % 75 = 10 -> calculate_change(10)
floor(160 / 75) = floor(2.xx) = 2
'''


def calculate_change(VALID_COINS, amount):
    """
    use a greedy algorithm to calculate coins
    amount: 80
    [25, 25, 25, 5]


    """
    ans_coins = []  # []

    coin_index = len(VALID_COINS) - 1  # 2
    while amount > 0:  # 5
        if amount - VALID_COINS[coin_index] >= 0:  # 5 - 5 = 0
            # use the coin
            ans_coins.append(VALID_COINS[coin_index])  # [25, 25, 25, 5]

            # update the remaining amount
            amount -= VALID_COINS[coin_index]  # 0
        else:
            # decremend the index
            coin_index -= 1  # 1

    return ans_coins


def coin_changes(VALID_COINS, input_coins, ride_price):
    """
    process the string, [25, 25, 25, 5 ,5 ...]

    calculate total_change

    if total_change >= 75: open the gate and calculate change. print open
    else: close the gate

    time complexity:
    if user has N input coins, O(N)
    if there are M valid coins, calculate change is O(M)
    O(N + M)

    space complexity:
    O(N)
    """

    # split user coins into a list
    user_coins = input_coins.split(",")

    # calculate total change
    total_change = 0
    for coin in user_coins:
        total_change += int(coin)

    num_tickets = int(int(total_change) / int(ride_price))  # 2
    change = total_change % ride_price
    # check to open or close
    for i in range(0, num_tickets):  # 0, 1
        print("OPEN")
    if change > 0:
        print(calculate_change(VALID_COINS, change))

    return


if __name__ == "__main__":
    coin_changes(VALID_COINS, '25, 25, 25, 25, 25, 25, 10', 75)





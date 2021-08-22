def get_num_distinct_chars(string):
    """Returns the number of distinct characters in string."""
    chars_in_string = set()
    num_distinct_chars = 0
    for char in string:
        if char not in chars_in_string:
            num_distinct_chars += 1
            chars_in_string.add(char)
    return num_distinct_chars

def get_all_substrings(string):
    """Return array of all substrings."""
    arr = []
    left = 0
    right = 1

    while left < len(string):
        while right <= len(string):
            if right == len(string):
                arr.append(string[left:])
            else:
                arr.append(string[left:right])
            right += 1
        left += 1
        right = left + 1
    return arr

def countKDistinctSubstrings(inputString, num):
    """Return number of substrings with K distinct chars"""
    count = 0
    substrings = get_all_substrings(inputString)

    for substring in substrings:
        if get_num_distinct_chars(substring) == num:
            count += 1
    return count

# question2
import heapq
def highestProfit(numSuppliers, inventory, order):
    """Greedy algorithm to maximize profits."""

    inventory_dict = {}
    max_price = 0
    profit = 0

    # create dictionary of each supplier's highest price to count
    for i in range(len(inventory)):
        item = inventory[i]
        max_price = max(item, max_price)

        if item in inventory_dict:
            inventory_dict[item] += 1
        else:
            inventory_dict[item] = 1

    while order > 0:
        # get inventory amount at highest price
        freq = inventory_dict[max_price]

        # satisfy all orders at max_price
        if order > freq:
            # all freq is sold at max price
            # update profit
            profit += freq * max_price
            # update remaining orders to fulfill
            order -= freq
            # delete from inventory
            del inventory_dict[max_price]

            # re insert updated inventory amounts
            if max_price - 1 in inventory_dict:
                inventory_dict[max_price-1] += freq
            else:
                inventory_dict[max_price-1] = freq
            max_price -= 1
        else:
            # only satisfy amount of orders left
            profit += order * max_price
            order = 0
    return profit


    # time limit exceed
    # """Greedy algorithm to maximize profits."""
    # satisfied_orders = 0
    #
    # # create heap with largest absolute value on top
    # inventory_heap = [val * -1 for val in inventory]
    # heapq.heapify(inventory_heap)
    # profit = 0
    #
    # while satisfied_orders != order and inventory_heap != []:
    #     max_val = heapq.heappop(inventory_heap) * -1
    #
    #     # update current profit
    #     profit += max_val
    #
    #     # no need to push new value if the inventory is at 1
    #     if max_val != 1:
    #         # need to update the heap with one less inventory
    #         # but dont forget to push a negative value
    #         heapq.heappush(inventory_heap, (max_val - 1) * -1)
    #
    #     # update satisfied_orders
    #     satisfied_orders += 1
    # return profit

    # time limit exceed
    # num_orders = order
    # satisfied_orders = 0
    # profit = 0
    #
    # while satisfied_orders != num_orders or sum(inventory) == 0:
    #
    #     # find highest price
    #     highest_price = max(inventory)
    #
    #     # get supplier index for highest price
    #     highest_price_index = inventory.index(highest_price)
    #
    #     # add to running profit
    #     profit += highest_price
    #
    #     # subtract from inventory
    #     inventory[highest_price_index] -= 1
    #
    #     # update satisfied orders
    #     satisfied_orders += 1
    #
    # return profit


if __name__ == "__main__":
    print(highestProfit(2, [3, 5], 6)) # 19
    print(highestProfit(2, [2, 5], 4)) # 14
    print(highestProfit(5, [2, 8, 4, 10, 6], 20)) # 110
    print(highestProfit(5, [3, 5, 7, 10, 6], 20)) # 107
    print(highestProfit(2, [3, 4], 6)) # 15
    print(countKDistinctSubstrings("pqpqs", 2))
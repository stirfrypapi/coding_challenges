class Event(object):
    def __init__(self, l):
        self.event_id = l[0]
        self.event_loc = l[1:3]
        self.event_prices = l[3:]
        self.event_prices.sort()


class Buyer(object):
    def __init__(self, l, id):
        self.buyer_id = id
        self.buyer_loc = l[0:]


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def distance_to_all_events(events, buyer):
    """
    :param events: List of Event
    :param buyer: One Buyer
    :return: List[lists] of [distance, event_id]
    """
    x_loc, y_loc = buyer.buyer_loc[0], buyer.buyer_loc[1]
    d = []
    for e in events:
        dist = manhattan_distance(x_loc, y_loc, e.event_loc[0], e.event_loc[1])
        d.append([dist, e.event_id])
    d.sort()
    return d


def closest_events(distance_to_all_events):
    """
    :param distance_to_all_events: List[lists] from distance_to_all_events()
    :return: List[lists] with only the closest event(s) (may be ties)
    """
    shortest_distance = distance_to_all_events[0][0]
    keepers = []
    for d in distance_to_all_events:
        if d[0] == shortest_distance:
            keepers.append(d)
    return keepers


def delete_price(events, event_ind):
    events[event_ind].event_prices.pop(0)
    if len(events[event_ind].event_prices) == 0:
        del events[event_ind]


def get_tickets_to_fans(events, buyers):
    """
        events -> List[list] of all events.
            Example: events[0] = [1, 1, 1, 40, 60]
                events[0][0] -> event id
                events[0][1:3] -> [x, y] coordinate of event
                events[0][2:] -> [40, 60] prices of tickets for that event
        buyers -> List[list] of all buyers.
            Example: buyers[0] = [3, 3] -> [x, y] coordinate of buyer 0

        for each buyer_id:
            d = {find distance to all events} key=distance, value=event_id
            d_closest = {closest distances}
            if d_closest has one key:
                print(buyer_id, price of the cheapest ticket)
                delete(e_id, price)
            else:
                event_ids = [event_ids of d_closest values]
                min = events[event_ids[0]].event_prices[0]
                for e_id in event_ids:
                    if events[event_ids[e_id]].event_prices[0] < min:
                        set the new min
                print(buyer_id, min)
                delete(e_id, price)
    """
    if len(events) == 0 or len(buyers) == 0:
        return
    events_objs = []
    for e in events:
        events_objs.append(Event(e))

    buyers_objs = []
    for b in range(len(buyers)):
        buyers_objs.append(Buyer(buyers[b], b+1))

    for b in buyers_objs:
        d_closest = closest_events(distance_to_all_events(events_objs, b))
        # [[distance, event_id]]
        if len(d_closest) == 1:
            e_ind = d_closest[0][1] - 1
            print("{} {}".format(events_objs[e_ind].event_id,
                                 events_objs[e_ind].event_prices[0]))
            delete_price(events_objs, e_ind)
        else:
            min_e_ind = d_closest[0][1] - 1
            min = events_objs[min_e_ind].event_prices[0]
            for inner in d_closest:
                e_ind = inner[1] - 1
                price = events_objs[e_ind].event_prices[0]
                if price < min:
                    min = price
                    min_e_ind = e_ind
            print("{} {}".format(events_objs[min_e_ind].event_id, min))
            delete_price(events_objs, min_e_ind)


if __name__ == "__main__":
    get_tickets_to_fans([[1, 1, 1, 40, 60], [2, 1, 4, 50]],
                        [[3, 3], [3, 2], [4, 3]])
    # 2 50
    # 1 40
    # 1 60
def join_phrases(start_phrases, end_phrases):
    res = []
    for end_phrase in end_phrases:
        for start_phrase in start_phrases:
            if end_phrase != start_phrase:
                join_phrase = end_phrase.split()[:]
                join_phrase.extend(start_phrase.split()[1:])
                res.append(" ".join(join_phrase))
    return res


def generate_phrases(phrases):
    """Combine 2 phrases if phrase 1 has the same ending word that phrase 2 has
    beginning word."""

    # preprocess
    words = {}
    for phrase in phrases:
        start_word, end_word = phrase.split()[0], phrase.split()[-1]
        if start_word not in words:
            words[start_word] = [set(), set()]
            words[start_word][0].add(phrase)
        else:
            words[start_word][0].add(phrase)
        if end_word not in words:
            words[end_word] = [set(), set()]
            words[end_word][1].add(phrase)
        else:
            words[end_word][1].add(phrase)

    res = []
    for word in words:
        start_phrases = words[word][0]
        end_phrases = words[word][1]
        res.extend(join_phrases(start_phrases, end_phrases))

    return res


class Node(object):
    def __init__(self, task, to, parents):
        self.task = task
        self.to = to
        self.parents = parents


def is_blocked(required_tasks, task_from, task_to):
    """Is there a path that goes through all nodes in required_tasks following
    the graph from task_from and task_to?"""

    required_tasks = set(required_tasks)

    all_nodes = {}

    for i in range(len(task_from)):
        if task_from[i] not in all_nodes:
            n = Node(task_from[i], [task_to[i]], [])
            all_nodes[task_from[i]] = n
        else:
            all_nodes[task_from[i]].to.append(task_to[i])
        if task_to[i] not in all_nodes:
            n = Node(task_to[i], [], [task_from[i]])
            all_nodes[task_to[i]] = n
        else:
            all_nodes[task_to[i]].parents.append(task_from[i])

    roots = []
    for task in all_nodes:
        if all_nodes[task].parents == []:
            roots.append(task)

    visited = set()

    queue = roots

    while queue:
        curr_node = all_nodes[queue.pop(0)]

        possible = True
        for parent in curr_node.parents:
            if parent not in visited and parent in required_tasks:
                possible = False

        if possible and curr_node.task in required_tasks:
            required_tasks.remove(curr_node.task)
            if len(required_tasks) == 0:
                return False
            visited.add(curr_node.task)
        if curr_node.task in visited:
            for to in curr_node.to:
                queue.append(to)

    return True




if __name__ == "__main__":
    # print(generate_phrases(["writing code", "code rocks"]))
    # print(generate_phrases(["a b a ", "a c"]))
    # print(generate_phrases([
    #     "mission statement",
    #     "a quick bite to eat",
    #     "a chip off the old block",
    #     "chocolate bar",
    #     "mission impossible",
    #     "a man on a mission",
    #     "block party",
    #     "eat my words",
    #     "bar of soap"
    # ]))
    #

    print(is_blocked(["get gas", "drive", "load materials", "exit"],
                     ["get gas", "drive", "load materials", "exit"],
                     ["drive", "exit", "exit", "load materials"]))  # expected True

    print(is_blocked(["get gas", "drive", "exit"],
                     ["get gas", "drive", "load materials", "exit"],
                     ["drive", "exit", "exit", "load materials"])) # expected False

    print(is_blocked(["get gas", "drive", "load materials", "exit"],
                     ["get gas", "drive", "load materials"],
                     ["drive", "exit", "exit"])) # expected False

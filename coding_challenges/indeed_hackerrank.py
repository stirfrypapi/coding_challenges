import heapq


def store_description(description, document_number):
    """
    Returns a set of words of the job description.
    """
    # print("store desc " + description + " doc num " + str(document_number))
    return set(description.split(" "))


def perform_search(jobs, search):
    """
    Returns the id of matching jobs.
    The jobs with highest match count are returned first.
    In case of a tie, the lowest job id is returned first.
    """

    matched_job_ids = ""

    # dictionary where keys are match counts
    # and values are a list of job ids in ascending order
    match_count_dict = {}

    # array of match counts
    match_count_arr = []
    # heapq.heapify(match_count_arr)

    for i in range(0, len(jobs)):
        description_set = jobs[i]
        search_set = set(search.split(" "))
        match_count = 0
        for word in search_set:
            if word in description_set:
                match_count += 1
        if match_count > 0:
            if match_count in match_count_dict:
                match_count_dict[match_count].append(i)
            elif match_count not in match_count_dict:
                match_count_dict[match_count] = [i]
                # use -1 so we can sort in ascending order
                match_count_arr.append(-1 * match_count)

    if len(match_count_arr) == 0:
        return -1

    # only need to consider top 10 matches
    match_count_arr = match_count_arr[0:10]
    match_count_arr.sort()
    num_job_matches = 0

    for num in match_count_arr:
        match_count = -1 * num
        for job_id in match_count_dict[match_count]:
            matched_job_ids += str(job_id) + " "
            num_job_matches += 1
            if num_job_matches == 10:
                # if we reach 10 job matches, return
                break

    return matched_job_ids


N = int(input())
# array of sets. each set is a job description. the index is the job id
jobs = []
for i in range(N):
    jobs.append(store_description("0 4 8 9 10 15 17 19 20 24", i))

M = int(input())
for _ in range(M):
    print(perform_search(jobs, input()))
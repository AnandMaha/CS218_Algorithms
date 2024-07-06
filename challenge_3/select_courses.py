def find_max_credits(n, m, courses):
    max_credits = 0
    stack = [(1, set(), 0)] # start with course 1, seen courses, and credit amount  

    while stack: # DFS to find optimal credit amount from subset of courses
        course, seen_courses, credits = stack.pop()
        if len(seen_courses) == m:  # max courses used up in this path
            max_credits = max(max_credits, credits)
            continue # pop next node from stack now
        for i in range(1, n + 1): # loop through each course
            if i not in seen_courses and (courses[i][0] == 0 or courses[i][0] in seen_courses): # no pre-req or pre-req met!
                stack.append((i + 1, seen_courses | {i}, credits + courses[i][1]))
    return max_credits # optimal answer from DFS found

n, m = map(int, input().split())
courses = [(0, 0)] # no pre-req class
for _ in range(n):
    pre_req, credits = map(int, input().split())
    courses.append((pre_req, credits))
print(find_max_credits(n, m, courses))

import bisect

def students_office_hour(n, m, free_days, student_free_days):
    student_cnt = 0
    free_days.sort()
    student_free_days.sort(key=lambda x: x[1])
    
    for begin, end in student_free_days:
        index = bisect.bisect_left(free_days, begin) # find free day at or after begin
        
        if index < len(free_days) and free_days[index] <= end:
            student_cnt += 1
            del free_days[index]  # don't let another student use the day

    return student_cnt

n, m = map(int, input().split())
free_days = [int(input()) for _ in range(n)]
student_free_days = [tuple(map(int, input().split())) for _ in range(m)]
print(students_office_hour(n, m, free_days, student_free_days))

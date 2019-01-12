if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    print ("%.2f" %(round(float(sum(student_marks[query_name]))/float(len(student_marks[query_name])),2)))

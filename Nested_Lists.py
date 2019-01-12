N = int(raw_input())
nested_list = []
for i in range(N):
    name = str(raw_input())
    score = float(raw_input())
    nested_list.append([name,score])
marks = []
for i in range(N):
    marks.append(nested_list[i][1])
marks = list(set(marks))
marks.sort()
second_lowest = marks[1]
name_list = []
for i in range(N):
    if(nested_list[i][1] == second_lowest):
        name_list.append(nested_list[i][0])
name_list.sort()
print "\n".join(name_list)

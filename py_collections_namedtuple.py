
from collections import namedtuple
n = int(input())
names = input().split()
Student = namedtuple('Student', names)
marks_list = [int(Student._make(input().split()).MARKS) for i in range(n)]
print('%.2f'%(sum(marks_list) / len(marks_list)))
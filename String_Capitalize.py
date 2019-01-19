import os
# Complete the solve function below.
def solve(s):
    splitted_s = s.split(" ")
    return (" ".join(i.capitalize() for i in splitted_s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

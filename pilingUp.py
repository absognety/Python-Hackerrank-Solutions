# Enter your code here. Read input from STDIN. Print output to STDOUT
def Piling_Up(sides):
    sidesLength = len(sides)
    forward_inds = range(sidesLength)
    backward_inds = range(-1,-1*sidesLength,-1)
    pile_decision_maker = []
    if sidesLength%2 == 0:
        for I,J in list(zip(forward_inds,backward_inds))[:(sidesLength//2)]:
            if sides[I]>=sides[J]:
                pile_decision_maker.append('TRUE')
            else:
                pile_decision_maker.append('FALSE')
        if 'TRUE' in pile_decision_maker and 'FALSE' not in pile_decision_maker:
            return ('Yes')
        else:
            return ('No')
    else:
        for I,J in zip(forward_inds,backward_inds):
            if sides[I]>=sides[J]:
                pile_decision_maker.append('TRUE')
            else:
                pile_decision_maker.append('FALSE')
        if 'TRUE' in pile_decision_maker and 'FALSE' not in pile_decision_maker:
            return ('Yes')
        else:
            return ('No')
        
        
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n = int(input())
        sideLengths = list(map(int,input().strip().split()))
        print (Piling_Up(sideLengths))
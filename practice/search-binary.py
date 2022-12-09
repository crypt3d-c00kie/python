#searching
#binary search

def binary_search(target, given_list):
    low = 0
    high = len(given_list)-1
    flag = False

    while low <= high:
        mid = int(low + (high-low)/2)
        # mid = (low+high)/2
        if given_list[mid] == target:
            print(f'Target found at {mid}')
            flag = True
            break
        elif given_list[mid] < target:
            low = mid + 1
        elif given_list[mid] > target:
            high = mid - 1
    
    if flag == False:
        print(f'The given key {target} is not found')

    
def main():
    n = int(input('Size :: '))
    given = []
    given = list(map(int,input('Given :: ').strip().split()))[:n]

    k = int(input('Target :: '))
    binary_search(k, given)


main()
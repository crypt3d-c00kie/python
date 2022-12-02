def runningSum(nums):
    runsum = 0
    solution = []
    for i in nums:
        runsum += i
        solution.append(runsum)
    
    return solution

def main():
    givenList = []
    size = int(input("Number of Elements : "))

    for i in range(0,size):
        val = int(input('Given : '))
        givenList.append(val)

    print(f"Running sum of this 1D array :: {runningSum(givenList)}")

main()
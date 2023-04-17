# rotate the array by n
# direction - left

def main():
    given = [1,2,4,5,6]
    kIter = [1,2,3,5]

    # for k in kIter:
    #     given[:] = given[k:] + given[:k] 
    #     print(given)

    
    for k in kIter:
        for i in range(k):
            given.append(given[0])
            del given[0]
        
        print(given)


if __name__ == '__main__':
    main()

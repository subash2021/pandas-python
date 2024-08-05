"""
A format for expressing an ordered list of integers is to use a comma separated list of either

- individual integers
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
  Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

"""
def solution(args):
    serializeList = [args[0]]
    prevNum = args[0]
    returningString = ''

    print(f"Initial serializeList: {serializeList}" )


    for num in args[1:]:
        if num-1 == prevNum:
            serializeList.append(num)
            print(f"Adding serial num in the list : {serializeList}")
        else:
            """print("First else entry:")
            print(f"num value: {num}" )
            print(f"Printing the list during first time else entry : {serializeList}")"""
            print("Entering else condition:")
            if len(serializeList)>=3:
                print("serial list len is greater than 3")
                returningString = returningString + str(serializeList[0]) + '-' + str(serializeList[-1]) + ','
            else:
                print("Serial list len is less than 3")
                for x in serializeList:
                    returningString = returningString + str(x) + ','
                # Reset list
            serializeList = [num]
        prevNum = num
        
    if len(serializeList)>=3:
        print("serial list len is greater than 3")
        returningString = returningString + str(serializeList[0]) + '-' + str(serializeList[-1]) + ','
    else:
        print("Adding to the string one at a")
        for x in serializeList:
            returningString = returningString + str(x) + ','
    finalString = returningString
    return finalString

testArray = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
printReturn = solution(testArray)[:-1]
print(f"The final returning string is: \n{printReturn}")

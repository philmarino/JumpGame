def jump(list):
    return jumpIterator(list, [0])

def jumpIterator(list, startingPoints):
    #print("looking at " + str(startingPoints))
    for startingPoint in startingPoints:
        newStartingPoints = []
        if startingPoint + list[startingPoint] >= len(list):
            print("jump from " + str(startingPoint) + " to the end.")
            return True #we can get from this starting point to the end of the list
        else:
            #create a list of new starting points in the list we can get to from this starting point
            for offset in range(1, list[startingPoint]+1):
                if startingPoint+offset < len(list):
                    if not startingPoint+offset in newStartingPoints:
                        newStartingPoints.append(startingPoint+offset)

            if len(newStartingPoints) > 0:
                #can we get to the end from any of these new starting points
                if jumpIterator(list, newStartingPoints):
                    print("jump from " + str(startingPoint))
                    return True

    return False #would have returned True above it it were

#Example 1:
#Input: 
nums = [2,3,1,1,4]
print(jump(nums))
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

#Example 2:
#Input: 
nums = [3,2,1,0,4]
print(jump(nums))
#Output: false
#Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

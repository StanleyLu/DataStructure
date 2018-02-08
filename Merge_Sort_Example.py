import time
import math

import random

insertArray = []
s = 0
while s < 9:
	tempRandNum = random.randint(0,100)
	insertArray.append(tempRandNum)
	s = s + 1 

# insertArray = [5,6,8,4,2,9,3,7,1]
# insertArray = [5,6,8,4,4,2,3,9,3,7,1]
# insertArray = [5,1,4,2,8]
print(insertArray)
# sortedList = []
def mergeList(leftList, rightList):

	if len(leftList) == 0:  
		return rightList  
	elif len(rightList) == 0:  
		return leftList  
	elif leftList[0] < rightList[0]:
		# print("leftList = " + str(leftList))
		# print("rightList = " + str(rightList))
		# print("leftList : " + str(leftList[1:]))
		return [leftList[0]] + mergeList(leftList[1:], rightList) 
	else:  
		# print("leftList = " + str(leftList))
		# print("rightList = " + str(rightList))
		# print("rightList : " + str(rightList[1:]))
		return [rightList[0]] + mergeList(rightList[1:], leftList)


def chopList(sourceList):
	
	if 1 >= len(sourceList):
		return sourceList
	
	centerKey = int(round(len(sourceList)/2))
	leftList = []
	rightList = []
	
	leftList = sourceList[0:centerKey]
	rightList = sourceList[centerKey:]

	leftData = chopList(leftList)
	rightData = chopList(rightList)

	return mergeList(leftData, rightData)


# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(chopList(insertArray))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 第二次做

def mergeList(leftList, rightList):

	if len(leftList) == 0:
		return rightList
	elif len(rightList) == 0:
		return leftList
	elif leftList[0] < rightList[0]:
		return [leftList[0]]+ mergeList(leftList[1:], rightList)
	else:
		# return [rightList[0]] + mergeList(rightList[1:], leftList)
		return [rightList[0]] + mergeList(leftList, rightList[1:])



def chopList(sourceList):
	
	if len(sourceList) <= 1:
		return sourceList

	centerKey = len(sourceList)/2

	leftList = sourceList[:centerKey]
	rightList = sourceList[centerKey:]
	
	leftData = chopList(leftList)
	leftData = chopList(rightList)

	return mergeList(chopList(leftList), chopList(rightList))



print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(chopList(insertArray))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))




first = [0]
second = [1]
print(first + second)





















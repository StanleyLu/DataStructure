import time
import math

import random

insertArray = []
s = 0
while s < 9:
	tempRandNum = random.randint(0,100)
	insertArray.append(tempRandNum)
	s = s + 1 

print(insertArray)

def mergeList(leftList, rightList):

	if len(leftList) == 0:  
		return rightList  
	elif len(rightList) == 0:  
		return leftList  
	elif leftList[0] < rightList[0]:
		return [leftList[0]] + mergeList(leftList[1:], rightList) 
	else:
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


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(chopList(insertArray))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))





















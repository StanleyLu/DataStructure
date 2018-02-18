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
# 這邊是合併的Function，合併時會有左邊的List和右邊的List
def mergeList(leftList, rightList):
	# 判斷左(右)邊的List，如果只有一邊有值，就可直接回傳
	if len(leftList) == 0:  
		return rightList  
	elif len(rightList) == 0:  
		return leftList  
	# 比較兩邊List的第一個值，如果右邊大於左邊，那麼就將左邊的第一個值放入，並將後面的值繼續做合併和排序的工作，直到將所有的值都比較完為止
	elif leftList[0] < rightList[0]:
		return [leftList[0]] + mergeList(leftList[1:], rightList) 
	# 與上一段做的工作相同，方向相反
	else:
		return [rightList[0]] + mergeList(rightList[1:], leftList)

# 這一段撰寫的是分割的Function
def chopList(sourceList):
	# 如果List只包含一個值，則直接回傳
	if 1 >= len(sourceList):
		return sourceList
	# 找出中間位置
	centerKey = int(round(len(sourceList)/2))
	leftList = []
	rightList = []
	# 將List分成左右兩邊
	leftList = sourceList[0:centerKey]
	rightList = sourceList[centerKey:]
	# 不斷分割，直到List內剩下一個值
	leftData = chopList(leftList)
	rightData = chopList(rightList)
	# 當無法分割時則開始合併
	return mergeList(leftData, rightData)


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(chopList(insertArray))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))





















'''
def greetings(name):
	print("Welcome to The Hundred Acre Wood " + name +"! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")
'''
'''
# U - The problem is asking to find the first instance of target from the list
# and return the index. If it's not found, return -1
# M - this problem is similar to many list problems that require you to loop
# through a list and find an element
# P - loop through the lst with enumerate to track index. If lst[i] == target
# return i. else return -1
def linear_search(lst, target):
	for i in range(len(lst)):
		if lst[i] == target:
			return i
	return -1



items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))
'''

# u - the problem is asking to remove the substrings t, i, gg, er from the input and return the the string
# m - the problem is similar to many split problems that require you to get a substring.
# p - get the word and split it by t, i, gg, er. then revmove those chars. after join them back and return the 
# the word

'''
def tiggerfy(word):
	word = word.lower()
	split = word.split("t")
	joined = ''.join(split)
	split = joined.split("i")
	joined = ''.join(split)
	split = joined.split("gg")
	joined = ''.join(split)
	split = joined.split("er")
	joined = ''.join(split)
	return joined

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))'
'''

# U - return bool whether an arr is sorted in descending order. if it is sorted in desc return false, else true
# M - this is similar where we need to compare elements of an arr to each other
# P - loop through the arr and compare two indexes, i and j=i+1. if arr[j] > arr[i] return true
def non_decreasing(nums):
	for i in range(len(nums)-1):
		j = i+1
		if nums[j] > nums[i]:
			return True
	return False



nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1, -1]
print(non_decreasing(nums))
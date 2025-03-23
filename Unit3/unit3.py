# #balanced () problem

# def is_balanced(parens): 
#     if not parens:
#         return False
#     #impl stack
#     opens = []
#     #loop through parens
#     for paren in parens:
#         if paren == "(":
#             opens.append(paren)
#     #for close, pop
#         else:
#             if not opens:
#                 return False
#             else:
#                 opens.pop()

#     return True if not opens else False
# #---------------------------------------

# def is_valid_post_format(posts):
#     #dictionary to match closing tags with their opening tags
#     paren = {')': '(', ']' : '[', '}': '{' }
#     stack = []
#     #stack to keep track of open and close
#     #for loop
#     for char in posts:
#         if char in paren.values():
#             stack.append(char)
#         elif char in paren:
#             if not stack or stack[-1] != paren[char]:
#                 return False
#             stack.pop()
#     return not stack
#     #if not stack or top element != dictionary then return false
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

# -------------------------------------------

# initialize the stacj
# loop through the stack
# insert the comments into the stack from the queue
# return it

# def reverse_comments_queue(comments):
#     stack = []
#     for comment in comments:
#         #stack.append(comment) WRONG
#         stack.insert(0,comment)


#     return stack

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# ---------------------------------------------


# def is_symmetrical_title(title):

#     title_striped = title.replace(" ","").lower()
#     print(title_striped)
#     r = len(title_striped) - 1

#     for l in range(len(title_striped)):
#         print(f"l: {l} - r: {r}")
#         if l == r:
#             return True

#         if title_striped[l] != title_striped[r]:
#             return False
#         r -= 1
#      return True


# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

# -------------------------------------------
# def engagement_boost(engagements):
#     # store elements in engagements list squared
#     squared_engagements = [0] * len(engagements)
#     l, r = 0, len(engagements) - 1
#     index = len(engagements) - 1


# # -4, -1, 0, 3, 10
# #     l      r


# #         16  ,100
# #        index

#     while l <= r:
#         left_sq = engagements[l]**2
#         right_sq = engagements[r]**2

#         if left_sq > right_sq:
#             squared_engagements[index] = left_sq
#             l += 1
#         else:
#             squared_engagements[index] = right_sq
#             r -= 1

#         index -= 1

#     return squared_engagements

#     # right_sq = engagements[right]**2
#     # if left_sq > right_sq
#     # result[i] = left_sq
#     # left += 1 

#     #initialize len of engagements
#     #initialize left and right to represent 2 pointers

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))
# -----------------------------------------------------------

# poOost
# p o s t 

# abBAcC
# 
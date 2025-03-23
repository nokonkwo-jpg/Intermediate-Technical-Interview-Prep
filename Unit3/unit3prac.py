from collections import deque
'''

movies are the number of movies a person at any given position wants to watch
k is the index of the person
we should process the first element, decr, then add it to the back of the queue. Next person gets processed, decr,
add them to teh back of the que. this repeates until person of position k gets to 0
'''
'''
def time_required_to_stream(movies, k):
    
    streamed = deque()

    time = 0

    for index, want_to_watch in enumerate(movies):
        streamed.append((index, want_to_watch))

    while streamed:
        temp_index, temp_watch = streamed.popleft()

        time += 1
        temp_watch -= 1
        
        if temp_watch == 0 and temp_index == k:
            
            return time
        
        if temp_watch > 0:
            streamed.append((temp_index, temp_watch))
    return time

print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 
'''
'''
#U - the funtion reverse_watchlist takes an array and reverses it in place. We can not use slicing. Must use two pointer
#M - The closest problem I know is two pointer where you literally use two pointers(vars) and iterate over and arr
#P - Let's initialize one variable j which is the end of the list. Then create a for loop with var i. j must be greater
# than i so we check that first. if i > j then we know we're done. else create a temp. temp = arr[i], arr[i] = arr[j],
# arr[j] = temp. then dec j.

def reverse_watchlist(watchlist):
    j = len(watchlist) - 1
    for i in range(len(watchlist)):
        if i >= j:
            return watchlist
        temp = watchlist[i]
        watchlist[i] = watchlist[j]
        watchlist[j] = temp
        j-=1
    return watchlist


watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]

print(reverse_watchlist(watchlist))
'''
'''
#U - the problem is asking us to remove duplicate & ADJACENT letters from the string. Adjacent is an important keyword
#M - This problem is similar to the set problems we've encountered but it's important to note that because they are 
# adjacent. A stack works better than a set here
#P - the plan is to iterate through the string and each letter is put in the stack. If the prev letter matches the curr letter
# pop the prev letter from the stack. keep going till the stack is empty 
def remove_duplicate_shows(schedule):
    seen = []
    for i in range(len(schedule)):
        if seen and seen[-1] == schedule[i]:
            top = seen[-1]
            seen.pop()
            print("This is whats popped", top, i, schedule[i])
        else:
            seen.append(schedule[i])
            print("this is whats appended", seen[-1] , i, schedule[i])
    return "".join(seen)


print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy")) '
'''

def space_crew(crew, position):
    pass


exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))
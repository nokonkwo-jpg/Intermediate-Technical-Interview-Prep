from queue import PriorityQueue

def process_performance_requests(requests):
    prQueue = PriorityQueue()
    for items in requests: 
        prQueue.put((items[0], items[1]))
    sorted_array = []
    while not prQueue.empty():
        _, event = prQueue.get()
    #print(priority, event)
        sorted_array.append(event)
        #print(sorted_array)
    
    sorted_array.reverse()
    
    return sorted_array
    

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
 # Understand - requests is an queue of requests with a weight attached

 # Match -  this a problem for processing the tuple by tuple in a queue

 #Plan - 
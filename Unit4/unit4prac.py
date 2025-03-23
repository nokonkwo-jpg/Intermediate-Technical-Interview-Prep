'''
def extract_nft_names(nft_collection):
    names = []
    for nfts in nft_collection:
        names.append(nfts.get("name"))
    return names


# U - the problem is asking to parse through a list and get the names of NFT's
# P loop through the list o - n, get name

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))'
'''
'''
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))'
'''
'''
# p - loop through the list. get key 
def identify_popular_creators(nft_collection):
    creatorNames = {}
    popularName = set()
    for nft in nft_collection: #Feel free to copy the code if you'd like
        if nft["creator"] not in creatorNames:
            creatorNames[nft["creator"]] = 1
        else:
            creatorNames[nft["creator"]] += 1
            popularName.add(nft["creator"])
    
    return list(popularName)

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))'
'''
'''
# U - the problem is asking us go through the values and count the number of unique characters
# M - set problems where we see which chars are redundant.
# P - get all the keys and put them in a set. then return sixe of swet
def count_unique_characters(script):
  unique = set(script.keys())
  return len(unique)

script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) '
'''
'''
# U - the problem is asking us for the most frequent value of a list. return the most freq
# M - math this to most frquency map problems where you loop through the dictionary and get the 
# most common val
# P - initialize a empty dictionary. for v in scenes.values. loop through v and the key is i.e
# action and value +=1. return empty dict
def find_most_frequent_keywords(scenes):
    freq = dict()
    for v in scenes.values():
        for descrp in v:
            if descrp not in freq:
                freq[descrp] =1
            else:
                freq[descrp] += 1
    max = 0
    for v in freq.values():
        if v > max:
            max = v
    
    li = []
    for key,value in freq.items():
        if value==max:
            li.append(key)
    return li


scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes)) '
'''

'''
# Problem 3: Track Scene Transitions
# Given a list of scenes in a story, use a queue to keep track of the transitions from one scene to the next. You need to simulate the transitions by processing each scene in the order they appear and print out each transition from the current scene to the next.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

#Prblm is simulating Queue behavior
#convert list to queue
#check for empty list and list size less than two
#we keep two pointers at i,i+1.
#increment pointer and print
from collections import deque
def track_scene_transitions(scenes):
  if not scenes or len(scenes)<2:
    return

  queue = deque(scenes)
  first = queue.popleft()
  while queue:
    second = queue.popleft()
    print(f"Transition from {first} to {second}")
    first = second


scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)


# Example Output:

# Transition from Opening to Rising Action
# Transition from Rising Action to Climax
# Transition from Climax to Falling Action
# Transition from Falling Action to Resolution

# Transition from Introduction to Conflict
# Transition from Conflict to Climax
# Transition from Climax to Denouement'
'''
def organize_scene_data_by_date(scene_records):
    return sorted(scene_records, key=lambda x: x[0])

scene_records = [
    ("2024-08-15", "Climax"),
    ("2024-08-10", "Introduction"),
    ("2024-08-20", "Resolution"),
    ("2024-08-12", "Rising Action")
]
print(organize_scene_data_by_date(scene_records))

scene_records = [
    ("2023-07-05", "Opening"),
    ("2023-07-07", "Conflict"),
    ("2023-07-01", "Setup"),
    ("2023-07-10", "Climax")
]
print(organize_scene_data_by_date(scene_records))
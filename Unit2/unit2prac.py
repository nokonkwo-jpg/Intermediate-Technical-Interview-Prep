'''
def lineup(artists, set_times):
    return dict(zip(artists, set_times))

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

def lineup(artists, set_times):
    lineup = {}
    for i in range(len(artists)):
        lineup[artists[i]] = set_times[i]

    return lineup



artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))'
'''
'''
# U - take a string artists and use it to search through a dict, festival_schedule, to find said artist.
# M - this problem is about accessing values in a dictionary. Similar to array problems with target.
# P - create a dictionary that has the default message. then simply run a get command on fest_sche with artist as the key.
# if this is successful pop the default message. else return the created dictionary
def get_artist_info(artist, festival_schedule):
    artist_info = {"message":"Artist not found"}
    if festival_schedule.get(artist) is not None:
        artist_info[artist] = festival_schedule.get(artist)
        artist_info.pop("message")

    return artist_info

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule)) '
'''
'''
# U - the problem wants me to add up all the values in a dictionary
# M - similar to many problems asking to access elements of a dict.
# P - loop through the values and add them to each other. Then return the total
def total_sales(ticket_sales):
    total = 0
    for v in ticket_sales.values():
        total +=v

    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))'
'''
'''
# U - the problem wants me to go through both maps to see if there are any conflicts in k & v. then return the k,v pair
# M - i've yet to see a problem this is similar to
# P - initialize an empty dict. then loop through k,v of v1 and put it in the empty dict. then loop through k,v of
# v2. if the k,v of v2 is seen the empty dict, then put it in another empty dict.
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = dict()
    for k,v in venue1_schedule.items():
        if venue2_schedule.get(k) == v:
            conflicts[k] = v
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
# E - Midway through I came up with another plan and realized i didn't have to loop through twice but rather could
# just loop through one venue and if any values in v2 matched the ones in v1 add them to the empty dictionary
'''
'''
from collections import Counter
def best_set(votes):
    count = Counter(votes.values())
    ans = count.most_common(1)
    ans1,ans2 = ans[0]
    return ans1

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))'
'''
import string
def can_trust_message(message):
    alphabet = set(string.ascii_lowercase)
    for char in message:
        alphabet.discard(char)
    if alphabet:
        return False
    return True

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
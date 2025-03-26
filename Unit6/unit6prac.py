'''
class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
#top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))


#print_linked_list(top_hits_2010s)

n1 = SongNode("Uptown FUnk")
n2 = SongNode("Party Rock Anthem")
n3 = SongNode("Bad Romance")

n1.next = n2
n2.next = n3

print_linked_list(n1)
'''
#U - return the frquency of each value
# M - similar to frequency map problems
# P loop through the list. the value that we see is key, and freq is value.
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

'''
def get_artist_frequency(playlist):
    freq_dict = dict()
    while playlist:
        if playlist.artist in freq_dict:
            freq_dict[playlist.artist] += 1
        else:
            freq_dict[playlist.artist] = 1
        playlist = playlist.next
    return freq_dict


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))'
'''

'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))'
'''
# P - loop through the list. for each node you see, put it in the set. If you see a node again
# remove from set and return true, else false
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    seen = set()

    #tempporary node curr and store the head of the linkedlist

    #use curr to traverse through the list
    curr = playlist_head

    if playlist_head is None:
        return False
    while curr:
        if curr in seen:
            return True
        seen.add(curr)  #this should be 
        curr = curr.next
    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
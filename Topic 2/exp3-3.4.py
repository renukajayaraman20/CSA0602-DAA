n = int(input("Enter number of songs: "))

playlist = []

for i in range(n):
    name = input(f"Enter song name {i+1}: ")
    duration = int(input("Enter duration: "))
    playlist.append((name, duration))

new_name = input("Enter new song name: ")
new_duration = int(input("Enter new song duration: "))

playlist.append((new_name, new_duration))

i = len(playlist) - 1

while i > 0 and playlist[i - 1][1] > playlist[i][1]:
    playlist[i], playlist[i - 1] = playlist[i - 1], playlist[i]
    i -= 1

print("Updated Playlist:")
for song in playlist:
    print(song)

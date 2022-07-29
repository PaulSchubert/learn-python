from nested_data import albums

SONGS_LIST_INDEX = 3 # constant that refers to the fourth item in the list
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits): ")

    # enumerate returns two values
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
              .format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song: ")
    for index, (track_num, song) in enumerate(song_list):
        print("{}: {}"
              .format(index +1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice -1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("=" * 40)
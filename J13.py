albumCollection = [["Where Rivers Meet", "Z Rahman", 2008, "World"], ["Best of CatStevens", "C Stevens", 1984, "Pop"], ["Come Away With Me", "N Jones", 2012, "Pop"],
                   ["Shine", "Bond", 2002, "Instrumenta"], ["Blessing", "J Rutter", 2012, "Classical"]]
userNewList = []

found = False
index = 0
anotherGo = 'y'

while anotherGo == 'y':

        inputUser = input('Enter s to search or enter e to append new artist to the list: ')
        if inputUser == 'e':
            print('Pls kindly req u to ans the question below: ')
            songName = input('Enter a song name pls: ')
            userNewList.append(songName)
            artist = input('Enter the artist name pls: ')
            userNewList.append(artist)
            musicReleaseDate = int(input('Enter the date of the song releases: '))
            userNewList.append(musicReleaseDate)
            musicType = input('Enter the type of the music: ')
            userNewList.append(musicType)

            albumCollection.append(userNewList)
            print(albumCollection)
        elif inputUser == 's':

            songName = input('Enter your song name: ')
            while index < len(albumCollection) and not found:
    #for index in range(0,len(albumCollection)):

                if songName == albumCollection[index][0]:
                    print('Song is found!')
                    print('The name of the singer is', albumCollection[index][1])
                    print('The release date of the song is', albumCollection[index][2])
                    print('The type of the song is', albumCollection[index][3])
                    found = True

                else:
                    index += 1
            if found == False:
               print('The song is not found!')
        anotherGo = input("Enter 'y' if you wanna try again")



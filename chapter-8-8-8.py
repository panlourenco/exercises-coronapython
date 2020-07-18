# 8-7. User Albums:

def make_album(artist , title):
    album_dict = {
        
        'artist': artist.title(),
        'title': title.title(),

    }
    return album_dict


while True:
    print("\n*** Enter 'q' at any time to quit ***\n")

    user_album= input("\n Please enter the album's artist:\n")
    if user_album =='q':
        break
    title_album=input("\n Please enter the album's title:\n")
    if title_album == 'q':
        break
    album = make_album(user_album, title_album)
    print(album)
    
print("\nThank you, have a good day ahead!\n")
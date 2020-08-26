# 8-7. Album:

def make_album(artist , title):
    album_dict = {
        
        'artist': artist.title(),
        'title': title.title(),

    }
    return album_dict

album = make_album('dream theater', 'train of thought')
print(album)

album = make_album('chopin', 'mazurkas')
print(album)

album = make_album('john coltrane', 'my favorite things')
print(album)
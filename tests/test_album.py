from lib.albums import Album

def test_album_construct():
    album = Album(1, 'Midnights', '2022', '3')
    assert album.id == 1
    assert album.title == 'Midnights'
    assert album.release_year == '2022'
    assert album.artist_id == '3'

def test_albums_are_equal():
    album1 = Album(1, 'Midnights', '2022', '3')
    album2 = Album(1, 'Midnights', '2022', '3')
    assert album1 == album2

def test_albums_format_nicely():
    album = Album(1, "Midnights", "2022", "3")
    assert str(album) == "Album(1, Midnights, 2022, 3)"


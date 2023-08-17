from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

"""
GET /album
Get a list of albums
"""
# def test_get_album(web_client, db_connection):
#     db_connection.seed('seeds/music.sql')
#     response = web_client.get("/albums")
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#         "Album(1, Doolittle, 1989, 1)\n" \
#         "Album(2, Surfer Rosa, 1988, 1)\n" \
#         "Album(3, Waterloo, 1974, 2)\n" \
#         "Album(4, Super Trouper, 1980, 2)\n" \
#         "Album(5, Bossanova, 1990, 1)\n" \
#         "Album(6, Lover, 2019, 3)\n" \
#         "Album(7, Folklore, 2020, 3)\n" \
#         "Album(8, I Put a Spell on You, 1965, 4)\n" \
#         "Album(9, Baltimore, 1978, 4)\n" \
#         "Album(10, Here Comes the Sun, 1971, 4)\n" \
#         "Album(11, Fodder on My Wings, 1982, 4)\n" \
#         "Album(12, Ring Ring, 1973, 2)" 
    
def test_add_album(web_client, db_connection, page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    h_1 = page.locator("h1")
    expect(h_1).to_have_text("Albums!")
    db_connection.seed('seeds/music.sql')
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, Voyage, 2022, 2)" 
    
# def test_get_artist(web_client, db_connection):
#     db_connection.seed('seeds/music_artist.sql')
#     response = web_client.get("/artists")
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#     "Artist(1, Pixies, Rock)\n" \
#     "Artist(2, ABBA, Pop)\n" \
#     "Artist(3, Taylor Swift, Pop)\n" \
#     "Artist(4, Nina Simone, Jazz)" 
    
    

def test_post_artist(web_client, db_connection):
    db_connection.seed('seeds/music_artist.sql')
    response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
    "Artist(1, Pixies, Rock)\n" \
    "Artist(2, ABBA, Pop)\n" \
    "Artist(3, Taylor Swift, Pop)\n" \
    "Artist(4, Nina Simone, Jazz)\n" \
    "Artist(5, Wild Nothing, Indie)"

        
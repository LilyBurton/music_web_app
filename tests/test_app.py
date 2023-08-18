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
def test_get_first_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/music_artist.sql')
    page.goto(f"http://{test_web_address}/2")
    para_tags = page.locator("p")
    expect(para_tags).to_contain_text("Release year: 1988")
    expect(para_tags).to_contain_text("Artist: Pixies")

def test_get_second_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/music_artist.sql')
    page.goto(f"http://{test_web_address}/1")
    para_tags = page.locator("p")
    expect(para_tags).to_contain_text("Release year: 1989")
    expect(para_tags).to_contain_text("Artist: Pixies")

def test_get_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/contain.sql')
    page.goto(f"http://{test_web_address}/albums")
    para_tags = page.locator("p")
    expect(para_tags).to_have_text([
        "Title: Doolittle",
        "Released: 1989",
        "Title: Surfer Rosa",
        "Released: 1988"
    ])


    
# def test_get_artist(web_client, db_connection):
#     db_connection.seed('seeds/music_artist.sql')
#     response = web_client.get("/artists")
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#     "Artist(1, Pixies, Rock)\n" \
#     "Artist(2, ABBA, Pop)\n" \
#     "Artist(3, Taylor Swift, Pop)\n" \
#     "Artist(4, Nina Simone, Jazz)" 
    
    

def test_post_artist(web_client, db_connection, test_web_address):
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

        
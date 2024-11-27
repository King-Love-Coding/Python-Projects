import lyricsgenius

token = "PmEFpewQ4-VewKyUMrUO_OTXSXCaai2H60fFt6NIGCwebV7GODremzwE9wV-gkws"
genius = lyricsgenius.Genius(token)
artist = genius.search_artist("Shreya Ghoshal", max_songs=2, sort="title")
print(artist.songs)
song = genius.search_song("Mere Dholna", "Shreya Ghoshal")
print(song.lyrics)

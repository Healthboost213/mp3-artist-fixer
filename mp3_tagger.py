from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os

folder_path = ".\\music"

# Change the Artist Field
def artist_change(file_path):
    try:
        audio = EasyID3(file_path)
    except:
        audio = MP3(file_path, ID3=EasyID3)
        audio.add_tags()
        print("🟡 Missing Metadata. Added ID3 Tags.")

    main_artist = audio['albumartist'][0].split('; ')[0]
    if audio['artist'][0] != main_artist:
        audio['artist'] = main_artist
        audio['albumartist'] = main_artist
        audio.save()
    
    print("🟢 Completed Renaming", audio['album'][0] + ' - ' + audio['title'][0])

# Read Folder and Adjust's Artist Name
def folder_read():
    
    for artist in os.listdir(folder_path):
        for album in os.listdir(os.path.join(folder_path, artist)):
            for file in os.listdir(os.path.join(folder_path, artist, album)):
                if file.endswith(".mp3"):
                    curr_file = os.path.join(folder_path, artist, album, file)
                    artist_change(curr_file)
    
    print("\n ✅ Finished Renaming All Files")

folder_read()


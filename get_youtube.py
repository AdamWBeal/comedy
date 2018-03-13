# import youtube_dl
#
# options = {'outtmpl': '%(id)s'}  # save file as the YouTube ID
# with youtube_dl.YoutubeDL(options) as ydl:
#     ydl.download(['http://www.youtube.com/watch?v=ZHWZf1Z4B5k'])

import youtube_dl

# download metadata
ydl = youtube_dl.YoutubeDL()
r = None
url = "https://www.youtube.com/watch?v=hwsXo6fsmso"
with ydl:
    # don't download, much faster
    r = ydl.extract_info(url, download=False)

# print some typical fields
print( "%s uploaded by '%s', has %d views, %d likes, and %d dislikes" )% (
    r['title'], r['uploader'], r['view_count'], r['like_count'], r['dislike_count'])

import pytube
url = 'type your url here'
youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download() # In Other Folder
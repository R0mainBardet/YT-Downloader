import pytube import Youtube

url = input("Url Youtube")
yt = Youtube(url)

stream = yt.streams.get_audio_only()

stream.download()
print("Réussi")


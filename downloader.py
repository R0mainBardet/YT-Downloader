import os
import yt_dlp

def download_youtube_playlist(url, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(playlist)s/%(title)s.%(ext)s'), 
        'yesplaylist': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Téléchargement de la playlist terminé !")

if __name__ == "__main__":
    youtube_url = input("Entrez l'URL de la playlist YouTube Music : ")
    output_folder = input("Entrez le dossier de destination : ")
    download_youtube_playlist(youtube_url, output_folder)

from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Fazendo o download")
        youtubeObject.download()
    except:
        print("Erro")
    print("Download completo!")


link = input("Cole o link do video: ")
Download(link)
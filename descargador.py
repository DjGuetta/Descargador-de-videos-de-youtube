from pytube import YouTube

link = input("Ingresa tu link:  ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

input("Presiona enter para salir... ")

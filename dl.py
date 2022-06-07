from pytube import YouTube
out_file = YouTube("https://www.youtube.com/watch?v=KzQiRABVARk").streams.filter(only_audio=True).first().download(output_path="./")
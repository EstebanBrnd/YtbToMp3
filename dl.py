from pytube import YouTube
out_file = YouTube("link here").streams.filter(only_audio=True).first().download(output_path="./")
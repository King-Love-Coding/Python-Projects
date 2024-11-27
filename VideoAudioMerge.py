from moviepy.editor import VideoFileClip, AudioFileClip


video_path = "MrunalThakur.mp4"
audio_path = "Aaj Ki Raat.mp3"
output_path = "mixture_video.mp4"

try:

    video_clip = VideoFileClip(video_path)
    print(f"Video duration: {video_clip.duration} seconds")
    audio_clip = AudioFileClip(audio_path)
    print(f"Audio duration: {audio_clip.duration} seconds")
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print("Merging completed successfully!")
    click = VideoFileClip(output_path)
    click.preview()
except Exception as e:
    print(f"An error occurred: {e}")

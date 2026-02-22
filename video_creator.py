from moviepy import ImageClip, AudioFileClip
import os

def create_video(audio_path):
    """
    Creates a simple video using a static background image
    and the generated audio.
    Returns the final video file path.
    """

    output_video_path = "final_video.mp4"
    background_image_path = "background.jpg"


    if not os.path.exists(background_image_path):
        raise FileNotFoundError("background.jpg not found in project folder")


    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")


    audio = AudioFileClip(audio_path)


    image_clip = ImageClip(background_image_path).with_duration(audio.duration)


    final_clip = image_clip.with_audio(audio)


    final_clip.write_videofile(output_video_path, fps=24)

    return output_video_path
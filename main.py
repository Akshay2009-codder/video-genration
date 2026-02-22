import os
from topic_generator import get_topic
from script_generator import generate_script
from voice_generator import text_to_speech
from video_creator import create_video


def run_pipeline():
    print(" Starting Automated Video Pipeline...\n")


    topic = get_topic()
    print(f" Selected Topic: {topic}\n")


    script = generate_script(topic)
    print(" Script Generated Successfully!\n")

    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)


    audio_path = text_to_speech(script)
    print(f" Audio Created: {audio_path}\n")


    output_video = create_video(audio_path)
    print(f" Video Created Successfully: {output_video}\n")

    print(" Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()
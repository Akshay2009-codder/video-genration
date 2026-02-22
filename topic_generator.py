import random

def get_topic():
    """
    Selects a random topic for the video.
    """

    topics = [
        "What happens if Earth stops rotating?",
        "What if humans could live on Mars?",
        "What if dinosaurs still existed?",
        "What happens inside a black hole?",
        "What if gravity suddenly disappeared for 10 seconds?"
    ]

    selected_topic = random.choice(topics)
    return selected_topic
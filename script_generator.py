import random

def generate_script(topic):

    hooks = [
        "What if I told you something crazy?",
        "This might blow your mind!",
        "Imagine this for a second...",
        "You won't believe this!",
        "Think about this..."
    ]

    middle_templates = [
        f"If {topic.lower()} suddenly happened, the world would completely change.",
        f"The moment {topic.lower()} became real, everything would shift.",
        f"If {topic.lower()} was true, daily life would never be the same."
    ]

    endings = [
        "Would humanity survive? Or would everything collapse?",
        "The consequences would be absolutely insane.",
        "It could either save the world... or destroy it.",
        "And that's just the beginning."
    ]

    script = f"""
{random.choice(hooks)}

{random.choice(middle_templates)}

Cars would stop. Planes would struggle. People would panic.

{random.choice(endings)}

Follow for more mind-blowing scenarios!
"""

    return script.strip()
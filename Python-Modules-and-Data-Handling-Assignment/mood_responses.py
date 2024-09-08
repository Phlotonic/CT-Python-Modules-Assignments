def mood_response(mood):
    """
    This function takes the user's mood as input and returns a custom message.
    """
    # Dictionary mapping moods to responses
    responses = {
        "happy": "That's great to hear! Keep smiling! 😊",
        "sad": "I'm sorry to hear that. I hope things get better soon. 💙",
        "excited": "Awesome! Enjoy the excitement! 🎉",
        "angry": "Take a deep breath. It's going to be okay. 🧘",
        "tired": "Make sure to get some rest. You deserve it. 😴",
        # Add more moods and responses as needed
    }

    # Return the response based on the mood, or a default message if the mood is not recognized
    return responses.get(mood.lower(), "I'm not sure how to respond to that mood. 🤔")

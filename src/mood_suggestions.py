def generate_suggestions(mood):
    """
    Generates mood-enhancing suggestions based on the detected mood.
    """
    suggestions = {
        'happy': "Keep up the positive vibes! Maybe share your joy with friends or take on a new challenge.",
        'neutral': "Engage in a relaxing activity or try something new to add a bit of excitement.",
        'sad': "It's okay to feel down. Consider talking to a friend, practicing mindfulness, or doing something you enjoy."
    }
    return suggestions.get(mood, "No suggestion available.")
# Import the mood_response function from the mood_responses module
import mood_responses

# Ask the user how they are feeling today
mood = input("How are you feeling today? ")

# Print the custom response based on the user's mood
print(mood_responses.mood_response(mood))

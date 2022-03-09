
def emotionResponse():
    print("How do you feel? Are you sad, angry or happy?")
    emotion = input()
    if emotion == ("sad" or "sadd" or "ssad"):
        print("Here's the number for a good therapist I know: 604-123-4567")
    elif emotion == "angry":
        print("Here's the number for an anger management counselor: 778-123-4567")
    elif emotion == "happy" or "Happy":
        print("That's great! Have a great day!")

#First time
emotionResponse()

#Second time
emotionResponse()
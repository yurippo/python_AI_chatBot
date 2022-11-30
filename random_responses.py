import random


def random_string():
    #if the user types something that's unknown

    random_sentences = [
        "Could you please provide us with further details of your problem?! 🤓 "
        "Thanks",
        "Oh! It appears you wrote something I will have to check. Could you please prodive further details?! 🤓"
        "Thank you",
        "Do you mind providing us further details about that? 🤓",
        "Could you please tell me more?! 🤓",
        "I'll have to check it for you ok 🤓"
    ]

    list_count = len(random_sentences)
    random_item = random.randrange(list_count)

    return random_sentences[random_item]
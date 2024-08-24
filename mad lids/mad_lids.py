import random


def get_input(word_type:str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


gender = input("Enter M or F:  ")

if gender == "M":
    noun1 = get_input("noun")
    characters = [f"a boy named {noun1}"]
else:
    noun2 = get_input("noun")
    characters = [f"a girl named {noun2}"]


beginnings = ["Once upon a time", "In a land far away",
              "In the not-so-distant future"]
settings = ["a mysterious forest", "a bustling city",
            "an ancient castle"]
conflicts = ["battling a fearsome dragon",
             "discovering a hidden treasure",
             "solving a perplexing mystery"]
endings = ["and they all lived happily ever after",
           "and the world was forever changed",
           "and they found their way back home."]


def generate_story():
    beginning = random.choice(beginnings)
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    ending = random.choice(endings)

    ran_story = f"{beginning}, {character}\
    set out on a journey to {setting}. \
    They faced the challenge of {conflict}. {ending}"

    return ran_story


if __name__ == '__main__':
    story = generate_story()
    print(story)

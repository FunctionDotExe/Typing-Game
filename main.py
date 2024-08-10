import random
from threading import Timer

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

score = 0

list = ("It had been sixteen days since the zombies first attacked.", "The wake behind the boat told of the past while the open sea for told life in the unknown future.", "She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news.", "He learned the important lesson that a picnic at the beach on a windy day is a bad idea.", "He wondered if it could be called a beach if there was no sand.", "Dolores wouldn't have eaten the meal if she had known what it actually was.", "Improve your goldfish's physical fitness by getting him a bicycle", "He was surprised that his immense laziness was inspirational to others. ", "He had unknowingly taken up sleepwalking as a nighttime hobby.")
list2 = ("""Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers?
Where's the peck of pickled peppers Peter Piper picked?
""" , """How much wood would a woodchuck chuck if a woodchuck could chuck wood?
He would chuck, he would, as much as he could, and chuck as much wood,
as a woodchuck would if a woodchuck could chuck wood.""" , """Betty bought a bit of butter.
But the butter Betty bought was bitter.
so Betty bought a better butter,
and it was better than the butter Betty bought before.""", """All I want is a proper cup of coffee,
Made in a proper copper coffee pot
I may be off my dot
But I want a cup of coffee
From a proper coffee pot.
"", ""Amidst the mists and coldest frosts,
With stoutest wrists and loudest boasts,
He thrusts his fists against the posts,
And still insists he sees the ghosts.""")

endgame = 0

def printbob():
    print("sad u lost :(")
    endgame = 1

def boys():
    points = 0
    while(score >= 0):
        timeout = 30
        timer = Timer(timeout, printbob)
        timer.start()
        if(points < 5):
            cs = random.choice(list)
        else:
            cs = random.choice(list2)
        print("Type this sentence:", color.GREEN + cs + color.END)
        user = "You have %d seconds to -write the correct answer...\n" % timeout
        answer = input(user)
        timer.cancel()
        if (answer == cs) and (endgame == 0):
            print("Nice")
            points += 1
        else:
            print("You didnt type it write, cya :D")
            exit()
boys()
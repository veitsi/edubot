import random
jokes=[
"Q. How did the programmer die in the shower? A. He read"\
" the shampoo bottle instructions: Lather. Rinse. Repeat.",
"How many programmers does it take to change a light bulb?"\
"None – It’s a hardware problem",
"There are only 10 kinds of people in this world: those who know"
"binary and those who don’t.",
"A programmer walks to the butcher shop and buys a kilo of meat.  An hour later"
"he comes back upset that the butcher shortchanged him by 24 grams.",
"Programming is like sex: One mistake and you have to support it for the rest of your life."
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# A man is smoking a cigarette and blowing smoke rings into the air.  His girlfriend becomes irritated with the smoke and says, “Can’t you see the warning on the cigarette pack?  Smoking is hazardous to your health!”
#
# To which the man replies, “I am a programmer.  We don’t worry about warnings; we only worry about errors.”
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# There are three kinds of lies: Lies, damned lies, and benchmarks.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# A programmer is walking along a beach and finds a lamp.  He rubs the lamp, and a genie appears.  “I am the most powerful genie in the world.  I can grant you any wish, but only one wish.”
#
# The programmer pulls out a map, points to it and says, “I’d want peace in the Middle East.”
#
# The genie responds, “Gee, I don’t know.  Those people have been fighting for millennia.  I can do just about anything, but this is likely beyond my limits.”
#
# The programmer then says, “Well, I am a programmer, and my programs have lots of users.  Please make all my users satisfied with my software and let them ask for sensible changes.”
#
# At which point the genie responds, “Um, let me see that map again.”
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# All programmers are playwrights, and all computers are lousy actors.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Have you heard about the new Cray super computer?  It’s so fast, it executes an infinite loop in 6 seconds.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# The generation of random numbers is too important to be left to chance.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# “I just saw my life flash before my eyes and all I could see was a close tag…”
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# The computer is mightier than the pen, the sword, and usually, the programmer.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Debugging: Removing the needles from the haystack.
]
def give_a_joke():
    global jokes
    i=random.randrange(len(jokes)-1)
    return jokes[i]

print(give_a_joke())
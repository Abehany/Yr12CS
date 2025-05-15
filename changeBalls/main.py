import random

balls = "balls"

def changeBalls(quote):
    splitQuote = quote.split()
    if splitQuote:
        for i in range(random.randint(1, len(splitQuote)-1)):
            selected = random.randint(0, len(splitQuote) -1)

            if splitQuote[selected] == splitQuote[0]:
                splitQuote[selected] = balls.capitalize()
                changedQuote = ' '.join(splitQuote)
            
            else:
                splitQuote[selected] = balls
                changedQuote = ' '.join(splitQuote)
    return changedQuote
        
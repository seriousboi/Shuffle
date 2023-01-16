from random import *
from draw import *


def create_deck(n):
    if n < 1:
        print("deck too skinny")
        return
    deck_list= []
    for i in range(n):
        deck_list= deck_list + [i]
    return deck_list



def cut(deck):
    deck_size= len(deck)
    cutting= randrange(0,deck_size)
    new_deck=[]
    for i in range(cutting,deck_size):
        new_deck= new_deck + [deck[i]]
    for i in range(cutting):
        new_deck= new_deck + [deck[i]]
    return new_deck



def yugi_shuffle(deck):
    deck_size= len(deck)
    cutting_size= randrange(0,deck_size)
    cutting= randrange(0,deck_size-cutting_size)
    new_deck=[]
    for i in range(cutting):
        new_deck= new_deck + [deck[i]]
    for i in range(cutting+cutting_size,deck_size):
        new_deck= new_deck + [deck[i]]
    for i in range(cutting,cutting+cutting_size):
        new_deck= new_deck + [deck[i]]
    return new_deck


def overhand_shuffle(deck):
    deck_size= len(deck)
    new_deck= []
    while len(new_deck) < deck_size:
        cutting= randrange(1,1+(deck_size//2))
        new_deck= deck[0:min(len(deck),cutting)] + new_deck
        del deck[0:min(len(deck),cutting)]
    return new_deck



def rifle_shuffle(deck):
    #inspiré du model de Gilbert–Shannon–Reeds
    deck_size= len(deck)
    cutting_size= int(deck_size*((1/2)+(5-randrange(0,11))/100))
    new_deck=[]
    cutting_1= deck[0:cutting_size]
    cutting_2= deck[cutting_size:deck_size]
    while len(new_deck) < deck_size:
        if random() < len(cutting_1)/(len(cutting_1)+len(cutting_2)):
            new_deck= new_deck + [cutting_1[0]]
            del cutting_1[0]
        else:
            new_deck= new_deck + [cutting_2[0]]
            del cutting_2[0]
    return new_deck




def mash_shuffle(deck):
    return


def repeat_shuffle(deck,shuffle,n):
    for i in range(n):
        deck= shuffle(deck)
    return deck



deck= create_deck(40)
deck= repeat_shuffle(deck,overhand_shuffle,0)
test_draw_deck(deck)

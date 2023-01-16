import pygame



def spectra(value):
    [red,green,blue]= [0,0,0]
    if (value >= 0 and value <= 1):
        green= int(255*(1-value))
        blue= int(255*value)
    if (value >= 1 and value <= 2):
        blue= int(255*(1-(value-1)))
        red= int(255*(value-1))
    return [red,green,blue]



def test_spectra():
    pygame.init()
    window = pygame.display.set_mode((400,400))
    window.fill([200,200,200])
    pygame.display.update()

    for i in range(35):
        pygame.draw.rect(window,spectra(2*i/30),(50,10+i*10,200,10),0)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return



def draw_deck(deck,x,y,width,height,window):
    deck_size= len(deck)
    card_width= max(1,height//deck_size)
    for i in range(deck_size):
        pygame.draw.rect(window,spectra(2*deck[i]/(deck_size-1)),(x,y+i*card_width,height,card_width),0)



def test_draw_deck(deck):
    pygame.init()
    window = pygame.display.set_mode((400,400))
    window.fill([200,200,200])
    pygame.display.update()
    draw_deck(deck,10,10,200,350,window)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return

import random

add_library("minim")


def random1(): #Random integer generator for the Dice
    global a, b, c
    a = (random.randint(0, 2))
    b = (random.randint(0, 2))
    c = (random.randint(0, 2))


def draw():
    global x
    if page == 1: # Mainpage functionality and layout
        background(bg)
        image(logo, 535, 30)
        fill(242, 242, 242)
        for x in range(350, 950, 200):
            rect(x, 350, 100, 100, 7)  # dice
        fill(0)
        textSize(60)
        text(a, 380, 420)  # most left number
        text(b, 580, 420)  # middle number
        text(c, 780, 420)  # most right number
        fill(216, 27, 96)
        rect(525, 480, 150, 70)  # throw button
        rect(540, 250, 120, 40)  # plus card button
        rect(540, 190, 120, 40)  # o card button
        rect(1080, 20, 100, 50)  # rule button
        fill(0)
        total = (a + b + c)
        if total == 0 or total == 3 or total == 6:
            textSize(35)
            text('You may add a pawn!', 440, 650)
        textSize(35)
        text('Move ' + str(total) + ' step(s)', 500, 600)
        fill(216, 100, 96)
        if mouseX > 1080 and mouseX < 1180 and mouseY > 20 and mouseY < 70:  # highlight rule button
            rect(1080, 20, 100, 50)
        elif mouseX > 525 and mouseX < 675 and mouseY > 480 and mouseY < 550:  # highlight throw button
            rect(525, 480, 150, 70)
        elif mouseX > 540 and mouseX < 660 and mouseY > 250 and mouseY < 290:  # highlight plus card
            rect(540, 250, 120, 40)
        elif mouseX > 540 and mouseX < 660 and mouseY > 190 and mouseY < 230:  # higlight o card
            rect(540, 190, 120, 40)
        fill(255, 255, 255)
        textSize(22)
        text('O-Card', 560, 220)
        text('Plus-Card', 548, 275)
        text('Rules', 1100, 52)
        textSize(25)
        text('Throw', 560, 520)
    elif page == 2: #Rulepage functionality and layout
        background(bg)
        fill(216, 27, 96)
        rect(20, 20, 100, 50)  # back button page 2
        rect(480, 600, 100, 50)
        rect(620, 600, 100, 50)
        fill(216, 67, 96)
        if mouseX > 20 and mouseX < 120 and mouseY > 20 and mouseY < 70: #Back button
            rect(20, 20, 100, 50)
        elif mouseX > 480 and mouseX < 580 and mouseY > 600 and mouseY < 650: #Previous button
            rect(480, 600, 100, 50)
        elif mouseX > 620 and mouseX < 720 and mouseY > 600 and mouseY < 650: #Next button
            rect(620, 600, 100, 50)
        fill(255, 255, 255)
        textSize(22)
        text('Back', 45, 52)
        textSize(15)
        text('Previous\n   page', 500, 620)
        text('Next page', 635, 630)
        for s in range(1, 6): #The 'x' equals the cardpage number
            if s == x:
                image(Rule_book[s - 1], 200, 100)
                image(Rule_book[s], 600, 100)
            if x < 1:
                image(Rule_book[0], 200, 100)
                image(Rule_book[1], 600, 100)
                x = 1
            elif x > 5:
                image(Rule_book[4], 200, 100)
                image(Rule_book[5], 600, 100)
                x = 5
    elif page == 3: #Cardpage functionality and layout
        background(bg)
        image(cardBlank, 200, 250, width / 1.5, height / 2.3)
        image(logo, 535, 30)
        fill(216, 27, 96)
        rect(20, 20, 100, 50)  # back button page 2
        rect(1080, 20, 100, 50) # Rule button
        fill(255, 255, 255)
        rect(270, 300, 660, 195, 5)
        textSize(22)
        text('Back', 45, 52)
        text('Rules', 1100, 52)
        if mouseX > 20 and mouseX < 120 and mouseY > 20 and mouseY < 70: #Highlight back button
            fill(216, 67, 96)
            rect(20, 20, 100, 50)
            fill(255, 255, 255)
            text('Back', 45, 52)
        if mouseX > 1080 and mouseX <1180 and mouseY > 20 and mouseY < 70: #Highlight rules button
            fill(216, 67, 96)
            rect(1080, 20, 100, 50)
            fill(255, 255, 255)
            text('Rules', 1100, 52)
        fill(0, 0, 0)
        textSize(28)
        if card:
            text(o, 290, 380)
        else:
            text(plus, 290, 380)


def mousePressed():
    global x, page, card
    if mouseX > 525 and mouseX < 675 and mouseY > 480 and mouseY < 550 and page == 1: #Throw button with sound
        Dice_sound.trigger()
        random1()
    if mouseX > 1080 and mouseX < 1180 and mouseY > 20 and mouseY < 70 and page == 1 or page ==3: #Rules button
        x = 0
        page = 2
    if mouseX > 540 and mouseX < 660 and mouseY > 190 and mouseY < 230 and page == 1:  # o card button
        random_0_card()
        card = True
        page = 3
    if mouseX > 540 and mouseX < 660 and mouseY > 250 and mouseY < 290 and page == 1:  # pluscard button
        random_plus_card()
        card = False
        page = 3
    if mouseX > 20 and mouseX < 120 and mouseY > 20 and mouseY < 70 and (page == 2 or page == 3): #Back button
        page = 1
    if mouseX > 620 and mouseX < 720 and mouseY > 600 and mouseY < 650 and page == 2: #Next button rules
        x = x + 1
    if mouseX > 480 and mouseX < 580 and mouseY > 600 and mouseY < 650 and page == 2: #Previous button rules
        x = x - 1


def random_0_card(): #List of OCards and a random card generator
    global o
    oCards = ['Throw off any opponent pawn', 'Throw off any opponent pawn', 'Throw off 2 opponent pawns', 'Move a pawn from an opponent of choice\n 3 steps back', 'Move a pawn from an opponent of choice\n 2 steps back', 'Move a pawn from an opponent of choice\n 1 step back', 'Move a pawn from an opponent of choice\n 1 step back', 'Remove your pawn on the O tile', 'Remove your pawn on the O tile', 'Move a pawn from an opponent of choice\n 3 steps forward',
              'Move a pawn from an opponent of choice\n 2 steps forward', 'Move a pawn from an opponent of choice\n 1 step forward', 'Move a pawn from an opponent of choice\n 1 step forward', 'Go to the other O tile. Do not draw a card.', 'Go to the other O tile. Don’t draw a card.', 'Go to the other O tile. Do not draw a card.', 'All pawns on the board\n (including your own!) go off the board', 'All opponent players may place one pawn\n on the board', 'Let an opponent player draw a O card']
    o = random.randint(0, len(oCards) - 1)
    o = oCards[o]


def random_plus_card(): #List of PlusCards and a random card generator
    global plus
    plusCards = ['Add a new pawn on the board', 'Add a new pawn on the board', 'Add 2 new pawns on the board', 'Move any of your own pawns 3 steps forward', 'Move any of your own pawns 2 steps forward', 'Move any of your own pawns 1 step forward', 'Throw the dice again', 'Remove your pawn on the + tile', 'Remove any of your own pawns', 'Move any of your own pawns 3 steps back', 'Move any of your own pawns 2 steps back', 'Move any of your own pawns 1 step back',
                 'Move any of your own pawns 1 step back', 'Go to the other + tile. Do not draw a card.', 'Go to the other + tile. Do not draw a card.', 'Go to the other + tile. Do not draw a card.', 'Switch any of your pawns with any opponent pawn', 'Move one of your pawns back to the start', 'Let an opponent player draw a + card']
    plus = random.randint(0, len(plusCards) - 1)
    plus = plusCards[plus]


def setup():
    global bg, logo, page, x, Rule_book, Dice_sound, minim, cardBlank, pages
    size(1200, 675)
    random1()
    page = 1
    bg = loadImage("hoi.png")
    logo = loadImage('UR Logo - background.png')
    bg.resize(1200, 675)
    logo.resize(130, 110)
    Rule_book = [
        loadImage('Schermopname (73).png'),
        loadImage('Schermopname (74).png'),
        loadImage('Schermopname (75).png'),
        loadImage('Schermopname (76).png'),
        loadImage('Schermopname (77).png'),
        loadImage('Schermopname (79).png'),
    ]
    for p in Rule_book: p.resize(400, 475)
    cardBlank = loadImage("CardBlank.png")
    minim = Minim(this)
    Dice_sound = minim.loadSample("dicedwergen.nl.mp3")
    x = 0

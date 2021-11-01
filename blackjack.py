from sklearn import tree
import pandas as panduh
import util
import joblib
from tkinter import * 
from tkinter import messagebox
import time

# Initialize vars
dealerWins = 0
playerWins = 0
ties = 0
winrate = 0.00

deckDict = {}
deckDict['K'] = 10
deckDict['Q'] = 10
deckDict['J'] = 10
deckDict['1'] = 10
deckDict['9'] = 9
deckDict['8'] = 8
deckDict['7'] = 7
deckDict['6'] = 6
deckDict['5'] = 5
deckDict['4'] = 4
deckDict['3'] = 3
deckDict['2'] = 2
deckDict['A'] = 11

root = Tk()

# Get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# Calculate x and y coordinates for the Tk root window
x = (ws/2) - (1100/2)
y = (hs/2) - (600/2)

# Set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (1100, 600, x, y))
root.configure(bg='green')
root.title("BlackJack AI")

dir = './images/cardimages/'
images = [PhotoImage(file=dir + "card{}.gif".format(i)) for i in range(52)]
faceDownImage = PhotoImage(file=dir + "back-red.gif")
blankImage = PhotoImage(file=dir + "blank.gif")
print(str(dir + "back-red.gif"))

dealerImages = []
playerImages = []

txt = ""

dealerWinsLabel = Label(root, text = "Dealer Wins = " + str(dealerWins))
dealerWinsLabel.grid(row = 2, column = 0, padx = 0, pady = 10)
dealerWinsLabel.config(font=("Courier", 13))

playerWinsLabel = Label(root, text = "Player Wins = " + str(playerWins))
playerWinsLabel.grid(row = 3, column = 0, padx = 0, pady = 10)
playerWinsLabel.config(font=("Courier", 13))

tiesLabel = Label(root, text = "Ties = " + str(ties))
tiesLabel.grid(row = 4, column = 0, padx = 0, pady = 10)
tiesLabel.config(font=("Courier", 13))

winrateLabel = Label(root, text = "Winrate: " + str(winrate) + "%")
winrateLabel.grid(row = 5, column = 0, padx = 0, pady = 10)
winrateLabel.config(font=("Courier", 13))
        
while True:

    if dealerWins == 0 and playerWins == 0:
        txt = "Winrate: 0.00%"
        winrateLabel.configure(text = txt)
        util.update(root)
    elif dealerWins == 0 and playerWins != 0:
        txt = "Winrate: 100.00%"
        winrateLabel.configure(text = txt)
        util.update(root)
    else:
        winrate = (playerWins / (playerWins + dealerWins)) * 100
        txt = "Winrate: " + "%.2f" % winrate + "%"
        winrateLabel.configure(text = txt)
        util.update(root)

    util.new_game(root, blankImage, dealerImages, playerImages)
    util.update(root)
    time.sleep(1)

    # Deal cards
    dealerScore = 0
    playerScore = 0
    playerAces = 0
    dealerAces = 0
    dealerSlot = 0
    playerSlot = 0
    playerRow = 1
    dealerRow = 0
    hit = 0

    deckImages = util.create_deck_hash()
    deck = util.create_deck()
    util.random.shuffle(deck)

    dealerHand = []
    playerHand = []

    if deck[-1][0] == 'A':
            playerAces += 1
    playerHand.append(deck.pop())
    img = PhotoImage(file = dir + deckImages.get(playerHand[-1]))
    playerImages[playerSlot].configure(image=img)
    playerImages[playerSlot].image = img
    util.update(root)
    playerSlot += 1
    time.sleep(2)

    if deck[-1][0] == 'A':
            dealerAces += 1
    dealerHand.append(deck.pop())
    img = PhotoImage(file = dir + deckImages.get(dealerHand[-1]))
    dealerImages[dealerSlot].configure(image= img)
    dealerImages[dealerSlot].image = img
    util.update(root)
    dealerSlot += 1
    time.sleep(2)

    if deck[-1][0] == 'A':
            playerAces += 1
    playerHand.append(deck.pop())
    img = PhotoImage(file = dir + deckImages.get(playerHand[-1]))
    playerImages[playerSlot].configure(image= img)
    playerImages[playerSlot].image = img
    util.update(root)
    playerSlot += 1
    time.sleep(2)

    if deck[-1][0] == 'A':
            dealerAces += 1
    dealerHand.append(deck.pop()) # face down
    img = faceDownImage
    dealerImages[dealerSlot].configure(image= img)
    dealerImages[dealerSlot].image = img
    util.update(root)
    time.sleep(2)

    playerScore = util.getBestScore(playerHand, deckDict)
    dealerScore = util.getBestScore(dealerHand, deckDict)

    needToLog = False

    # Player turn
    if playerScore == 21:
        playerWins = playerWins + 1
        txt = "Player Wins = " + str(playerWins)
        playerWinsLabel.configure(text = txt)
        util.popupmsg("Player Wins!!", root)
        util.update(root)
        time.sleep(2)
    while True and playerScore != 21:
        hand = [playerScore, playerAces]
        hasHit = util.AIHit(hand)

        if hasHit:
            needToLog = False
            if deck[-1][0] == 'A':
                playerAces += 1
            playerHand.append(deck.pop())
            img = PhotoImage(file = dir + deckImages.get(playerHand[-1]))
            playerImages[playerSlot].configure(image=  img)
            playerImages[playerSlot].image = img
            print(playerHand[-1])
            util.update(root)
            time.sleep(2)
            playerSlot += 1
            needToLog = True
        else:
            needToLog = False
        if not (util.getBestScore(playerHand, deckDict) > 0 and util.getBestScore(playerHand, deckDict) < 21 and hasHit):
            break
        
    if needToLog:
        needToLog = False

    # If Player Bust
    if util.getBestScore(playerHand, deckDict) == 0:
        # Log data as loss
        
        dealerWins = dealerWins + 1
        txt = "Dealer Wins = " + str(dealerWins)
        dealerWinsLabel.configure(text = txt)
        util.popupmsg("Player Busted!!", root)
        util.update(root)
        print("Player BUSTED!")
        '''
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''
        continue # To next game of blackjack
        
    # Dealer turn 
    img = PhotoImage(file = dir + deckImages.get(dealerHand[-1]))
    dealerImages[dealerSlot].configure(image= img)
    dealerImages[dealerSlot].image = img
    dealerSlot += 1
    util.update(root)
    time.sleep(2)
    
    while util.getBestScore(dealerHand, deckDict) > 0 and util.getBestScore(dealerHand, deckDict) < 17:
        if deck[-1][0] == 'A':
            dealerAces += 1
        dealerHand.append(deck.pop())
        img = PhotoImage(file = dir + deckImages.get(dealerHand[-1]))
        dealerImages[dealerSlot].configure(image= img)
        dealerImages[dealerSlot].image = img
        util.update(root)
        time.sleep(2)
        dealerSlot += 1

    if util.getBestScore(dealerHand, deckDict) == util.getBestScore(playerHand, deckDict):
        
        # Log player loss
        ties = ties + 1
        txt = "Ties = " + str(ties)
        tiesLabel.configure(text = txt)
       
        util.popupmsg("Tie Game!!", root)
        util.update(root)
        print("TIE!!")
        time.sleep(2)
        '''
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''

    elif util.getBestScore(playerHand, deckDict) < util.getBestScore(dealerHand, deckDict):
        # Log player loss
        
        dealerWins = dealerWins + 1
        txt = " Dealer Wins = " + str(dealerWins)
        dealerWinsLabel.configure(text = txt)
        util.popupmsg("Dealer Wins!!", root)
        util.update(root)
        print("DEALER WIN!!")
        time.sleep(2)
        '''
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''


    elif util.getBestScore(playerHand, deckDict) > util.getBestScore(dealerHand, deckDict):
        
        playerWins = playerWins + 1
        txt = "Player Wins = " + str(playerWins)
        playerWinsLabel.configure(text = txt)
        util.popupmsg("Player Wins!!", root)
        util.update(root)
        print("PLAYER WIN!!")
        time.sleep(2)
        '''
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''


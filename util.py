import random
from tkinter import *
import joblib

def create_deck_hash():
    return {'2c':"card0.gif",'3c':"card1.gif",'4c':"card2.gif",'5c':"card3.gif",'6c':"card4.gif",'7c':"card5.gif",'8c':"card6.gif",'9c':"card7.gif",'10c':"card8.gif",'Jc':"card9.gif",'Qc':"card10.gif",'Kc':"card11.gif",'Ac':"card12.gif",               
            '2d':"card13.gif",'3d':"card14.gif",'4d':"card15.gif",'5d':"card16.gif",'6d':"card17.gif",'7d':"card18.gif",'8d':"card19.gif",'9d':"card20.gif",'10d':"card21.gif",'Jd':"card22.gif",'Qd':"card23.gif",'Kd':"card24.gif",'Ad':"card25.gif",     
            '2h':"card26.gif",'3h':"card27.gif",'4h':"card28.gif",'5h':"card29.gif",'6h':"card30.gif",'7h':"card31.gif",'8h':"card32.gif",'9h':"card33.gif",'10h':"card34.gif",'Jh':"card35.gif",'Qh':"card36.gif",'Kh':"card37.gif",'Ah':"card38.gif",     
            '2s':"card39.gif",'3s':"card40.gif",'4s':"card41.gif",'5s':"card42.gif",'6s':"card43.gif",'7s':"card44.gif",'8s':"card45.gif",'9s':"card46.gif",'10s':"card47.gif",'Js':"card48.gif",'Qs':"card49.gif",'Ks':"card50.gif",'As':"card51.gif"
            }
def create_deck():
    return ['2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','Ac',                                                                                                                                                                              
            '2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ad',                                                                                                                                                                              
            '2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ah',                                                                                                                                                                              
            '2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks','As'
            ]

def getBestScore(hand, deckDict):
    score = 0
    aces = 0

    for card in hand:
        score += deckDict[card[0]]
        if card[0] == 'A':
            aces += 1
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    
    if score > 21:
        score = 0

    return score

def randomHit():
    return random.choice([0,1])

def AIHit(hand):
    filename = 'model.sav'
    trained = joblib.load(filename)

    handHitInner = hand.copy()
    handStayInner = hand.copy()

    handHitInner.append(1)
    handStayInner.append(0)

    handHit = [handHitInner]
    handStay = [handStayInner]
    prob_hit = trained.predict_proba(handHit).reshape(1,-1)[0][1]
    prob_stay = trained.predict_proba(handStay).reshape(1,-1)[0][1]

    if prob_hit > prob_stay:
        return 1
    else:
        return 0

def update(root):
    root.update_idletasks()
    root.update()

def new_game(root, blankImage, dealerImages, playerImages):

    for i in range(9):
        dHand = Label(root, text = "Dealer's Hand")
        dHand.grid(row = 0, column = 0, padx = 0, pady = 10)
        dHand.config(font=("Courier", 13))
        pHand = Label(root, text = "Player's Hand")
        pHand.grid(row = 1, column = 0, padx = 0, pady = 10)
        pHand.config(font=("Courier", 13))

        dealerImages.append(Label(root))
        dealerImages[i].grid(row = 0, column = i + 1, padx = 10, pady = 10)
        dealerImages[i].configure(image=blankImage)

        playerImages.append(Label(root))
        playerImages[i].grid(row = 1, column = i + 1, padx = 10, pady = 10)
        playerImages[i].configure(image=blankImage)

def popupmsg(msg, root):
    
    popup = Toplevel()


    w = 100 # width for the Tk root
    h = 100 # height for the Tk root

    # Get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # Calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    popup.geometry("%dx%d+%d+%d" % (w, h, x, y))
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    update(popup)
    popup.wait_window()
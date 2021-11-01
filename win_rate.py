from sklearn import tree
import pandas as panduh
import util
import joblib

# Initialize vars
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

data = panduh.DataFrame(columns=['score', 'aces', 'hit', 'result'])

win = 0
loss = 0

for i in range(100000):
    print("Game number: " + str(i + 1))
    currentGame = panduh.DataFrame(columns=['score', 'aces', 'hit'])
    # Deal cards
    dealerScore = 0
    playerScore = 0
    playerAces = 0
    dealerAces = 0
    hit = 0

    deck = util.create_deck()
    util.random.shuffle(deck)

    dealerHand = []
    playerHand = []

    if deck[-1] == 'A':
            playerAces += 1
    playerHand.append(deck.pop())

    if deck[-1] == 'A':
            dealerAces += 1
    dealerHand.append(deck.pop())

    if deck[-1] == 'A':
            playerAces += 1
    playerHand.append(deck.pop())

    if deck[-1] == 'A':
            dealerAces += 1
    dealerHand.append(deck.pop()) # face down

    playerScore = util.getBestScore(playerHand, deckDict)
    dealerScore = util.getBestScore(dealerHand, deckDict)

    needToLog = False

    # Player turn
    if playerScore == 21:
        temp = panduh.DataFrame([[util.getBestScore(playerHand, deckDict), playerAces, 0]], columns=['score', 'aces', 'hit'])
        currentGame = currentGame.append(temp, ignore_index=True)
    while True and playerScore != 21:
        hand = [playerScore, playerAces]
        hasHit = util.AIHit(hand)
        if hasHit:
            temp = panduh.DataFrame([[util.getBestScore(playerHand, deckDict), playerAces, hasHit]], columns=['score', 'aces', 'hit'])
            currentGame = currentGame.append(temp, ignore_index=True)
            needToLog = False
            if deck[-1] == 'A':
                playerAces += 1
            playerHand.append(deck.pop())
            needToLog = True
        else:
            temp = panduh.DataFrame([[util.getBestScore(playerHand, deckDict), playerAces, hasHit]], columns=['score', 'aces', 'hit'])
            currentGame = currentGame.append(temp, ignore_index=True)
            needToLog = False
        if not (util.getBestScore(playerHand, deckDict) > 0 and util.getBestScore(playerHand, deckDict) < 21 and hasHit):
            break
        
    if needToLog:
        temp = panduh.DataFrame([[util.getBestScore(playerHand, deckDict), playerAces, hasHit]], columns=['score', 'aces', 'hit'])
        currentGame = currentGame.append(temp, ignore_index=True)
        needToLog = False

    # If Player Bust
    if util.getBestScore(playerHand, deckDict) == 0:

        # Log data as loss
        loss += 1
        currentGame['result'] = 0
        data = data.append(currentGame, ignore_index=True)

        '''
        print("Player BUSTED!")
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''
        continue # To next game of blackjack
        
    # Dealer turn
    while util.getBestScore(dealerHand, deckDict) > 0 and util.getBestScore(dealerHand, deckDict) < 17:
        if deck[-1] == 'A':
            dealerAces += 1
        dealerHand.append(deck.pop())

    if util.getBestScore(dealerHand, deckDict) == util.getBestScore(playerHand, deckDict):

        # Log player loss
        loss += 1
        currentGame['result'] = 0
        data = data.append(currentGame, ignore_index=True)
        '''
        print("TIE!!")
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''

    elif util.getBestScore(playerHand, deckDict) < util.getBestScore(dealerHand, deckDict):

        # Log player loss
        loss += 1
        currentGame['result'] = 0
        data = data.append(currentGame, ignore_index=True)
        '''
        print("DEALER WIN!!")
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''


    elif util.getBestScore(playerHand, deckDict) > util.getBestScore(dealerHand, deckDict):
        currentGame['result'] = 1
        win += 1
        data = data.append(currentGame, ignore_index=True)
        '''
        print("PLAYER WIN!!")
        print("Dealer: ")
        print(dealerHand)
        print("Player: ")
        print(playerHand)
        '''


print(str(win + loss) + " games played!")
print("Win rate: " + str(win / (win + loss)))
print("win" + str(win))
print("loss" + str(loss))
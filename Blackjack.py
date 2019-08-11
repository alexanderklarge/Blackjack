#My blackjack code!

#Probably the best way to do it is to have a dictionary from 1 - 14
#with 11 being ace, 12 being Jack, 13 being Queen, 14 being King

#General plan:
    # Give player two cards
    # Have 4 of each card, so if player or dealer gets one, they have less chance of getting same
    # Have "hit/stick" ability 
    # GIVE USER CHOICE OF HAVING ACE BE 1 OR 11!
    
#To do
    # Add dealer functionality (currently just the player)
    
#Advanced features
    # Have ability to bet!
    # Add suits (do they matter? Just to ensure you aren't getting 2 x King of Hearts?)
  
import numpy as np
    
deck = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,
        8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J',
        'Q','Q','Q','Q','K','K','K','K']

card1_index = np.random.randint(52)
card2_index = np.random.randint(52)  
    #TO DO - MAKE SURE CARD 2 CAN'T BE THE SAME AS CARD 1

#print('The randomly generated index for card 1 is {}'.format(card1_index))
#print('The randomly generated index for card 2 is {}'.format(card2_index))

card1 = deck[card1_index]
card2 = deck[card2_index]

print('First card is a {}'.format(card1))
print('Second card is a {}'.format(card2))

##ASSIGNING CARD 1 VALUE
#If the card is 2-10, can just assign it's value to 2-10 in an easy way
if card1 in range(2,11):
    card1_value = card1
#If card is Ace, assign value to 11
if card1 == 'A':
    card1_value = 11
#this would be a great place to have a user input (would you like ace to be 11 or 1)
if card1 in ['J','Q','K']:
    card1_value = 10

##ASSIGNING CARD 2 VALUE 
if card2 in range(2,11):
    card2_value = card2
#If card is Ace, assign value to 11
if card2 == 'A':
    card2_value = 11
#this would be a great place to have a user input (would you like ace to be 11 or 1)
if card2 in ['J','Q','K']:
    card2_value = 10

##VALUE OF YOUR HAND 
hand_value = card1_value + card2_value
print('The value of your hand is {}'.format(hand_value))


#HIT OR STICK 
print('Hit, or stick?')
user_input = input()

if user_input in ['hit','Hit','HIT']:
    print('Ok partner, third card coming up')
    card3_index = np.random.randint(52) 
    card3 = deck[card3_index]
    print('Third card is a {}'.format(card3))
    
    ##ASSIGNING CARD 3 VALUE 
    if card3 in range(2,11):
        card3_value = card3
    #If card is Ace, assign value to 11
    if card3 == 'A':
        card3_value = 11
        #this would be a great place to have a user input (would you like ace to be 11 or 1)
    if card3 in ['J','Q','K']:
        card3_value = 10
        
    hand_value += card3_value
    print('The value of your hand is now {}'.format(hand_value))
    if hand_value >21:
        print('Bust! Too bad.')

elif user_input in ['Stick','stick','STICK']:
    print('Stick, got it')

#Just testing if I have PyCharm set up right, delete me
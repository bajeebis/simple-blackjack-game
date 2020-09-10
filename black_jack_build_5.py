from random import choice
import sys
from time import sleep

per_deck = ['ace', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', 'jack', 'king', 'queen']

# Empty Decks (Lists) below
spade_suits = [] ; hearts_suits = [] ; clubs_suits = [] ; diamonds_suits = []
players_hands = [] ; dealers_hands = []


for card in per_deck:
    spade_suits.append(card + ' of spades')
    hearts_suits.append(card + ' of hearts')
    clubs_suits.append(card + ' of clubs')
    diamonds_suits.append(card + ' of diamonds')

full_deck = spade_suits + hearts_suits + clubs_suits + diamonds_suits
the_deck = full_deck[:]


def get_card_value(x):
    if 'ace' in x:
        return 0
    if '10' in x or 'jack' in x or 'king' in x or 'queen' in x:
        return 10
    if '9' in x:
        return 9
    if '8' in x:
        return 8
    if '7' in x:
        return 7
    if '6' in x:
        return 6
    if '5' in x:
        return 5
    if '4' in x:
        return 4
    if '3' in x:
        return 3
    if '2' in x:
        return 2
    if '1' in x:
        return 1


def pick_card(deck, answer=False):
    """Picks a random card and removes it from the_deck."""
    card_1 = choice(the_deck)
    deck.append(card_1)
    the_deck.remove(card_1)
    if answer:
        show_cards(deck)
        return deck
    else:
        return deck


def show_cards(deck):
    for card in deck:
        sys.stdout.write(f"\t{card}")
        sys.stdout.flush()
        sleep(1.5)


def get_deck_value(deck):
    x = 0
    for card in deck:
        x += get_card_value(card)
    return x


def ace_check(deck):
    if any('ace' in i for i in deck):
        return True
    else:
        return False


def player_vs_dealer():
    player = players_value()
    dealer = dealers_value()
    if dealer == player and dealer <= 21 and player <= 21:
        print("Your hands:")
        show_cards(players_hands)
        print(f"\nDealers hands:")
        show_cards(dealers_hands)
        print("\n\tIt's a tie!")
        reset_decks()
    if player > dealer and dealer <= 21 and player <= 21:
        print("Your hands:")
        show_cards(players_hands)
        print(f"\nDealers hands:")
        show_cards(dealers_hands)
        print(f"\n\tPlayer wins!")
        reset_decks()
    if dealer > player and dealer <= 21 and player <= 21:
        print("Your hands:")
        show_cards(players_hands)
        print(f"\nDealers hands:")
        show_cards(dealers_hands)
        print("\n\tDealer wins the round!")
        reset_decks()
    if player > 21 and dealer < 21:
        print("You lose, you went over 21!")
        reset_decks()
    if dealer > 21 and player <= 21:
        print("You win!")
        reset_decks()

def players_value():
    deck = players_hands
    x = get_deck_value(deck)
    ac_p = ace_check(deck)
    if ac_p and x < 11:
        x += 11
        return x
    elif ac_p and x > 11:
        x += 1
        return x
    else:
        return x

def dealers_value():
    deck = dealers_hands
    x = get_deck_value(deck)
    ac_d = ace_check(deck)
    if ac_d:
        x += 11
        return x
    else:
        return x


def reset_decks():
    while players_hands:
        x = players_hands.pop()
        the_deck.append(x)
    while dealers_hands:
        x = dealers_hands.pop()
        the_deck.append(x)


def start_round():
    flag = True
    while flag:
        print("\n\nLet's play BlackJack!")
        answer_1 = input("Wanna play? (Y|N)\n")
        if answer_1.casefold() == "y":
            print("\n\nYour first card pick:")
            pick_card(players_hands, True)
            print("\nThe dealer's first hand:")
            pick_card(dealers_hands, True)
            print("\nYour 2nd card:")
            pick_card(players_hands, True)
            pick_card(dealers_hands)
            print("\n(The dealer has now picked the wild card)")
            ac_d = ace_check(dealers_hands)
            if ac_d:
                print("\t*Dealer has ace*")
                show_cards(dealers_hands)
            answer_2 = input("\nDo you hit or stand? (stand|hit)\n")
            if answer_2.casefold() == 'hit':
                flag_3 = True
                while flag_3:
                    if players_value() > 21:
                        print("\nYou have more than 21 cards, you lose.")
                        print("\nThe dealer's hand:")
                        show_cards(dealers_hands)
                        reset_decks()
                        start_round()
                    if players_value() < 21:
                        pick_card(players_hands, True)
                        if players_value() > 21:
                            print("\nYou lose mate!")
                            print("\nDealer's hands:")
                            show_cards(dealers_hands)
                            reset_decks()
                            start_round()
                    answer_3 = input("\nHit or stand? (stand|hit)\n")
                    if answer_3 == "hit":
                        continue
                    elif answer_3 == "stand":
                        flag_3 = False
                    else:
                        continue
                player_vs_dealer()
            elif answer_2.casefold() == 'stand':
                player_vs_dealer()
            else:
            # While on the part "do you hit or stand",
            #   program goes back to the start
                continue
        elif answer_1.casefold() == 'n':
            flag = False
        else:
            continue


start_round()
# Notes:
#   - goes over 21, it's bad
#   -

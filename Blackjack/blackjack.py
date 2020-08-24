from random import shuffle
from os import system
from time import sleep

class Blackjack(object):
    suits = ("♥", "♠", "♦", "♣")
    card_names = ("6", "7", "8", "9", "10", "jack", "queen", "king", "ace")
    cards = []
    weight = {
        
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "jack":10,
        "queen":10,
        "king":10,
        "ace":1,
        
        }

    def create_cards(self) -> None:
        for i in range(0, len(self.suits)):
            for j in range(0, len(self.card_names)):
                self.cards.append(self.suits[i]+" "+self.card_names[j])
        shuffle(self.cards)

    def give_cards(self, cards_amount):
        given_cards = []
        for i in range(0, cards_amount):
            given_cards.append(self.cards[i])
            self.cards.remove(self.cards[i])
        return given_cards

    def compare(self, first_user, second_user) -> None:
        if first_user.score() > second_user.score():
            print(first_user.name+" WINS with the score of "+str(first_user.score())+"!")
        elif second_user.score() > first_user.score():
            print(second_user.name+" WINS with the score of "+str(second_user.score())+"!") 
        else:
            print("Draw! We have a two winners here!")

class User(object):

    def receive_cards(self, given_cards) -> None:
        for i in range(0, len(given_cards)):
            self.cards.append(given_cards[i])

    def __init__(self, given_cards, cards, name="Computer"):
        self.cards = cards
        self.receive_cards(given_cards)
        self.name = name
    def score(self) -> None:
        score_card_names = []
        total_score = 0
        
        for i in range(0, len(self.cards)):
            card_string = str.split(self.cards[i], " ") 
            score_card_names.append(card_string[1])
        
        for i in range(0, len(score_card_names)):
            card_score = int(Blackjack().weight.get(score_card_names[i]))        
            total_score += card_score
        
        return total_score

username = input("Please, enter your name: ")

blackjack_game = Blackjack()
blackjack_game.create_cards()

user = User(blackjack_game.give_cards(1), [], username)
computer = User(blackjack_game.give_cards(1), [])

print(user.name+"'s cards "+str(user.cards))
print(computer.name+"'s cards "+str(computer.cards))

game_process = True
hold_checker = False

while game_process == True:

    system("cls")

    print("You have a such cards: ")
    for i in range(0, len(user.cards)):
        print(user.cards[i], sep=", ")
    score = user.score()
    print("Your score is "+str(score))
    if score <= 21:
        if hold_checker == False:
            print("What you want to do?")
            print("[1] Hit")
            print("[2] Hold")
            action = int(input("Choose the number of action: "))
            if action == 1:
                user.receive_cards(blackjack_game.give_cards(1))
                print("One card has been received!")
                continue            
            if action == 2:
                hold_checker = True
                if computer.score() >= 18 and computer.score() <= 21:
                    blackjack_game.compare(user, computer)
                    game_process = False
                    exit(0)
                elif computer.score() > 21:
                    print(computer.name+" is busted! "+user.name+" WINS with the score of "+str(user.score())+"!")
                    exit(0)
                elif computer.score() < 18:
                    computer.receive_cards(blackjack_game.give_cards(1))
                    print(computer.name+" receives 1 card!")
                    sleep(1.5)
        else:
                if computer.score() >= 18 and computer.score() <= 21:
                    blackjack_game.compare(user, computer)
                    game_process = False
                    exit(0)
                elif computer.score() > 21:
                    print(computer.name+" is busted! "+user.name+" WINS with the score of "+str(user.score())+"!")
                    exit(0)
                elif computer.score() < 18:
                    computer.receive_cards(blackjack_game.give_cards(1))
                    print(computer.name+" receives 1 card!")
                    sleep(1.5)
    else:
        print("Busted! "+computer.name+" WINS!")
        game_process = False
        exit(0)
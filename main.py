import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def calculate_score(player_cards):
    score = sum(player_cards)
    if len(player_cards) == 2 and score == 21:
        return 0
    if 11 in player_cards and score > 21:
        player_cards.remove(11)
        player_cards.append(1)

    return sum(player_cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def show_score(current_score):
    if current_score == 0:
        return "Blackjack"
    return current_score

def play_blackjack():
    players = {'player': [], 'dealer': []}
    print(art.logo)
    for player in players:
        for _ in range(2):
            players[player].append(deal_card())
    game_over = False
    while not game_over:
        score = calculate_score(players["player"])
        player_cards = players["player"]
        print(f"Your cards {player_cards} score: {show_score(score)}")

        dealer_cards = players["dealer"]
        print(f"Dealer's first card: {dealer_cards[0]}")

        hit = input("Do you want to draw a card? (y/n): ") == 'y'
        if not hit:
            game_over = True
            score = calculate_score(players["dealer"])
            while score != 0 and score < 17:
                players["dealer"].append(deal_card())
                score = calculate_score(players["dealer"])
        else:
            players["player"].append(deal_card())
            card = players["player"][-1]
            score = calculate_score(players["player"])
            print(f"You got a {card}. Your score: {score}")

            if score == 0:
                print("Blackjack!!!")
                game_over = True
            if score > 21:
                print("Busted!!!")
                game_over = True

    user_cards = players["player"]
    user_score = calculate_score(players["player"])

    computer_cards = players["dealer"]
    computer_score = calculate_score(players["dealer"])

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? (y/n): ") == "y":
    print("\n" * 20)
    play_blackjack()
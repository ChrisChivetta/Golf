import round

#Initalization
name = 'SeattleCrew'
number_people = 5
number_of_decks = 2
is_dealer_random = 1
cost_penalty = 50
number_of_rounds = 9
number_of_jokers = 2

DummyRound = round.Round(name, number_people, number_of_decks, is_dealer_random, cost_penalty, number_of_rounds, number_of_jokers)

##print(DummyRound.printSeatsInfo())

#Let's update Player Name

Player1 = 'Anika'
Player2 = 'Mo'
Player3 = 'Alex'
Player4 = 'Chris'
Player5 = 'Julia'

DummyRound.ConfirmSeat(Player1)
DummyRound.ConfirmSeat(Player2)
DummyRound.ConfirmSeat(Player3)
DummyRound.ConfirmSeat(Player4)
DummyRound.ConfirmSeat(Player5)
DummyRound.ConfirmSeat('Betty')

print(DummyRound.seats_info[1])
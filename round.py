
import uuid
from seat import Seat

class Round:
    
    def __init__(self, round_input_name, num_players, num_decks, dealer_type, penalty, num_rounds, num_jokers):
        self.name = round_input_name
        self.UUID = uuid.uuid4()
        self.num_players = num_players
        self.num_decks = num_decks
        self.dealer_type = dealer_type
        self.penalty = penalty
        self.num_rounds = num_rounds
        self.num_jokers = num_jokers
        self.seats_info = {}
        self.round_full = False

        for i in range(num_players):
            self.seats_info[i+1] = Seat(i+1)

    def ConfirmSeat(self, new_playername):
        for i in self.seats_info:
            if self.seats_info[i].player_name is None:
                self.seats_info[i].player_name = new_playername
                print("Assigning " + new_playername + " at " + str(i) + " position")
                break
            else:
                pass

    def printSeatsInfo(self):
        return self.seats_info

    def printRoundInfo(self):
        return print(self.name, self.UUID, self.num_players, self.num_decks, self.dealer_type, self.penalty, self.num_rounds, self.num_jokers)

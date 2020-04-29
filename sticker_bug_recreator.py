from sticker import Sticker

class WebStickerGame():

    def __init__(self, number_of_rounds):
        self.number_of_rounds = int(number_of_rounds)
        self.current_round = 1
        self.lukas_sticker = Sticker()
        [self.lukas_sticker.new_game() for round in range(self.number_of_rounds)]

    def remove_cards(self, row_number, number_of_cards):
        current_game = self.lukas_sticker.igre[self.current_round - 1]

        print('---------------------------BEFORE-------------------------')
        [print(f'This is game {dict_key} and this is its position: {self.lukas_sticker.igre[dict_key].position}. This is its class mark: {self.lukas_sticker.igre[dict_key]}') for dict_key in self.lukas_sticker.igre.keys()]
        print(f'I will execute a move command on igra {current_game} with data.')

        move_message = current_game.move(row_number, number_of_cards) 

        print('---------------------------AFTER---------------------------')
        print(f'This was the move_message: {move_message}.')
        [print(f'This is game {dict_key} and this is its position: {self.lukas_sticker.igre[dict_key].position}. This is its class mark: {self.lukas_sticker.igre[dict_key]}') for dict_key in self.lukas_sticker.igre.keys()]


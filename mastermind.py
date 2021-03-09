# Michelle McFarland
# CS 325, Winter 2021
# Portfolio Project - Mastermind

import random as rdm


class Game:
    def __init__(self):
        """Initializes a new game of Mastermind with a random pattern of four colors (repeats allowed)"""
        self.color_options = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        self.correct_pattern = []
        self.num_guesses = 0

        # chooses the four colors in the correct pattern (to be guessed)
        for i in range(4):
            color_pick = self.color_options[rdm.randint(0, 5)]
            self.correct_pattern.append(color_pick)

        # show rules at the start of a new game
        print("Let's play Mastermind!")
        print("Your goal is to guess a sequence of four colors, in the correct order.")
        print("There are six color options to choose from, and repeats are allowed.")
        print("You must guess correctly within eight guesses to win, and you will receive feedback after each guess.")
        print("Good luck!")
        print()

    def make_guesses(self):
        # player makes guesses until they win or they reach 8 guesses (lose)
        while self.num_guesses < 8:
            # increments guess counter
            self.num_guesses += 1

            # instructions for guess input
            print("Make a guess below. This is guess number " + str(self.num_guesses) + " out of 8.")
            print("Choose four colors in the correct order.")
            print("Color options are red, orange, yellow, green, blue, and purple.")

            # guess input
            guess = []

            for i in range(4):
                color_guess = input("Color choice " + str(i+1) + ": ").lower()
                guess.append(color_guess)

            # print their full guess
            print("Your guess is:", guess[0], guess[1], guess[2], guess[3])
            print()

            # check the solution and give feedback
            self.check_solution(guess)

    def check_solution(self, guess):
        # create a copy of the correct pattern to avoid issues with feedback about repeated colors
        solution = self.correct_pattern.copy()

        # create a dictionary for feedback pegs
        feedback = {
            'black': 0,
            'white': 0
        }

        # iterate through guess and correct pattern, compare and assign feedback pegs accordingly
        for i in range(4):
            # color is a complete match (color and position)
            if guess[i] == self.correct_pattern[i]:
                if guess[i] in solution:
                    solution.remove(guess[i])
                feedback['black'] += 1
            # color is a partial match (color is correct but position is incorrect)
            elif guess[i] in solution:
                if guess[i] in solution:
                    solution.remove(guess[i])
                feedback['white'] += 1

        # print feedback summary for the player
        print("Here is your feedback. Each black peg represents correct color and position. Each white peg represents a correct color that is in an incorrect position.")
        print("Black: ", feedback['black'])
        print("White: ", feedback['white'])
        print()

        # check if they have won the game, end game if so
        if feedback['black'] == 4:
            print("Solved!")
            self.num_guesses = 8

        elif self.num_guesses == 8:
            # out of guesses, lost game message
            print("No more guesses left! Better luck next time.")
            print("The correct pattern was:", self.correct_pattern[0], self.correct_pattern[1], self.correct_pattern[2],
                  self.correct_pattern[3])

        else:
            print("Not solved yet!")
            print()

            # reset feedback for next guess
            feedback['black'] = 0
            feedback['white'] = 0


def main():
    continue_playing = True
    while continue_playing is True:
        # option for testing mode (solution visible)
        testing_mode = input("Would you like to be shown the correct pattern prior to guessing? (for testing purposes) Enter Y or N: ")

        # start a new game
        gm = Game()

        # if testing mode was chosen, show correct solution
        if testing_mode == 'Y':
            print("The correct pattern is:", gm.correct_pattern[0], gm.correct_pattern[1], gm.correct_pattern[2], gm.correct_pattern[3])
            print()

        # player makes guesses and receives feedback until win or loss
        gm.make_guesses()

        # ask them if they would like to continue playing
        continue_choice = input("Would you like to play again? Enter Y or N: ")
        if continue_choice == 'N':
            continue_playing = False
            print("Thanks for playing!")


main()
from playwright.sync_api import sync_playwright
from .data_splitting import Data
from .wordle_solver import Solver
import time

GRAY = "rgb(58, 58, 60)"
YELLOW = "rgb(181,159,59)"
GREEN = "rgb(83,141,78)"

with sync_playwright() as p:

    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    actual_answer = {"word": None}

    def handle_dialog(dialog):
        message = dialog.message

        if "The word was " in message:
            actual_answer["word"] = (
                message.split("The word was ",1)[1].rstrip(".")
            )
        dialog.dismiss()


    page.on("dialog",handle_dialog)

    page.goto("http://localhost:8000/front_page.html")

    page.wait_for_timeout(2000)

    games_to_run = int(input("Enter amount of Games to Run: \n"))

    total_wins = 0
    total_games = 0

    total_guesses = 0
    total_compute_time = 0


    while total_games < games_to_run:

        actual_answer["word"] = None

        solver = Solver()
        #Change the Boolean values to help debug or display the graph at the end of the game
        solver.data.initialize(Debug =False, graphing = True)
        row  = 0
        total_games += 1
        game_compute_time = 0

        while not solver.game_over:
            guess  = solver.word_choice()

            page.keyboard.type(guess,delay =250)
            page.keyboard.press("Enter")

            page.wait_for_timeout(1500)

            squares = page.locator(".square")

            start = row * 5
            end = start + 5


            styles = []

            for i in range(start,end):

                square = squares.nth(i)
                styles.append(square.get_attribute("style"))


            solver.scoring(styles)

            if solver.game_over:

                total_guesses += solver.guess_count
                total_compute_time += game_compute_time

                if solver.win:
                    total_wins += 1
                else:
                    print("SOLVER LOST")
                    print(f"ACTUAL ANSWER: {actual_answer["word"]}")
                break

            start_compute = time.perf_counter()
            solver.word_filter()
            solver.IG_scoring()
            end_compute = time.perf_counter()

            game_compute_time += (end_compute - start_compute)

            row +=1


        page.reload()
        page.wait_for_timeout(1500)


width = 30
win_rate = f"{total_wins}/{games_to_run}"
percent = f"{(total_wins / games_to_run) * 100:.2f}%"
average_guesses = total_guesses / total_games
average_compute_time = total_compute_time / total_games

print(f"┌{'-'* width}┐")
print("|" + f"TOTAL WIN RATE: {win_rate}".center(width)+ "|")
print("|" + f"Percentage Rate: {percent}".center(width) + "|")
print("|" + f"Average Guesses: {average_guesses:.2f}".center(width) + "|")
print("|" + f"Average Compute Time: {average_compute_time:.4f}s".center(width) + "|")

print(f"└{'-'* width}┘\n")




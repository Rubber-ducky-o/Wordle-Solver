from playwright.sync_api import sync_playwright
from .data_splitting import Data
from .wordle_solver import Solver

GRAY = "rgb(58, 58, 60)"
YELLOW = "rgb(181,159,59)"
GREEN = "rgb(83,141,78)"

with sync_playwright() as p:

    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.on("dialog",lambda dialog:dialog.dismiss())

    page.goto("http://localhost:8000/front_page.html")

    page.wait_for_timeout(2000)

    games_to_run = int(input("Enter amount of Games to Run: \n"))

    total_wins = 0
    total_games = 0

    while total_games < games_to_run:

        solver = Solver()
        solver.data.initialize(Debug =True, graphing = False)
        row  = 0
        total_games += 1


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

                if solver.win:
                    total_wins += 1

                break


            solver.word_filter()
            solver.IG_scoring()

            row +=1


        page.reload()
        page.wait_for_timeout(1500)


width = 30
win_rate = f"{total_wins}/{games_to_run}"
percent = f"{(total_wins / games_to_run) * 100:.2f}%"

print(f"┌{'-'* width}┐")
print("|" + f"TOTAL WIN RATE: {win_rate}".center(width)+ "|")
print("|" + f"Percentage Rate: {percent}".center(width) + "|")
print(f"└{'-'* width}┘\n")




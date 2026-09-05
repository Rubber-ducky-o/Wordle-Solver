from playwright.sync_api import sync_playwright
from data_splitting import Data
from wordle_solver import Solver

GRAY = "rgb(58, 58, 60)"
YELLOW = "rgb(181,159,59)"
GREEN = "rgb(83,141,78)"

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.on("dialog",lambda dialog:dialog.dismiss())

    page.goto("http://localhost:8000/front_page.html")

    page.wait_for_timeout(2000)

    total_wins = 0
    total_games = 0

    while total_games < 100:
        solver = Solver()
        solver.data.initialize(Debug = True)
        row  = 0
        total_games += 1
        while row < 6:
            guess  = solver.word_choice()

            page.keyboard.type(guess,delay =250)
            page.keyboard.press("Enter")

            page.wait_for_timeout(1500)

            squares = page.locator(".square")

            score = ""

            start = row * 5
            end = start + 5

            print("GUESS:", guess)
            print("ROW:", row)
            print("START:", start)
            print("END:", end)

            styles = []

            for i in range(start,end):

                square = squares.nth(i)
                print(
                        i,
                        square.inner_text(),
                        square.get_attribute("style")
                    )


                styles.append(square.get_attribute("style"))



            solver.scoring(styles)
            print("WIN STATUS:",solver.win)

            if solver.win:
                total_wins +=1
                break

            solver.word_filter()
            solver.IG_scoring()

            row +=1


        page.reload()
        page.wait_for_timeout(1500)

print(f"TOTAL WIN RATE {total_wins} / 100")



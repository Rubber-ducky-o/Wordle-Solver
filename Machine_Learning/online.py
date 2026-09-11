from playwright.sync_api import sync_playwright
from .data_splitting import Data
from .wordle_solver import Solver
import time


with sync_playwright() as p:

    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://www.nytimes.com/games/wordle/index.html")

    page.get_by_role("button",name ="Play").click()

    page.wait_for_timeout(5000)

    ad = page.locator("#instl-slug")

    if ad.count() > 0 and ad.is_visible():
        continue_button = page.get_by_role("button",name = "Continue to Wordle")

        if continue_button.count() > 0:
            continue_button.click()


    page.wait_for_timeout(2000)

    close_button = page.get_by_test_id("icon-close")

    if close_button.count() > 0 and close_button.first.is_visible():
        close_button.first.click()


    page.wait_for_timeout(1000)

    solver = Solver()
    solver.data.initialize()

    row  = 0
    game_compute_time = 0


    while not solver.game_over:


        tiles = page.locator('[class^="Board-"] [data-testid="tile"]')

        start = row * 5
        end = start + 5

        page.locator("body").click()
        page.wait_for_timeout(200)
        guess  = solver.word_choice()
        print("GUESS:", guess)

        page.keyboard.type(guess,delay =250)
        page.wait_for_timeout(300)
        typed_states = [tiles.nth(i).get_attribute("data-state") for i in range(start,end)]



        page.keyboard.press("Enter")

        valid_states = {"absent","present","correct"}

        wait = time.perf_counter()

        while True:
            states = []
            animations = []

            for i in range(start,end):

                tile = tiles.nth(i)
                state = tile.get_attribute("data-state")
                animation = tile.get_attribute("data-animation")
                states.append(state)
                animations.append(animation)
            states_done = all(state in valid_states for state in states)

            animations_done = all(animation == "idle" for animation in animations)

            if states_done and animations_done:
                break

            if time.perf_counter() - wait > 10:
                raise TimeoutError(f"Tiles did not finish updating {states}")

            page.wait_for_timeout(100)

        solver.scoring(states)


        if solver.game_over:
            break

        start_compute = time.perf_counter()
        solver.word_filter()
        solver.IG_scoring()
        end_compute = time.perf_counter()

        game_compute_time += (end_compute - start_compute)

        row +=1
        page.wait_for_timeout(300)

    width = 35

    print(f"┌{'-'* width}┐")
    print("|" + f"Solver Compute Time: {game_compute_time:.4f}".center(width) + "|")
    print(f"└{'-'* width}┘\n")


    browser.close()




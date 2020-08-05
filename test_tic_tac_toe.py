import pytest, time, logging, random
import utils as util
from selenium.webdriver.common.keys import Keys

def test_tic_tac_toe(setup):
    buttons = setup["driver"].find_elements_by_class_name("square")
    number_of_games = int(setup["number_of_games"])
    new_game_button = setup["driver"].find_element_by_class_name("button.button--new-game")
    game_number = 1

    while number_of_games >= game_number:
        if util.tai_checker(setup, buttons, new_game_button, game_number):
            util.screenshot(setup, game_number)
            game_number += 1
            continue

        button_number = random.randint(0, 8)
        if util.slot_checker(buttons, button_number):
            continue

        util.choose_slot(buttons, button_number)
        if util.winner_checker(setup, new_game_button ,game_number):
            util.screenshot(setup, game_number)
            game_number += 1
            continue

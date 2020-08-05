import pytest,time
import logging, random
import utils as util
from selenium.webdriver.common.keys import Keys


def test_tic_tac_toe(setup_driver):
    buttons = setup_driver.find_elements_by_class_name("square")
    while True:
        if util.check_end_of_game(buttons):
            logging.info(f"The game end, No winner!!!")

        button_number = random.randint(0, 8)
        if util.check_button(buttons, button_number) != '':
            logging.info(f"The button you choose {button_number} not empty, please try again! ")
            continue

        buttons[button_number].send_keys(Keys.RETURN)
        logging.info(f"The button you choose {button_number}")

        if util.check_the_winner(buttons)== 'X':
            logging.info(f"The 'X' player is the winner!!!")
            break
        elif util.check_the_winner(buttons)== 'O':
            logging.info(f"The 'O' player is the winner!!!")
            break




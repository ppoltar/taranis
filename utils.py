import logging
from selenium.webdriver.common.keys import Keys

def screenshot(setup, game_number):
    setup["driver"].save_screenshot(f"game{game_number}.png")

def choose_slot(buttons, button_number):
    buttons[button_number].send_keys(Keys.RETURN)
    logging.info(f"The slot you choose {button_number}")

def slot_checker(buttons,  button_number):
    if buttons[button_number].text != '':
        logging.info(f"The slot you choose {button_number} not empty, please try again! ")

def start_new_game(new_game_button, game_number):
    logging.info(f"------> Finishing game number {game_number}")
    new_game_button.send_keys(Keys.RETURN)

def tai_checker(setup, buttons, new_game_button, game_number):
    for i in range(0, 8):
        if buttons[i].text != '':
            continue
        else:
            return False
    logging.info(f"The game end, No winner!!!")
    start_new_game(new_game_button, game_number)
    return True

def winner_checker(setup, new_game_button, game_number):
    game_info = setup["driver"].find_element_by_class_name("game-info").text.split("\n")[0]
    if "Winner" in game_info:
        logging.info(f"The {game_info}!!!")
        start_new_game(new_game_button, game_number)
        game_number += 1
        return True
    return False


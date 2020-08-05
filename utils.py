
def check_button(buttons, num):
    return buttons[num].text

def check_end_of_game(buttons):
    for i in range(0, 8):
        if buttons[i].text != '':
            continue
        else:
            return False
    return True


def check_the_winner(buttons):
    # row
    if buttons[0].text =='X' and buttons[1].text == 'X' and buttons[2].text == 'X'  or buttons[3].text == 'X' and buttons[4].text == 'X' and buttons[5].text == 'X' or buttons[6].text == 'X' and buttons[7].text == 'X' and buttons[8].text == 'X':
        return 'X'
    elif buttons[0].text == 'O' and buttons[1].text == 'O' and buttons[2].text == 'O' or buttons[3].text == 'O' and buttons[4].text == 'O' and buttons[5].text == 'O' or buttons[6].text == 'O' and buttons[7].text == 'O' and buttons[8].text == 'O':
        return 'O'

    # colunm
    if buttons[0].text == 'X' and buttons[3].text == 'X' and buttons[6].text == 'X' or buttons[1].text == 'X' and buttons[4].text == 'X' and buttons[7].text == 'X' or buttons[2].text == 'X' and buttons[5].text == 'X' and buttons[8].text == 'X':
        return 'X'
    elif buttons[0].text == 'O' and buttons[3].text == 'O' and buttons[6].text == 'O'      or buttons[1].text == 'O' and buttons[4].text == 'O' and buttons[7].text == 'O' or buttons[2].text == 'O' and buttons[5].text == 'O' and buttons[8].text == 'O':
        return'O'

    # slant
    if buttons[0].text == 'X' and buttons[4].text == 'X' and buttons[8].text == 'X' or buttons[2].text == 'X' and buttons[4].text == 'X' and buttons[6].text == 'X':
        return 'X'
    elif  buttons[0].text == 'O' and buttons[4].text == 'O' and buttons[8].text == 'O 'or buttons[2].text == 'O' and buttons[4].text == 'O' and buttons[6].text == 'O':
        return'O'

    else:
        return False



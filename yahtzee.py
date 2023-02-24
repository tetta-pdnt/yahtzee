# Yahtzee
import random
import time
import sys
import keyboard
import os

WIDTH = 19


def roll_dice(category_dict, left, hands):

    def delay_print(hand_list, save_list, is_slow, category_dict, left):

        print('-'*WIDTH)
        print('<->: move\nSpace: save dice\nr: reroll\nEnter: select hand\n' + '-'*WIDTH)
        for k, v in category_dict.items():
            result = '' if v[2] else v[0]
            print(f'{k}: {result}')
        print('-'*WIDTH)
        print(f'{left} left' + '\n' + '-'*WIDTH)
        if left == 3:
            print('Press "r" to roll the dice.', end='')
            while True:
                if keyboard.is_pressed('r'):
                    break
            left -= 1
            sys.stdout.write('\033[2K\033[2A\033[G')
            sys.stdout.flush()
            print(f'{left} left' + '\n' + '-'*WIDTH)

        if is_slow:
            for c in hand_list:
                for i in range(1, 7):
                    print(f'\b{i}', end='')
                    time.sleep(0.03)
                print(f'\b{c}', end=' ')
                time.sleep(0.3)
            print('\b', end='')

        else:
            hand_text = ''.join(map(str, hand_list))
            print(hand_text, end='')

        save_text = ''.join(map(str, save_list))
        print('|'+save_text)
        return left

    def show_arrow(choice_index, max_index):
        text = '\r' + ' '*choice_index + '^' + ' '*(4-choice_index)
        text = text[:max_index+2] + ' ' + text[max_index+2:]
        print(text, end='')

    def choice_hand(max_index):

        choice_index = 0
        show_arrow(choice_index, max_index)
        lr_dict = {'left': -1, 'right': 1}

        while True:
            key = keyboard.read_key()
            if key in lr_dict.keys():
                choice_index += lr_dict[key]
                if choice_index < 0:
                    choice_index = 4
                if choice_index > 4:
                    choice_index = 0
                show_arrow(choice_index, max_index)
                time.sleep(0.2)
            return_dict = {
                'space': choice_index,
                'r': 'r',
                'enter': 'enter',
                'esc': 'esc'
            }
            if key in return_dict.keys():
                return return_dict[key]

    os.system('cls')

    hand_list = hands[0] if hands else [random.randint(1, 6) for _ in range(5)]
    save_list = hands[1] if hands else []
    is_slow = False if hands else True

    left = delay_print(hand_list, save_list, is_slow, category_dict, left)
    while True:
        if left <= 0:
            time.sleep(1)
            return [hand_list , save_list], left

        max_index = len(hand_list)-1
        choice_index = choice_hand(max_index)

        if choice_index == 'esc':
            raise Exception('ESCキーが押されました')

        if choice_index == 'enter':
            return [hand_list , save_list], left

        if choice_index == 'r':
            left -= 1
            hand_list = [random.randint(1, 6) for _ in range(len(hand_list))]
            is_slow = True

        else:
            if choice_index <= max_index:
                save_list.append(hand_list.pop(choice_index))
            else:
                hand_list.append(save_list.pop(choice_index-max_index-1))
            is_slow = False

        os.system('cls')
        delay_print(hand_list, save_list, is_slow, category_dict, left)
        time.sleep(0.3)


def calc_sub(hand):
    sorted_dice = sorted(set(hand))
    sub_set = [sorted_dice[i+3] - sorted_dice[i]
               for i in range(len(sorted_dice)-3)]
    return sub_set


def choice_category(hand, category_dict, left):

    def show_hand(hand, category_dict, category_index):
        os.system('cls')

        print('-'*WIDTH)
        print(' '*((WIDTH-5)//2) + ''.join(map(str, hand)))
        print('-'*WIDTH)

        for i, (k, v) in enumerate(category_dict.items()):
            pointer = '>' if i == category_index else ' '
            result = f'({v[1](hand)})' if v[2] else v[0]
            print(f' {pointer} {k}: {result}')

    def can_choice_hand(category_dict, category_index):
        category = list(category_dict.keys())[category_index]
        return category_dict[category][2]

    category_index = [x[2] for x in category_dict.values()].index(True)
    ud_dict = {'up': -1, 'down': 1}

    show_hand(hand, category_dict, category_index)
    time.sleep(0.3)
    while True:
        key = keyboard.read_key()

        if key in ud_dict.keys():
            category_index += ud_dict[key]
            if category_index < 0:
                category_index = len(category_dict)-1
            if category_index > len(category_dict)-1:
                category_index = 0

        if key in ['enter', 'space'] and can_choice_hand(category_dict, category_index):
            return category_index

        if key == 'r' and left > 0:
            return 'r'

        show_hand(hand, category_dict, category_index)
        time.sleep(0.2)


category_dict = {
    'Aces': [0, lambda hand:hand.count(1)*1, True],
    'Deuces': [0, lambda hand:hand.count(2)*2, True],
    'Threes': [0, lambda hand:hand.count(3)*3, True],
    'Fours': [0, lambda hand:hand.count(4)*4, True],
    'Fives': [0, lambda hand:hand.count(5)*5, True],
    'Sixes': [0, lambda hand:hand.count(6)*6, True],
    'Choice': [0, lambda hand:sum(hand), True],
    '4 of a Kind': [0, lambda hand:sum(hand) if max([hand.count(i) for i in set(hand)]) >= 4 else 0, True],
    'Full House': [0, lambda hand:sum(hand) if sorted([hand.count(i) for i in set(hand)]) == [2, 3] else 0, True],
    'S. Straight': [0, lambda hand:15 if 3 in calc_sub(hand) else 0, True],
    'L. Straight': [0, lambda hand:30 if calc_sub(hand) == [3, 3] else 0, True],
    'Yahtzee': [0, lambda hand:50 if len(set(hand)) == 1 else 0, True],
    # 'Bonus':[0,0],
}


while True:
    left = 3
    hands = []
    category_index = 'r'
    while category_index == 'r':
        hands,left = roll_dice(category_dict,left,hands)
        os.system('cls')
        hand = sum(hands,[])
        category_index = choice_category(hand, category_dict, left)
        time.sleep(0.3)

    choiced_category = category_dict[list(
        category_dict.keys())[category_index]]
    choiced_category[0] = choiced_category[1](hand)
    choiced_category[2] = False

    if not any([x[2] for x in category_dict.values()]):
        print(f'your scoa is {sum([x[0] for x in category_dict.values()])}!')
        break
sys.exit()

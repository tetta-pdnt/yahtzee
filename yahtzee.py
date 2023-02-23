# Yahtzee
import random
import time
import sys
import keyboard
import os


def delay_print(hand_list, save_list, is_slow):
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


def roll_dice():
    os.system('cls')
    howto = '<->: move\nSpace: save dice\nr: reroll\nEnter: select hand\n' + '-'*18
    hand_list = [random.randint(1, 6) for _ in range(5)]
    save_list = []
    print(howto)
    delay_print(hand_list, save_list, True)
    def default_func(): return Exception("Invalid input")
    while True:
        max_index = len(hand_list)-1
        choice_index = choice_hand(max_index)
        if choice_index == 'esc':
            raise Exception('ESCキーが押されました')
        if choice_index == 'enter':
            return hand_list + save_list
        if choice_index == 'r':
            hand_list = [random.randint(1, 6) for _ in range(len(hand_list))]
            is_slow = True
        else:
            if choice_index <= max_index:
                save_list.append(hand_list.pop(choice_index))
            else:
                hand_list.append(save_list.pop(choice_index-max_index-1))
            is_slow = False
        os.system('cls')
        print(howto)
        # print(f'{max_index=},{choice_index=}')
        delay_print(hand_list, save_list, is_slow)
        time.sleep(0.3)


def calc_sub(hand):
    sorted_dice = sorted(set(hand))
    sub_set = [sorted_dice[i+3] - sorted_dice[i]
               for i in range(len(sorted_dice)-3)]
    return sub_set


def show_hand(hand, category_dict):
    os.system('cls')
    for i, (k, v) in enumerate(category_dict.items()):
        pointer = '>' if i == choice_index else ' '
        print(f' {pointer} {k}: {v[1](hand)}')


def choice_category(hand, category_dict):
    choice_index = 0
    ud_dict = {'up': -1, 'down': 1}

    show_hand(hand, category_dict)
    while True:
        key = keyboard.read_key()
        if key in ud_dict.keys():
            choice_index += ud_dict[key]
            if choice_index < 0:
                choice_index = len(category_dict)-1
            if choice_index > len(category_dict)-1:
                choice_index = 0
        if key in ['enter', 'space']:
            return choice_index
        show_hand(hand, category_dict)
        time.sleep(0.2)


category_dict = {
    'Aces': [0, lambda hand:hand.count(1)*1],
    'Twos': [0, lambda hand:hand.count(2)*2],
    'Threes': [0, lambda hand:hand.count(3)*3],
    'Fours': [0, lambda hand:hand.count(4)*4],
    'Fives': [0, lambda hand:hand.count(5)*5],
    'Sixes': [0, lambda hand:hand.count(6)*6],
    'Chance': [0, lambda hand:sum(hand)],
    'Four of a Kind': [0, lambda hand:sum(hand) if max([hand.count(i) for i in set(hand)]) >= 4 else 0],
    'Full House': [0, lambda hand:sum(hand) if sorted([hand.count(i) for i in set(hand)]) == [2, 3] else 0],
    'Small Straight': [0, lambda hand:15 if 3 in calc_sub(hand) else 0],
    'Large Straight': [0, lambda hand:30 if calc_sub(hand) == [3, 3] else 0],
    'Yahtzee': [0, lambda hand:50 if len(set(hand)) == 1 else 0],
    # 'Bonus':[0,0],
}

hand = roll_dice()
os.system('cls')
category_index = choice_category(hand, category_dict)


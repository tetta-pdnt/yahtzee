# Yahtzee
import random
import time
import sys
import keyboard
import os


# def delay_print(hand_list,save_list,is_slow):
#     if is_slow:
#         for c in hand_list:
#             for i in range(1,7):
#                 print(f'\b{i}',end='')
#                 time.sleep(0.03)
#             print(f'\b{c}',end=' ')
#             time.sleep(0.3)
#         print('\b',end='')
#     else:
#         hand_text = ''.join(map(str, hand_list))
#         print(hand_text, end='')
#     save_text = ''.join(map(str, save_list))
#     print('|'+save_text)

# def show_arrow(choice_index,max_index):
#     text = '\r' + ' '*choice_index + '^' + ' '*(4-choice_index)
#     text = text[:max_index+2] + ' ' + text[max_index+2:]
#     print(text, end='')


# def choice_hand(max_index):

#     choice_index = 0
#     show_arrow(choice_index,max_index)
#     lr_dict = {'left':-1,'right':1}

#     while True:
#         key = keyboard.read_key()
#         if key in lr_dict.keys():
#             choice_index += lr_dict[key]
#             if choice_index<0:
#                 choice_index = 4
#             if choice_index>4:
#                 choice_index = 0
#             show_arrow(choice_index,max_index)
#             time.sleep(0.3)
#         return_dict = {
#             'space':choice_index,
#             'r':'r',
#             'enter':'enter',
#             'esc':'esc'
#             }
#         if key in return_dict.keys():
#             return return_dict[key]

# def roll_dice():
#     os.system('cls')
#     howto = '<->: move\nSpace: save dice\nr: reroll\nEnter: select hand\n' + '-'*18
#     hand_list = [random.randint(1, 6) for _ in range(5)]
#     save_list = []
#     print(howto)
#     delay_print(hand_list,save_list,True)
#     default_func = lambda: Exception("Invalid input")
#     while True:
#         max_index = len(hand_list)-1
#         choice_index = choice_hand(max_index)
#         if choice_index == 'esc':
#             raise Exception('ESCキーが押されました')
#         if choice_index == 'enter':
#             return hand_list + save_list
#         if choice_index == 'r':
#             hand_list = [random.randint(1, 6) for _ in range(len(hand_list))]
#             is_slow = True
#         else:
#             if choice_index <= max_index:
#                 save_list.append(hand_list.pop(choice_index))
#             else:
#                 hand_list.append(save_list.pop(choice_index-max_index-1))
#             is_slow = False
#         os.system('cls')
#         print(howto)
#         # print(f'{max_index=},{choice_index=}')
#         delay_print(hand_list,save_list,is_slow)
#         time.sleep(0.3)

# hand = roll_dice()
# os.system('cls')
# print(hand)
# def aces(hand):
#     return hand.count(1)
# def twos(hand):
#     return hand.count(2)
# def threes(hand):
#     return hand.count(3)
# def fours(hand):
#     return hand.count(4)
# def fives(hand):
#     return hand.count(5)
# def sixes(hand):
#     return hand.count(6)


# three_of_a_kind = sum(hand) if len(set(hand))<=3 else 0
# four_of_a_kind = sum(hand) if len(set(hand))<=2 else 0
# full_house = sum(hand) if [hand.count(i) for i in set(dice)].sort()==[2,3] else 0
# hands_dict = {
#     'Aces':[0,hand.count(1)*1],
#     'Twos':[0,hand.count(2)*2],
#     'Threes':[0,hand.count(3)*3],
#     'Fours':[0,hand.count(4)*4],
#     'Fives':[0,hand.count(5)*5],
#     'Sixes':[0,hand.count(6)*6],
#     'Three of a Kind':0,
#     'Four of a Kind':0,
#     'Full House':0,
#     'Small Straight':0,
#     'Large Straight':0,
#     'Yahtzee':0,
#     'Chance':0,
#     'Yahtzee Bonus':0,
# }

hand = [1,1,1,2,2]
print(sum(hand) if [hand.count(i) for i in set(hand)].sort()==[2,3] else 0)
print([hand.count(i) for i in set(hand)].sort())
print(set(hand))

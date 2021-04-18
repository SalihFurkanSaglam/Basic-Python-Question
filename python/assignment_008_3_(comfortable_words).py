# -*- coding: utf-8 -*-
"""#Assignment-008/3 (Comfortable Words)

#Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

#A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
#The word will always be a string consisting of only letters from a to z.
#Write a program which returns True if it's a comfortable word or False otherwise.


left_hand = set('qwertasdfgyxcvb')
right_hand = set('zuiophjklnm')
word = set(input(" Please write your word: "))
left_check = word.intersection(left_hand)
right_check = word.intersection(right_hand)
if left_check and right_check:
       print("Your word is comfortable")
else:
       print("Your word is not comfortable")

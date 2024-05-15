import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import array

def BOMB (word):
  choosen_word = f"Your Word: {word}"
  length_of_word = f"Your Length of Word: {len(word)}"
  print(choosen_word, " | ", length_of_word)
  print("")
  word_list = np.array(word)
  print(word_list)

BOMB('jancuk')


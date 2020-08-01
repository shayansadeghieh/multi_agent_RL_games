import logging
import numpy as np

import matplotlib.pyplot as plt

from keras.models import Sequential, Model
from keras.layers import Input, Dense, Conv2D, Flatten, BatchNormalization, Activation, LeakyReLU
from keras.optimizers import SGD
from keras import regularizers

from loss import softmax_cross_entropy_with_logits
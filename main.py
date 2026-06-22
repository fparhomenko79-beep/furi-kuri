import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_array():
    input_list = list(map(float, input().split()))
    return np.array(input_list)

print(get_array())
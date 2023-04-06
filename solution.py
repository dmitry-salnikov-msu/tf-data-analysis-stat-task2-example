import pandas as pd
import numpy as np

from scipy.stats import norm, expon, gamma


chat_id = 626925789 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    #x = 2*(x + 1/2)/95**2
    alpha = 1 - p
    loc = x.mean()
    n = len(x)
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    left   = 2*(loc - 1/2 + gamma.ppf(alpha/2,n)/n)/95**2
    right  = 2*(loc - 1/2 + gamma.ppf(1-alpha/2,n)/n)/95**2
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return left,right

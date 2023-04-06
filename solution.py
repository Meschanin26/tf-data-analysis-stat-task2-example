import pandas as pd
import numpy as np
import scipy
from scipy.stats import norm


chat_id = 470764857 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    jj=np.sum((x-loc)**2)*(len(x)-1)
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    gg=scipy.stats.chi2.ppf(1-alpha,1)
    hh=scipy.stats.chi2.ppf(alpha,1)
    left_side=np.sqrt(jj/gg)/21
    right_side=np.sqrt(jj/hh)/21
    return left_side,right_side

import numpy as np
import scipy

chat_id = 470764857 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x:np.array) -> tuple:
    alpha = 1 - p
    
    r_sum = np.sum(x**2)
    left_chi = scipy.stats.chi2.ppf((1-alpha) / 2, 2 * len(x)) * 21
    right_chi = scipy.stats.chi2.ppf(alpha / 2, 2 * len(x)) * 21

    lower_bound = np.sqrt(r_sum / left_chi)
    upper_bound = np.sqrt(r_sum / right_chi)

    return lower_bound, upper_bound

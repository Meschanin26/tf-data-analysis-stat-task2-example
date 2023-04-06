import numpy as np
from scipy.stats import norm



def solution(p:float, x:np.array) -> tuple:
    # Рассчитываем выборочное среднее и выборочное стандартное отклонение
    sample_mean = np.mean(x)
    sample_std = np.std(x, ddof=1)

    # Рассчитываем значение статистики Z-оценки для уровня доверия
    z_critical = norm.ppf(1 - (1 - p) / 2)

    # Рассчитываем левую и правую границы доверительного интервала
    margin_error = z_critical * sample_std / np.sqrt(len(x))
    lower_bound = sample_mean - margin_error
    upper_bound = sample_mean + margin_error

    return lower_bound, upper_bound

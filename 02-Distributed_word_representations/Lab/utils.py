import numpy as np
import logging



def randmatrix(m, n, lower=-0.5, upper=0.5):
    """Creates an m x n matrix of random values in [lower, upper]"""
    return np.array([random.uniform(lower, upper) for i in range(m*n)]).reshape(m, n)


def log_of_array_ignoring_zeros(M):
    """Returns an array containing the logs of the nonzero
    elements of M. Zeros are left alone since log(0) isn't
    defined.
    """
    log_M = M.copy()
    mask = log_M > 0
    log_M[mask] = np.log(log_M[mask])
    return log_M


def tf_train_progress_logging():
    logging.getLogger('tensorflow').setLevel(logging.INFO)
    def info_filter(logrec):
        return int('loss' in logrec.getMessage().lower())
    logging.getLogger('tensorflow').addFilter(info_filter)
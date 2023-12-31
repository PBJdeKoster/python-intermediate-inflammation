"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data
    (each row contains measurements for a single patient across all days).
    :returns: The daily mean of a 2D inflammation
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data
    (each row contains measurements for a single patient across all days)
    :returns: The daily maximimum over all patients
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data
    :returns: The daily mininimum over all patients
    """
    return np.min(data, axis=0)


def daily_std_dev(data):
    """Calculate the daily standard deviation of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data
    (each row contains measurements for a single patient across all days)
    :returns: The daily standard deviation over all patients
    """
    return np.std(data, axis=0)


def daily_above_threshold(data, patient_num, threshold):
    """Determine whether each daily inflammation value for a
    given patient exceeds a given threshold.

    :param data: A 2D data array with inflammation data
    (each row contains measurements for a single patient across all days)
    :param patient_num: The row number of the patient
    :param threshold: A number that specifies the upper bound a patient should
    not exceed
    
    :returns: A 2D data array with booleans indicating whether the patient has
    exceeded the threshold value 
    """
    result = list(map(lambda x: x > threshold, data[patient_num]))
    return result

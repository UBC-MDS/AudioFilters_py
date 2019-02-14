# This script tests the low_pass_filter function

import numpy as np
import pytest
from AudioFilters.low_pass_filter import low_pass_filter

input_signal = np.genfromtxt('data/bark.csv', dtype = 'float32')

'''
Test that exception is raised for invalid cutoff_frequency argument.
'''
def cutoff_zero():
    with pytest.raises(Exception):
        low_pass_filter(input_signal, 1)

'''
Make sure the output matches example data
'''
def test_low_pass_filter_attenuates_frequencies_below_1000_cutoff():
    expected_output = np.genfromtxt('data/lowpass/bark_lowpass_1000Hz.csv', dtype = 'float32')
    output_signal = low_pass_filter(input_signal, 1000)

    # Mean squared error between input and output signal
    mse = ((expected_output - output_signal)**2).mean(axis=0)
    print(mse)

    assert mse < 0.00001, "Output does not match test data!"


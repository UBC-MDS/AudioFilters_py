# This script tests the low_pass_filter function

import numpy as np
import pytest
from audiofilters.low_pass_filter import low_pass_filter

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

'''
Test that exception is raised for unsupported input_signal argument type.
'''
def test_unsupported_input_signal_type_raises_error():
    with pytest.raises(Exception):
        low_pass_filter(np.array(['1', '2', '3']), 500)

'''
Test that exception is raised for invalid zero cutoff_frequency argument.
'''
def test_cutoff_zero_raises_error():
    with pytest.raises(Exception):
        low_pass_filter(input_signal, 0)

'''
Test that exception is raised for invalid negative cutoff_frequency argument.
'''
def test_cutoff_negative_raises_error():
    with pytest.raises(Exception):
        low_pass_filter(input_signal, -1)

'''
Make sure the output matches example data
'''
def test_low_pass_filter_attenuates_frequencies_below_1000_cutoff():
    expected_output = np.genfromtxt('tests/data/lowpass/bark_lowpass_1000Hz.csv', dtype = 'float32')
    output_signal = low_pass_filter(input_signal, 1000)

    # Mean squared error between input and output signal
    mse = ((expected_output - output_signal)**2).mean(axis=0)
    print(mse)

    assert mse < 0.00001, "Output does not match test data!"

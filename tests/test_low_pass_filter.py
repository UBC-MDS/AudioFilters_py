# This script tests the low_pass_filter function

import numpy as np
import pytest
from AudioFilters.low_pass_filter import low_pass_filter

input_signal = np.genfromtxt('data/bark.csv', dtype = 'float32')

def test_low_pass_filter_attenuates_frequencies_below_1000_cutoff():
    expected_output = np.genfromtxt('data/lowpass/bark_lowpass_1000Hz_24db.csv', dtype = 'float32')
    output_signal = low_pass_filter(input_signal, 1000)

    assert np.array_equal(output_signal, expected_output), "Output does not match expected output!"

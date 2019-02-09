# This script tests the high_pass_filter function

import numpy as np
import pytest
from audiofilters.high_pass_filter import high_pass_filter

input_signal = np.genfromtxt('data/bark.csv', dtype = 'float32')

def test_high_pass_filter_attenuates_frequencies_below_440_cutoff():
    expected_output = np.genfromtxt('data/hipass/bark_highpass_1000Hz_24db.csv', dtype = 'float32')
    output_signal = high_pass_filter(input_signal, 440)

    assert np.array_equal(output_signal, expected_output)

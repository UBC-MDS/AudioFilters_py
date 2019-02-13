import numpy as np
import pytest
from audiofilters.reverb import add_reverb

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

def test_hall_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_hall.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'hall')

    assert np.array_equal(output_signal, expected_output)

def test_church_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_church.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'church')

    assert np.array_equal(output_signal, expected_output)

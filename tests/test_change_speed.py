import numpy as np
import pytest
from audiofilters.change_speed import change_speed

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

def test_change_speed_doubles_playback_speed():
    expected_output = np.genfromtxt('tests/data/change_speed/bark_double_speed.csv', dtype = 'float32')
    output_signal = change_speed(input_signal, 2.0)

    assert np.array_equal(output_signal, expected_output)

def test_change_speed_halves_playback_speed():
    expected_output = np.genfromtxt('tests/data/change_speed/bark_half_speed.csv', dtype = 'float32')
    output_signal = change_speed(input_signal, 0.5)

    assert np.array_equal(output_signal, expected_output)
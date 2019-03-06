import numpy as np
import pytest
from audiofilters.change_speed import change_speed

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

'''
Test that exception is raised for unsupported input_signal argument type.
'''
def test_unsupported_input_signal_type_raises_error():
    with pytest.raises(Exception):
        change_speed(np.array(['1', '2', '3']), 1.5)

'''
Test that exception is raised for negative rate argument
'''
def test_negative_rate_raises_error():
    with pytest.raises(Exception):
        change_speed(input_signal, -1)

'''
Test that exception is raised for rate argument equal to zero
'''
def test_zero_rate_raises_error():
    with pytest.raises(Exception):
        change_speed(input_signal, 0)

'''
Make sure the output matches example data when speed is increased
'''
def test_change_speed_doubles_playback_speed():
    expected_output = np.genfromtxt('tests/data/change_speed/bark_double_speed.csv', dtype = 'float32')
    output_signal = change_speed(input_signal, 2.0)

    # Mean squared error between input and output signal
    mse = ((expected_output - output_signal)**2).mean(axis=0)
    print(mse)

    assert mse < 0.00001, "Output does not match test data!"

'''
Make sure the output matches example data when speed is decreased
'''
def test_change_speed_halves_playback_speed():
    expected_output = np.genfromtxt('tests/data/change_speed/bark_half_speed.csv', dtype = 'float32')
    output_signal = change_speed(input_signal, 0.5)

    # Mean squared error between input and output signal
    mse = ((expected_output - output_signal)**2).mean(axis=0)
    print(mse)

    assert mse < 0.00001, "Output does not match test data!"

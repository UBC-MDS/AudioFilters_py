import numpy as np
import pytest
from audiofilters.reverb import add_reverb

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

'''
Test that exception is raised for unsupported input_signal argument type.
'''
def test_unsupported_input_signal_type_raises_error():
    with pytest.raises(TypeError):
        add_reverb(np.array(['1', '2', '3']), 'hall')

'''
Test that exception is raised for invalid type argument.
'''
def test_unsupported_reverb_type_raises_error():
    with pytest.raises(Exception):
        add_reverb(input_signal, 'unsupported_reverb_type')

'''
Make sure the output matches example data for hall reverb
'''
def test_hall_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_hall.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'hall')

    # Mean squared error between input and output signal
    mse = ((expected_output - output_signal)**2).mean(axis=0)
    print(mse)

    assert mse < 0.00001, "Output does not match test data!"

'''
Make sure the output matches example data for church reverb
'''
def test_church_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_church.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'church')

    # Mean squared error between input and output signal
    mse = ((expected_output - output_signal)**2).mean(axis=0)
    print(mse)

    assert mse < 0.00001, "Output does not match test data!"

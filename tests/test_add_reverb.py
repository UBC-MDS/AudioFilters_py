import numpy as np
import pytest
from audiofilters.reverb import add_reverb

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

'''
Test that exception is raised for unsupported input_signal argument type.
'''
def test_unsupported_input_signal_type_raises_error():
    with pytest.raises(Exception):
        add_reverb(['1', '2', '3'], 'hall')

'''
Test that exception is raised for invalid type argument.
'''
def test_unsupported_reverb_type_raises_error():
    with pytest.raises(Exception):
        add_reverb(input_signal, 'unsupported_reverb_type')

'''
Make sure the output matches example data
'''
def test_hall_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_hall.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'hall')

    assert np.array_equal(output_signal, expected_output)

'''
Make sure the output matches example data
'''
def test_church_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_church.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'church')

    assert np.array_equal(output_signal, expected_output)

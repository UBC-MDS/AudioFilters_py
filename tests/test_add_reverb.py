import numpy as np
import pytest
from audiofilters.reverb import add_reverb

input_signal = np.genfromtxt('tests/data/bark.csv', dtype = 'float32')

'''
Test that TypeError is raised for invalid input_signal argument.
'''
def signal_format():
    with pytest.raises(TypeError):
        add_reverb(123, 1)

'''
Test that exception is raised for an invalid type argument.
'''
def type_invalid():
    with pytest.raises(Exception):
        add_reverb(input_signal, "testTESTtest")

'''
Make sure the output matches example data for hall reverb
'''
def test_hall_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_hall.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'hall')

    assert np.array_equal(output_signal, expected_output)

'''
Make sure the output matches example data for church reverb
'''
def test_church_reverb_is_applied_correctly():
    expected_output = np.genfromtxt('tests/data/reverb/bark_church.csv', dtype = 'float32')
    output_signal = add_reverb(input_signal, 'church')

    assert np.array_equal(output_signal, expected_output)

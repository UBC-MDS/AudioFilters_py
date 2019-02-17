from librosa import core
import numpy as np

def change_speed(input_signal, rate):
    """Change the playback speed of an audio signal

    Parameters
    ----------
    input_signal : numpy.array
        Input array, must have numerical type.
    rate : numeric
        Desired rate of change to the speed.
        To increase the speed, pass in a value greater than 1.0.
        To decrease the speed, pass in a value between 0.0 and 1.0.

    Returns
    -------
    numpy.array representing the audio signal with changed speed.

    """

    if input_signal.dtype.kind not in 'iu' and input_signal.dtype.kind != 'f' :
        raise TypeError("'input_signal' must be an array of integers or floats")

    if rate <= 0:
        raise Exception('rate must be a positive number')

    # Convert input signal to a -1.0 to 1.0 float if it's an integer type
    if input_signal.dtype.kind in 'iu':
        i = np.iinfo('float32')
        abs_max = 2 ** (i.bits - 1)
        offset = i.min + abs_max
        input_signal =  (input_signal.astype('float32') - offset) / abs_max

    # Transform signal to frequency domain
    frequency_domain_signal = core.stft(input_signal)

    # Change speed with the phase vocoding method
    fds_changed_speed = core.phase_vocoder(frequency_domain_signal, rate)

    # Transform frequency domain signal back to time domain
    output_signal = core.istft(fds_changed_speed, dtype = input_signal.dtype)

    return output_signal

import numpy as np

def low_pass_filter(input_signal, cutoff_frequency):
    """Filter audio signal, attenuating frequencies above a cut off.  Sampling rate of input signal is assumed to be 44100 Hz.

    Parameters
    ----------
    input_signal : numpy.array
        Input array, must have numerical type.
    cutoff_frequency : numeric
        Cutoff frequency of the low pass filter.

    Returns
    -------
    numpy.array representing the audio signal with frequencies above the cut off attenuated.

    """

    # Raise error if input_signal is of an unsupported type
    if input_signal.dtype.kind not in 'iu' and input_signal.dtype.kind != 'f' :
        raise TypeError("'input_signal' must be an array of integers or floats")

    # Raise error if cutoff_frequency is not positive
    if cutoff_frequency <= 0:
        raise Exception('cutoff frequency must be a positive number')
    
    cf = cutoff_frequency/44100 # 44100 assumed for sampling rate of input_signal
    trans_bandwidth = 0.08
    # N = int(np.ceil((4 / trans_bandwidth)))
    wndow_grid = np.arange(50)

    # Compute sinc filter.
    sinc_filter = np.sinc(2 * cf * (wndow_grid - (49) / 2))

    # Compute window
    window = np.blackman(50)
    #window = -trans_bandwidth * np.cos(2 * np.pi * wndow_grid / 49) + 0.08 * np.cos(4 * np.pi * wndow_grid / 49)

    # Multiply the sinc filter and window
    lp_filter = sinc_filter * window

    # Normalize
    lp_filter = lp_filter / np.sum(lp_filter)

    # Convert input signal to a -1.0 to 1.0 float if it's an integer type
    if input_signal.dtype.kind in 'iu':
        i = np.iinfo('float32')
        abs_max = 2 ** (i.bits - 1)
        offset = i.min + abs_max
        input_signal =  (input_signal.astype('float32') - offset) / abs_max

    # Apply the filter to the input signal
    output_signal = np.convolve(input_signal, lp_filter)

    return(output_signal)

# References
# https://tomroelandts.com/articles/how-to-create-a-simple-low-pass-filter

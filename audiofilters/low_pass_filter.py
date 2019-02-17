import numpy as np

def low_pass_filter(input_signal, cutoff_frequency):
    """Filter audio signal, attenuating frequencies above a cut off.  Sampling rate of input signal is assumed to be 44100 Hz.

    Parameters
    ----------
    input_signal : numpy.array
        Input array, must have float32 type.
    cutoff_frequency : numeric
        Cutoff frequency of the low pass filter.

    Returns
    -------
    numpy.array representing the audio signal with frequencies above the cut off attenuated.

    """
    
    # Validate inputs
    if cutoff_frequency <= 0:
        raise Exception('cutoff frequency must be a positive number')
    
    try:
        isinstance(input_signal[0], np.float64)
    except TypeError:
        print("Input must be a float64 numpy array")

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

    # Apply the filter to the input signal
    output_signal = np.convolve(input_signal, lp_filter)

    return(output_signal)

# References
# https://tomroelandts.com/articles/how-to-create-a-simple-low-pass-filter

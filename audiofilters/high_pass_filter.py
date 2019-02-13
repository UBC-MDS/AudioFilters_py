import numpy as np

def high_pass_filter(input_signal, cutoff_frequency):
    """Filter audio signal, attenuating frequencies below a cut off.  Sampling rate of input signal is assumed to be 44100 Hz.

    Parameters
    ----------
    input_signal : numpy.array
        Input array, must have float32 type.
    cutoff_frequency : numeric
        Cutoff frequency of the high pass filter.

    Returns
    -------
    numpy.array representing the audio signal with frequencies below the cut off attenuated by 24 db.

    """
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
    hp_filter = sinc_filter * window

    # Normalize
    hp_filter = hp_filter / np.sum(hp_filter)

    # Apply the filter to the input signal
    output_signal = np.convolve(input_signal, hp_filter)

    return(output_signal)

# References
# https://tomroelandts.com/articles/how-to-create-a-simple-low-pass-filter

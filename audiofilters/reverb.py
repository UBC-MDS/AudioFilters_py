import numpy as np

def add_reverb(input_signal, type = 'hall'):
    """Add a reverb effect to the audio signal, simulating a different recording environment

    Parameters
    ----------
    input_signal : numpy.array
        Input array, must have numerical type.
    type : string
        Choice of reverb effect.
        Options are 'hall' and 'church'.
        Defaults to 'hall'.

    Returns
    -------
    numpy.array representing the audio signal with the specified type of reverb applied.

    """
    
    # Validate input signal
    try:
        isinstance(input_signal[0], np.float64)
    except TypeError:
        print("Input must be a float64 numpy array")

    # Raise error if input_signal is of an unsupported type
    if input_signal.dtype.kind not in 'iu' and input_signal.dtype.kind != 'f' :
        raise TypeError("'input_signal' must be an array of integers or floats")

    # Check the reverb type and get the corresponding impulse response file.
    # If the type is not 'hall' or 'church', raise an error.
    if type == "hall":
        impulse_response = np.genfromtxt('audiofilters/impulse_responses/impulse_hall.csv', dtype = 'float32')
    elif type == "church":
        impulse_response = np.genfromtxt('audiofilters/impulse_responses/impulse_church.csv', dtype = 'float32')
    else:
        raise Exception('{} reverb type not supported'.format(type))

    # Convert input signal to a -1.0 to 1.0 float if it's an integer type
    if input_signal.dtype.kind in 'iu':
        i = np.iinfo('float32')
        abs_max = 2 ** (i.bits - 1)
        offset = i.min + abs_max
        input_signal =  (input_signal.astype('float32') - offset) / abs_max

    # Convolve the input_signal with the impulse_response to get the vector with reverb applied.
    return np.convolve(input_signal, impulse_response)

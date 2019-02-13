import numpy as np

def add_reverb(input_signal, type = 'hall'):
    """Add a reverb effect to the audio signal, simulating a different recording environment

    Parameters
    ----------
    input_signal : numpy.array
        Input array, must have float32 type.
    type : string
        Choice of reverb effect.
        Options are 'hall' and 'church'.
        Defaults to 'hall'.

    Returns
    -------
    numpy.array representing the audio signal with the specified type of reverb applied.

    """
    
    if type == "hall":
        impulse_response = np.genfromtxt('audiofilters/impulse_responses/impulse_hall.csv', dtype = 'float32')
    elif type == "church":
        impulse_response = np.genfromtxt('audiofilters/impulse_responses/impulse_church.csv', dtype = 'float32')
    else:
        raise Exception('{} reverb type not supported'.format(type))

    return np.convolve(input_signal, impulse_response)

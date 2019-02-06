# Audio Filters for Python

Python project for sound convolutions

### Contributors
- [Marcelle Chiriboga](https://github.com/mchiriboga)
- [Paul Vial](https://github.com/Pall-v)
- [Socorro Dominguez](https://github.com/sedv8808)

### Overview


### Functions

###### change_speed
This function changes the audio speed, speeding up or down an audio signal.

###### add_reverb
This function applies an effect to an audio signal so that it sounds like it was recorded in a different environment.

###### high_pass_filter
This function uses convolution to attenuate a 1-D (audio) signal signal for frequencies above a specified cutoff level.

### Python Ecosystem
Python software packages that have the same/similar functionality:
- [Pyo](https://github.com/belangeo/pyo) is an existing Python module that Python module provides a variety of audio signal processing type, including [reverb](http://ajaxsoundstudio.com/pyodoc/examples/07-effects/02-schroeder-reverb.html?highlight=reverb) although it is a for a specific type of reverb which we do not plan to implement.  The functionality implemented by our system will also include functions for changing speed and high-pass filtering which are not found in Pyo.  We do not plan to use any digital signal processing packages.  We plan to code the convolutions mathematically within the functions so that they are easily testable and interpretable.  We will make limited use of other packages to represent waveforms, and input/output as neccessary.

### R Ecosystem
- [Seewave](http://rug.mnhn.fr/seewave/) is an an R package dedicated to sound analysis and synthesis and includes a filter, [ffilter](http://rug.mnhn.fr/seewave/HTML/MAN/ffilter.html) with similar functionality to our high-pass filter.

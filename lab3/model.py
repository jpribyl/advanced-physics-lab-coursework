import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fftpack import fft
from scipy import signal

class model(object):

    """A class which holds models corresponding to the lab"""

    def __init__(self, name='Unknown'):
        """models need a name"""
        self.name = name

    def model(self):
        """
        All models need to be able to model something

        """
        pass

class lrc(model):

    """The LRC circuit is a model"""

    def __init__(self,
                freq_list=np.linspace(0, 30000, 10000),
                C=10 * 10**-9,
                R=1000,
                L=68 * 10**-3,
                import_phase=True):

        """
        LRC's need values for L, R, and C as well as frequencies measured
        we can set this model's name automatically
        """

        self.freq_list = freq_list
        self.C = C
        self.R = R
        self.L = L
        self.import_phase = import_phase

        # setting the model.name attribute
        super(lrc, self).__init__('LRC-Model')

    def model(self, plotMag=False, plotPhase=False):
        """
        """
        self.modelMag(plot=plotMag)
        self.modelPhase(plot=plotPhase)
        super().model()

    def modelMag(self, plot=False, style='.'):
        """
        :plot: when true, adds magnitude to the current plot

        """
        self.magnitude = 20 * np.log(1 / (np.sqrt(
        (1 - 4 * self.C * self.freq_list**2 * self.L * np.pi**2)**2 +
        (2 * self.C * self.freq_list * np.pi * self.R)**2)))

        if plot:
            plt.plot(
                self.freq_list / 1000,
                self.magnitude,
                style,
                label = 'Modeled Magnitude of LRC Response')

    def modelPhase(self,
                    path='/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/lrc_phase_df.csv',
                    plot=False):

        if self.import_phase:
            source_list = pd.read_csv(path)
            self.phaseFreq = source_list['frequency']
            self.phase = source_list['phase']

        else:
            self.phase = np.arctan(
            (2 * self.C * self.freq_list * np.pi * self.R) /
            (1 - 4 * self.C * self.freq_list**2 * self.L * np.pi**2))

        if plot:
            plt.plot(self.phaseFreq, self.phase, label = 'Phase of LRC')



class simpleInput(model):

    """
    We need to FT and model several types of input
    """

    def __init__(self,
                 numPoints=6000,
                 sampleSpacing=(1/800),
                 name='Modeled Waveform'):
        """

        :numPoints: number of points to sample
        :sampleSpacing: how far apart the sample points are

        """
        self.N = numPoints
        self.T = sampleSpacing
        self.time = np.linspace(0.0, self.N * self.T, self.N)

        # by default, assume linear relationship between time and voltage
        self.voltageFunction = self.time

        super(simpleInput, self).__init__(name)

    def transformX(self):
        """produce the frequency bins for a single frequency wave
        :returns: An array with the bins for frequency (IE the x axis)

        """

        return np.linspace(0.0, 1.0 / (2.0 * self.T), self.N//2)


    def transformY(self):
        """Transfrom the voltage of a sine function
        :returns: an array with the FT of the voltage of a sine

        """

        return fft(self.voltageFunction)


    def model(self, style='--'):
        """Transform and plot both X and Y domains
        :returns: nothing, but adds sine to current plot

        """
        plt.plot(
            self.transformX(),
            20 * np.log(
                2.0/self.N *
                np.abs(self.transformY()[0:self.N//2])),
            style,
            label=self.name
        )

        return


class sine(simpleInput):

    """
    Fourier Transform and plot a sine functions
    """

    def __init__(self, freq, amplitude=2.5):
        """
        :freq: frequency of the input signal
        :numPoints: number of points to sample
        :sampleSpacing: how far apart the sample points are
        """
        super(sine, self).__init__(
            name="Sine Modeled Waveform"
        )

        # here, we override the relationship between time and frequency
        self.voltageFunction = amplitude * np.sin(freq * 2*np.pi*self.time)


class triangle(simpleInput):

    """
    Fourier Transform and plot a sine functions
    """

    def __init__(self, freq, amplitude=2.5):
        """
        :freq: frequency of the input signal
        :amplitude: peak amplitude of input signal
        """
        super(triangle, self).__init__(
            name='Triangle Modeled Waveform'
        )

        # here, we override the relationship between time and frequency
        self.voltageFunction = amplitude * signal.sawtooth(2 * np.pi * 5 * self.time, width=.5)


class square(simpleInput):

    """
    Fourier Transform and plot a sine functions
    """

    def __init__(self, freq, amplitude=2.5):
        """
        :freq: frequency of the input signal
        :amplitude: peak amplitude of input signal
        """
        super(square, self).__init__(
            name='Square Modeled Waveform'
        )

        # here, we override the relationship between time and frequency
        self.voltageFunction = amplitude * signal.square(2 * np.pi * 5 * self.time)

class sineSum(simpleInput):

    """
    Transform and model the sum of two sine functions
    """

    def __init__(self, freqA, freqB, ampA, ampB):
        """
        :freqA: frequency of first sine
        :freqB: frequency of second sine
        :ampA: amplitude of first sine
        :ampB: amplitude of second sine
        """
        simpleInput.__init__(self, name='Modeled Summer Module')
        self.voltageFunction = \
            ampA * np.sin(freqA * 2*np.pi*self.time) + \
            ampB * np.sin(freqB * 2*np.pi*self.time)


class sineMult(simpleInput):

    """
    Transform and model the product of two sine functions
    """

    def __init__(self, freqA, freqB, ampA, ampB):
        """TODO: to be defined1. """
        simpleInput.__init__(self)

        self.voltageFunction = \
                ampA * ampB * \
                np.sin((freqA * 2 * np.pi) * self.time) * \
                np.sin((freqB * 2 * np.pi) * self.time)



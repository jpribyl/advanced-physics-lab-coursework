import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal
from scipy.fftpack import fft
from scipy.optimize import curve_fit


class model(object):

    """
    A class which holds models corresponding to the lab

    Attributes
    :measurementXValues: The measured X values (used to fit parameters)
    :measurementYValues: The measured Y values (used to fit parameters)
    :measurementYError: The measured y error (used to fit parameters)
    :name: the name of the model, will be displayed on plot legend

    Methods
    :model: a placeholder for the general method which will add the current
    model to a plot
    """

    def __init__(
        self,
        name='Unknown'):

        """models need a name"""
        self.name = name

    def model(self):
        """
        All models need to be able to model something
        """
        pass



class fourierModel(model):

    """
    We need to FT and model several types of input

    Attributes
    :numPoints: The number of points used during the Fourier Transform
    :sampleSpacing: How far apart the points should be
    :name: passed to model.__init__(name) as the name which shows up on plots
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

        super(fourierModel, self).__init__(name)

    def transformX(self):
        """Produce the frequency bins for a single frequency wave
        :returns: An array with the bins for frequency (IE the x axis)

        return np.linspace(0.0, 1.0 / (2.0 * self.T), self.N//2)

        T is the spacing between points
        N is the number of points

        """

        return np.linspace(0.0, 1.0 / (2.0 * self.T), self.N//2)


    def transformY(self):
        """Transfrom the voltage of a sine function
        :returns: an array with the FT of the voltage of a sine

        return 20 * np.log10(
                2.0/self.N *
                np.abs(fft(self.voltageFunction)[0:self.N//2]))
        """

        return 20 * np.log10(
                2.0/self.N *
                np.abs(fft(self.voltageFunction)[0:self.N//2]))


    def model(self, style='--'):
        """Transform and plot both X and Y domains
        :returns: nothing, but adds sine to current plot

        """

        plt.plot(
            self.transformX(),
            self.transformY(),
            style,
            label=self.name
        )

        return


class sine(fourierModel):

    """
    Fourier Transform and plot a sine function
    """

    def __init__(
        self,
        freq,
        numPoints=6000,
        sampleSpacing=1/800,
        amplitude=2.5):
        """
        :freq: frequency of the input signal
        :numPoints: number of points to sample
        :sampleSpacing: how far apart the sample points are
        """
        super(sine, self).__init__(
            numPoints,
            sampleSpacing,
            name="Sine Modeled Waveform"
        )

        # here, we override the relationship between time and frequency
        self.voltageFunction = amplitude * np.sin(freq * 2*np.pi*self.time)


class triangle(fourierModel):

    """
    Fourier Transform and plot a triangle function
    """

    def __init__(self, freq,numPoints=6000, sampleSpacing=1/800, amplitude=2.5):
        """
        :freq: frequency of the input signal
        :amplitude: peak amplitude of input signal
        """
        super(triangle, self).__init__(
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name='Triangle Modeled Waveform'
        )

        # here, we override the relationship between time and frequency
        self.voltageFunction = amplitude * signal.sawtooth(2 * np.pi * 5 * self.time, width=.5)


class square(fourierModel):

    """
    Fourier Transform and plot a square function
    """

    def __init__(self, freq, numPoints=6000, sampleSpacing=1/800, amplitude=2.5):
        """
        :freq: frequency of the input signal
        :amplitude: peak amplitude of input signal
        """
        super(square, self).__init__(
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name='Square Modeled Waveform'
        )

        # here, we override the relationship between time and frequency
        self.voltageFunction = amplitude * signal.square(2 * np.pi * freq * self.time)

class sineSum(fourierModel):

    """
    Transform and model the sum of two sine functions
    """

    def __init__(self, freqA, freqB, ampA, ampB, numPoints=6000, sampleSpacing=1/800):
        """
        :freqA: frequency of first sine
        :freqB: frequency of second sine
        :ampA: amplitude of first sine
        :ampB: amplitude of second sine
        """
        fourierModel.__init__(
            self,
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name='Modeled Summer Module')

        self.voltageFunction = \
            ampA * np.sin(freqA * 2*np.pi*self.time) + \
            ampB * np.sin(freqB * 2*np.pi*self.time)


class sineMult(fourierModel):

    """
    Transform and model the product of two sine functions
    """

    def __init__(self, freqA, freqB, ampA, ampB, numPoints=6000, sampleSpacing=1/800):
        """
        :freqA: frequency of first sine
        :freqB: frequency of second sine
        :ampA: amplitude of first sine
        :ampB: amplitude of second sine
        """
        fourierModel.__init__(
            self,
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name='Modeled Product of Sines')

        self.voltageFunction = \
                ampA * ampB * \
                np.sin((freqA * 2 * np.pi) * self.time) * \
                np.sin((freqB * 2 * np.pi) * self.time)


class lrc(fourierModel):

    """
    The LRC circuit is a fourier model
    """

    def __init__(self,
                 C=10 * 10**-9,
                 R=1000,
                 L=68 * 10**-3,
                 import_phase=True,
                 numPoints=6000,
                 sampleSpacing=1/800,
                 name='LRC-Model'):

        """
        LRC's need values for L, R, and C as well as frequencies measured
        we can set this model's name automatically
        """
        # setting the model.name attribute
        super(lrc, self).__init__(
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name=name)

        self.C = C
        self.R = R
        self.L = L
        self.import_phase = import_phase


    def voltageOut(self):
        """
        :returns: Voltage out in frequency domain calculated by the transfer
        function multiplied by voltage in (IE self.transformY())
        """

        return (1 / (np.sqrt(
        (1 - 4 * self.C * self.transformX()**2 * self.L * np.pi**2)**2 +
        (2 * self.C * self.transformX() * np.pi * self.R)**2))) * self.transformY()

    def phaseOut(self,
                    path='/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/lrc_phase_df.csv',
                    plot=False):

        # if self.import_phase:
            # source_list = pd.read_csv(path)
            # self.phaseFreq = source_list['frequency']
            # self.phase = source_list['phase']

        # else:

        return - np.arctan2(
        (2 * self.C * self.transformX() * np.pi * self.R),
        (1 - 4 * self.C * self.transformX()**2 * self.L * np.pi**2))

    def model(self, style='--'):
        """
        :returns: Nothing, but will plot the FT of the model

        plt.plot(
                    self.transformX(),
                    self.voltageOut(),
                    style,
                    label=self.name
                )


        """
        plt.plot(
            self.transformX(),
            self.voltageOut(),
            style,
            label=self.name
        )

class lrcSine(lrc):

    """
    LRC model when the input is a sine function
    """

    def __init__(
            self,
            freq,
            C=10 * 10**-9,
            R=1000,
            L=68 * 10**-3,
            numPoints=6000,
            sampleSpacing=1/80,
            amplitude=2.5):

        """
        :freq: frequency of the sine input
        """
        lrc.__init__(
            self,
            C=C,
            R=R,
            L=L,
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name='LRC Sine Wave Model')

        self.voltageFunction = amplitude * np.sin(freq * 2*np.pi*self.time)


class lrcSquare(lrc):

    """
    LRC model for a transient step function type response
    """

    def __init__(
                    self,
                    freq,
                    numPoints=6000,
                    sampleSpacing=1/800,
                    amplitude=2.5):
        """
        :freq: frequency of the square input
        """
        lrc.__init__(
            self,
            numPoints=numPoints,
            sampleSpacing=sampleSpacing,
            name='LRC Square Wave Model')

        # convert to Hz
        freq = freq * 1000

        # generate the wave
        self.voltageFunction = amplitude * signal.square(2 * np.pi * freq * self.time)

    def model(self, style='--', alpha=1):
        plt.plot(

            # convert back to kHz
            self.transformX() / 1000,

            self.voltageOut(),

            style, label='LRC Square Wave Model', alpha=alpha)

class lrcMultiFreq(lrc):

    """
    LRC model for a transient step function type response
    """

    def __init__(
        self,
        numPoints=6000,
        sampleSpacing=1/30000,
        xvals=None,
        yvals=None,
        yerr=None,
        amplitude=2.5):
        """
        :freq: frequency of the square input
        """
        lrc.__init__(
            self,
            numPoints=numPoints,
            sampleSpacing=sampleSpacing)

        self.voltageFunction = amplitude * np.random.rand(len(self.time))
        self.xvals = xvals
        self.yvals = yvals
        self.yerr = yerr


class lrcMultiFreqPhase(lrcMultiFreq):

    """
    An instance of this class will model the phase response of a
    multi-frequency input into the LRC circuit
    """

    def __init__(
        self,
        numPoints=6000,
        sampleSpacing=1/30000,
        xvals=None,
        yvals=None,
        yerr=None,
        amplitude=2.5):

        """
        :xvals: the measurement values (measurement.xanvalues)
        :yvals: the measurement values (measurement.yanvalues)
        :yerr: the measurement error (measurement.yanerror)
        
        """
        lrcMultiFreq.__init__(
            self,
            numPoints,
            sampleSpacing,
            xvals,
            yvals,
            yerr,
            amplitude)


    def lrcPhaseFunction(self, x, amp, L, R, C):
        """
        :x: frequency values (x-axis)
        :L: inductance
        :R: resistance
        :C: capacitance
        :returns: a dataframe with the y-values for LRC phase
        """

        return - np.arctan2(
            amp * (2 * C * x * np.pi * R),
            (1 - 4 * C * x**2 * L * np.pi**2))


    def model(self, style='--'):
        """Model
        :returns: Nothing, but plots the phase information

        """

        # try to fit the data provided
        try:
            x = 1000 * self.xvals
            y = 10 ** (self.yvals / 20)
            p0 = np.array([1, self.L, self.C, self.R])
            yerr = self.yerr

            popt, pcov = curve_fit(
                self.lrcPhaseFunction,
                x,
                y,
                sigma=yerr,
                p0=p0)

            xfit = x / 1000
            yfit = 20 * np.log10(self.lrcPhaseFunction(x, *popt))

            plt.plot(xfit, yfit, style, label='LRC Phase Model Fit to Data')

        except Exception as e:
            print("Can't fit data to phase", e)

        # plot the theoretical model without fitting the parameters
        plt.plot(
            self.transformX() / 1000,
            self.lrcPhaseFunction(
                x=self.transformX(),
                amp=1,
                L=self.L,
                R=self.R,
                C=self.C),
            style, label='LRC Phase Model')



class lrcMultiFreqGain(lrcMultiFreq):

    """Docstring for lrcMultiFreqGain. """

    def __init__(
        self,
        numPoints=6000,
        sampleSpacing=1/30000,
        xvals=None,
        yvals=None,
        yerr=None,
        amplitude=2.5):

        """TODO: to be defined1. """
        lrcMultiFreq.__init__(
            self,
            numPoints,
            sampleSpacing,
            xvals,
            yvals,
            yerr,
            amplitude)



    def lrcGainFunction(self, x, amp, L, C, R):
        """
        This is the magnitude of the gain function for the LRC - I produced it
        using Mathematica's ComplexExpand[] and Abs[]

        :x: frequency (X-axis)
        :amp: amplitude parameter of Gain
        :L: induction of LRC
        :R: resistance of LRC
        :C: capacitance of LRC

        :returns: amp / (np.sqrt(
                    (1 - 4 * C * x**2 * L * np.pi**2)**2 +
                    (2 * C * x * np.pi * R)**2))
        """

        return amp / (np.sqrt(
            (1 - 4 * C * x**2 * L * np.pi**2)**2 +
            (2 * C * x * np.pi * R)**2))


    def model(self, style='--'):
        """Model
        :returns: TODO

        """

        x = 1000 * self.xvals
        y = 10 ** (self.yvals / 20)
        p0 = np.array([1, self.L, self.C, self.R])
        yerr = self.yerr

        popt, pcov = curve_fit(
            self.lrcGainFunction,
            x,
            y,
            sigma=yerr,
            p0=p0)

        xfit = x / 1000
        yfit = 20 * np.log10(self.lrcGainFunction(x, *popt))

        plt.plot(xfit, yfit, style, label='LRC Gain Function Model')

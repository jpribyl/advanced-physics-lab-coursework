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
                 y=None,
                 numPoints=10000,
                 sampleSpacing=(1/250),
                 name='Fourier Model'):

        """
        :numPoints: number of points to sample
        :sampleSpacing: how far apart the sample points are

        """
        self.N = numPoints
        self.T = sampleSpacing
        self.time = np.linspace(0.0, self.N * self.T, self.N)

        self.y = y

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
        :returns: an array with the FT of the y function passed to the instance

        return 2.0/self.N * np.abs(fft(self.y)[0:self.N//2])
        """

        return 2.0/self.N * np.abs(fft(self.y)[0:self.N//2])
    
    def complexTransformY(self):
        return 2.0 / self.N * fft(self.y)
    
    def complexTransformX(self):
        return  np.concatenate((np.linspace(-1.0 / (2.0 * self.T), 0, self.N//2), 
            np.linspace(0.0, 1.0 / (2.0 * self.T), self.N//2)))

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

class lrcMultiFreq(lrc):

    """
    LRC model for multiple frequenquency noise / chirp inputs
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




class lrcMultiFreqGain(lrcMultiFreq):

    """
    Class that will model the magnitude of the gain for chirps / noise through
    the LRC circuit. 

    :xvals: The corresponding xanvalues from an instance of the measurement
    class. This data (Pandas DataFrame) will be used to fit parameters to the
    gain function

    :yvals: corresponding measured yanvalues

    :yerr: corresponding measured yanerror
    """

    def __init__(
        self,
        xvals,
        yvals,
        yerr,
        numPoints=10000,
        sampleSpacing=1/250,
        amplitude=2.5):

        """
        Call the superclass initializaion
        """
        lrcMultiFreq.__init__(
            self,
            numPoints,
            sampleSpacing,
            xvals,
            yvals,
            yerr,
            amplitude)



    def lrcGainFunction(self, x, amp, m, w0, xi):
        """
        This is the magnitude of the gain function for the LRC - I produced it
        using Mathematica's ComplexExpand[] and Abs[]

        :x: frequency (X-axis)
        :amp: amplitude parameter of Gain
        :L: induction of LRC
        :R: resistance of LRC
        :C: capacitance of LRC

        :returns: a pandas DF or number depending upon data type of the input
        """

        return amp / (m * x * np.sqrt(
            (2*w0*xi)**2 + (w0**2 - x**2)**2 / x**2
            
            ))


    def model(self, style='--', p0=[5, 10**-13, 50, 1], maxfev=1000):
        """Model method override

        :style: the line style for this plot

        :returns: Nothing, but adds the magnitude of the gain to the current
        plot

        """

        x = self.xvals
        y = self.yvals
        p0 = np.array(p0)
        yerr = self.yerr

        popt, pcov = curve_fit(
            self.lrcGainFunction,
            x,
            y,
            sigma=yerr,
            maxfev=maxfev,
            p0=p0,
        )

        xfit = x
        yfit = self.lrcGainFunction(x, *popt)

        # plt.plot(xfit, yfit, style, label='LRC Gain Function Model')
        return xfit, yfit

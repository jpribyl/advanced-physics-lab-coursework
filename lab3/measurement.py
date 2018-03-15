import pandas as pd
import numpy as np
import mysql.connector as sql
import matplotlib.pyplot as plt
import uncertainties
import os
from uncertainties.unumpy import uarray

password = os.environ['PW']

db_connect = sql.connect(
    host='localhost',
    database='444lab3',
    user='root',
    password=password)


def plot_an(measurementId, channel_num=1, multiplier=1):
    voltage = pd.read_sql('select voltage \
                            from analyzerData \
                            where measurements_id = ' + \
                            str(measurementId),
                         con = db_connect)


    frequency = pd.read_sql('select frequency \
                            from analyzerData \
                            where measurements_id = ' + \
                            str(measurementId),
                        con=db_connect)


    plt.plot(frequency, voltage)

def plot_scope(measurementId, channel_num=1, multiplier=1):
    voltage = pd.read_sql('select voltage \
                            from scopeData \
                            where measurements_id = ' + \
                            str(measurementId),
                         con = db_connect)


    time = pd.read_sql('select time \
                            from scopeData \
                            where measurements_id = ' + \
                            str(measurementId),
                        con=db_connect)


    plt.plot(time, voltage)


def query(query):
    print(pd.read_sql(query, con=db_connect))


class measurement:
    '''
    Objects of this class correspond to measured data.

    ATTRIBUTES:
        :measurementId: Int - unique identifier assigned to each measurement

        :an: Pandas DF - holds all analyzer data

        :xan: Pandas DF - holds uncertainties and values for x component
        :yan: Pandas DF - holds uncertainties and values for y component

        :xanvalues: Pandas DF - holds values for x component
        :yanvalues: Pandas DF - holds values for y component

        :xanerror: Pandas DF - holds uncertainties for x component
        :yanerror: Pandas DF - holds uncertainties for y component

        :sc: Pandas DF - holds all oscilloscope data

        :xsc: Pandas DF - holds values for x component
        :ysc: Pandas DF - holds values for y component
    '''
    def __init__(self, measurementId):
        self.measurementId = measurementId

        print(pd.read_sql('select \
                          id, \
                          filepath, \
                          form_name, \
                          channel_num, \
                          frequency, \
                          amplitude \
                          from measurement_info \
                          where id =' + str(self.measurementId),
                         con = db_connect))


    def getAnalyzerData(self):
        """
        :returns: panadas dataframe with analyzer data from a given measurement

        """
        self.an = pd.read_sql(
            'select \
                frequency, \
                voltage \
                from analyzerData \
                where measurements_id = ' + str(self.measurementId),
            con=db_connect)

        # accuracy of ± 25 ppm from 20°C to 40°C.
        self.frequency = pd.Series(uarray(
            self.an['frequency'],
            25 * self.an['frequency'] / 1000000))

        #convert to kHz
        self.frequency = self.frequency/1000.

        # accuracy of ± 0.3 dB ± 0.02% of full scale (excluding windowing effects)
        an_scale = abs(max(self.an['voltage']) - min(self.an['voltage']))
        self.voltage = pd.Series(uarray(self.an['voltage'], .3 + .02 * an_scale))

        self.xan = self.frequency
        self.yan = self.voltage

        return self.an


    def getScopeData(self):
        """
        :returns: panadas dataframe with scope data from a given measurement

        """
        try:
            self.sc = pd.read_sql(
                'select \
                    time, \
                    voltage \
                    from scopeData \
                    where measurements_id = ' + str(self.measurementId),
                con=db_connect)

            # accuracy of ±3%, from 10 mV/div to 5 V/div
            self.voltage = pd.Series(
                uarray(
                    self.sc['voltage'],
                    abs(self.sc['voltage'] * 3 / 100))
            )

            # accuracy of ± 50 ppm
            self.time = pd.Series(
                uarray(
                    self.sc['time'],
                    abs(50 * self.sc['time'] / 1000000))
            )

            self.time_step = self.time[2]- self.time[1]


            self.xsc = self.time
            self.ysc = self.voltage

            return self.sc

        except Exception as e:
            print('could not get scope data: ', e)

    def fourierTransformVoltage(self):
        """
        :returns: nothing - however, will fourier transform, normalize, and
        convert voltage to dBv and set all the necessary variables for plotting

        """
        try:
            #do fft on oscilloscope voltage data
            self.voltage = self.voltage.apply(lambda x: x.n)
            self.time = self.time.apply(lambda x: x.n)
            self.time_step = self.time[2]- self.time[1]
            # print(self.voltage)
            fftvolt = np.fft.fft(self.voltage)
            #clean up and normalize
            fftvolt = np.fft.fftshift(fftvolt)
            fftvolt= 2*fftvolt/float(len(self.voltage))

            #convert voltage fft to dbv
            self.fftdbv = 20.*np.log10(np.abs(fftvolt))

            #determine the time step and window length for performing fft on x-axis (time)
            self.win_length = len(self.time)

            self.fftfreq = np.fft.fftfreq(self.win_length, self.time_step)
            self.fftfreq = np.fft.fftshift(self.fftfreq)

            #convert to kHz
            self.fftfreq = self.fftfreq/1000.

            self.xsc = self.fftfreq
            self.ysc = self.fftdbv

        except Exception as e:
            print('could not perform FT: ', e)

    def plotData(self, title, ylabel, xlabel, scStyle='-', anStyle='-',
                 anAlpha=1):
        #try to plot scope data
        try:
            plt.plot(self.xsc, self.ysc, scStyle, label = 'FFT of Oscilloscope Data')
        except Exception as e:
            pass

        #try to plot analyzer data
        try:
            self.xanvalues = self.xan.apply(lambda x: x.n)
            self.yanvalues = self.yan.apply(lambda y: y.n)

            self.xanerror = self.xan.apply(lambda x: x.s)
            self.yanerror = self.yan.apply(lambda y: y.s)

            # plot the analyzer data with error bars
            plt.errorbar(self.xanvalues, self.yanvalues, yerr=self.yanerror,
                         fmt='.', label='SR770 Data Points', alpha=anAlpha)

            # connect the points with a faint line
            plt.plot(self.xanvalues, self.yanvalues, anStyle, alpha=.5,
                    label='Line fit of SR770 Points')

            # limit the window to something reasonable
            plt.xlim(0,max(self.xanvalues))
        except Exception as e:
            pass

        try:
            plt.ylim(min(self.yanvalues)-10, max(self.yscvalues)+10)
        except Exception as e:
            pass

        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)

    def model(
        self,
        title='No Title',
        ylabel='No Label',
        xlabel='No Label',
        plotAn=True,
        plotSc=True,
        anAlpha=1):

        if plotAn:
            self.getAnalyzerData()

        if plotSc:
            self.getScopeData()
            self.fourierTransformVoltage()

        self.plotData(title, ylabel, xlabel, anAlpha=anAlpha)

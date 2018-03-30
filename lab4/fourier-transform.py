def fourierTransformy(t, y):
    #do fft on oscilloscope y data
    t_step = t[2]- t[1]
    # print(y)
    ffty = np.fft.fft(y)
    #clean up and normalize
    ffty = np.fft.fftshift(ffty)
    ffty= 2*ffty/float(len(y))

    #convert y fft to dbv
    # fftdbv = 20.*np.log10(np.abs(ffty))

    #determine the t step and window length for performing fft on x-axis (t)
    win_length = len(t)

    fftfreq = np.fft.fftfreq(win_length, t_step)
    fftfreq = np.fft.fftshift(fftfreq)

    #convert to kHz
    fftfreq = fftfreq/1000.

    return fftfreq, ffty


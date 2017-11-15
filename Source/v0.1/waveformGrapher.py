#This is the graphical plotting for each wave. Calculates the values for each one again.
#Puts the values into localized lists and prints them out to the plot
#Thiis function is a basic implimentation of the matplotlib and can be modified slightly for
#clearer output readings.  

#BUG The plot tends to get very squished when using higher frequencies!
#BUG Try to impliment a log function for plotting

import matplotlib.pyplot as plt
import numpy 
import globalQueue


def graphWaveforms():
    SAMPLES = globalQueue.sampleSettings[2] #Local Vars for easier use/calling
    FREQUENCY = globalQueue.sampleSettings[0]
    DURATION = globalQueue.sampleSettings[1]

    SIN_SAMPLES =  (numpy.sin(2*numpy.pi*numpy.arange(SAMPLES*DURATION)*FREQUENCY/SAMPLES)) #Make our sin samples
    INVERSE_SIN_SAMPLES = -1*SIN_SAMPLES #Inverse sin samples should just be a negated version of the sin samples globally
    #so this method of creation is ok.

    TIME = (numpy.arange(0.0, FREQUENCY/2, 1) / 100) * 2 * 2 #Calculations
    SIN_WAVE = (SIN_SAMPLES[0:FREQUENCY/2]) * FREQUENCY #Calculations
    INVERSE_SIN = (INVERSE_SIN_SAMPLES[0:FREQUENCY/2]) * FREQUENCY #Calculations

    plt.plot(TIME, SIN_WAVE, color='b')
    plt.plot(TIME, INVERSE_SIN, color='r')

    plt.xlabel('TIME (S)')
    plt.ylabel('FREQUENCY CHANGE')
    plt.title('WAVEFORM COMPARISONS')      #Plot settings
    plt.grid(True)
    plt.savefig("/WAVEFORMS.png")
    plt.show() #DRAW IT!


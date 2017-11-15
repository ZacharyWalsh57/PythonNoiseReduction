from decimal import Decimal
import numpy
import pyaudio
import globalQueue
import sampleSettings

#Take the frequency that the user wants.  Make a sweeping wave of it now.
#So for a frequency 'x' we need to begin at the middle of it "x/2" as an INT. NOT FLOAT
#Then add one to that list until we hit the frequency value, then down to zero and back to
#the middle of the frequency.  This is one period of the frequency.  

def CSV(): #Ask the user for a CSV preference
    CSV = int(raw_input("Would you like a CSV with the sample points? (0 is No, 1 is Yes): "))
    globalQueue.appendCreateSoundSamples(CSV,globalQueue.VERBOOSE_SETTING) #Append CSV preferences


def SIN_WAVE_GENERATOR(FREQUENCY, DURATION, SAMPLES, CSV): #Generate Sin Wave samples for that frequency
    print "\nGENERATING SINE WAVEFORM....."
    SIN_SAMPLES = ((numpy.sin(2*numpy.pi*numpy.arange(SAMPLES*DURATION)*FREQUENCY/SAMPLES))) * 1000
    if CSV == 1: numpy.savetxt("SIN_DATA.csv", SIN_SAMPLES, delimiter='\n') #Save them if the user wants to

    MIDPOINT = SAMPLES / 2 #Midpoint of the samples (should be a positive value)
    MIDPOINT_SAMPLE = '%.2e' % Decimal(SIN_SAMPLES[MIDPOINT])

    globalQueue.appendSIN_WAVE_SAMPLES(SIN_SAMPLES, globalQueue.VERBOOSE_SETTING) #Append sin wave values

    globalQueue.appendCreateSoundSamples(SIN_SAMPLES[0], globalQueue.VERBOOSE_SETTING) #Append the first sin value
    globalQueue.appendCreateSoundSamples(SIN_SAMPLES[MIDPOINT], globalQueue.VERBOOSE_SETTING) #Append the midpoint value

def INVERSE_WAVE_GENERATOR(FREQUENCY, DURATION, SAMPLES, CSV): #Generate the inverse phase wave
    print "GENERATING INVERSE WAVEFORM....."
    INVERSE_SIN_SAMPLES = (-1*(numpy.sin(2*numpy.pi*numpy.arange(SAMPLES*DURATION)*FREQUENCY/SAMPLES))) * 1000 #Math for samples
    if CSV == 1: numpy.savetxt("INVERSE_SIN_DATA.csv", INVERSE_SIN_SAMPLES, delimiter='\n') #Save them if wanted
    
    MIDPOINT = SAMPLES / 2
    MIDPOINT_SAMPLE = '%.2e' % Decimal(INVERSE_SIN_SAMPLES[MIDPOINT])

    globalQueue.appendINVERSE_SIN_WAVE_SAMPLES(INVERSE_SIN_SAMPLES, globalQueue.VERBOOSE_SETTING) #Append all values 
 
    globalQueue.appendCreateSoundSamples(INVERSE_SIN_SAMPLES[0], globalQueue.VERBOOSE_SETTING) #Append the first value
    globalQueue.appendCreateSoundSamples(INVERSE_SIN_SAMPLES[MIDPOINT], globalQueue.VERBOOSE_SETTING) #Append midpoint.  Must be opposite sign!

import globalQueue
import numpy
import scipy
import scipy.io.wavfile


#This library is used to create the actual files of audio from the samples of the sin wave and inverse sin wave.
#STRUCTUTRE
#   L or R or COMBINE
#   Generate sin
#   generate inverse
#   save files
#       name them sin and inverse sine if monos
#       name them sin-inverse sin if stereo.

def SIN_GENERATION():
    print "SIN GENERATING......"
    SIN_SAMPLES = []
    SIN_SAMPLES.append(globalQueue.SIN_WAVE_SAMPLES)
    SIN_SAMPLES = numpy.asarray(SIN_SAMPLES, dtype=numpy.int16)
    scipy.io.wavfile.write('SIN.wav', globalQueue.sampleSettings[2], SIN_SAMPLES)

def INVERSE_GENERATION():
    print "INVERSE GENERATING....."
    INVERSE_SAMPLES = []
    INVERSE_SAMPLES.append(globalQueue.INVERSE_SIN_WAVE_SAMPLES)
    INVERSE_SAMPLES = numpy.asarray(INVERSE_SAMPLES, dtype=numpy.int16)
    scipy.io.wavfile.write('INVERSE_SIN.wav', globalQueue.sampleSettings[2], INVERSE_SAMPLES)
    
    


def SIN_AND_INVERSE_GENERATION():
    print "ADDING"


def monoStereo():
    MONO_STEREO = int(raw_input("Would you like to use one channel for each sound or one combined sound file? (0 for mono, 1 for stereo)"))
    globalQueue.appendGenerateSounds(MONO_STEREO, globalQueue.VERBOOSE_SETTING)

    if MONO_STEREO == 0:
        print "MONO SELECTED.  The SIN wave will be the left speaker and the inverse phase will be the right speaker seperately"
        print "Please hold while the sounds are created."

        SIN_GENERATION()
        INVERSE_GENERATION()

    if MONO_STEREO == 1:
        print "STEREO SELECTED. The SIN wave and inverse phase wave will be saved as two different files!"
        print "Please hold while the sounds are created."

        SIN_AND_INVERSE_GENERATION()


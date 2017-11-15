#This file is a "RAM" for the porgram.  All variables used in each library gets its own list.
#As things are collected, the values get added into the list. 
#The order of elements in the list is defined by the order of functions in the file.
#So for the settings library, we have FREQUENCY_GRABBER and GET_DURATION in that order.
#The FREQUENCY_GRABBER info comes first, then the GET_DURATION info.


#Initalization funtion to make each library specific list:
VERBOOSE_SETTING = '0' #changes to one if the user picks run verboose.

def initLists(VERBOOSE): #VERBOOSE allows the user to see the lists as the program runs.
    global sampleSettings #List for sample options
    global createSoundFile #List with peaks, valleys, and midpoints
    global SIN_WAVE_SAMPLES #List of all sin wave points
    global INVERSE_SIN_WAVE_SAMPLES #List of all inverse wave points
    global generateSounds
    sampleSettings = [] 
    createSoundFile = []        #INITS 
    SIN_WAVE_SAMPLES = []
    INVERSE_SIN_WAVE_SAMPLES = []
    generateSounds = []

    if int(VERBOOSE) == 1:
        #PRINTS ALL LISTS FROM INIT!!
        print "\nsamplesSettings: " + str(sampleSettings[:]).rjust(20, )
        print "createSoundFile: " + str(createSoundFile[:]).rjust(20, )
        print "SinWaveSamples" + str(SIN_WAVE_SAMPLES[:]).rjust(20, )
        print "InverseSampple" + str(INVERSE_SIN_WAVE_SAMPLES[:]).rjust(20, )
        print "GenerateSounds" + str(generateSounds[:]).rjust(20, )
        print "Lists Initalized, moving on...\n"

def printLists():
    #Print out the lists with their current values at any point.
    createSoundFile_FORMATTED = ['%.1e' % elem for elem in createSoundFile]
    print "\nsamplesSettings: " + (str(sampleSettings[:])).rjust(30, )
    try:
        print "createSoundFile: " +  ('[' + str(createSoundFile_FORMATTED[2]) + ']' +  ' ' + '[' + str(createSoundFile_FORMATTED[4]) + ']').rjust(30, )
    except:
        print "createSoundFile: " + str(createSoundFile[:]).rjust(30) + '\n'

def appendSampleSettings(value, VERBOOSE): #add value to the settings of each wave
    sampleSettings.append(value)
    if int(VERBOOSE) == 1:
        printLists()

def appendCreateSoundSamples(value, VERBOOSE): #Add value to the creation points
    createSoundFile.append(value)
    if int(VERBOOSE) == 1:
        printLists()

def appendSIN_WAVE_SAMPLES(value, VERBOOSE): #Add value to the sin wave samples
    SIN_WAVE_SAMPLES.append(value)
    if int(VERBOOSE) == 1:
        print SIN_WAVE_SAMPLES[:]


def appendINVERSE_SIN_WAVE_SAMPLES(value, VERBOOSE): #Add value to inverse phase samples
    INVERSE_SIN_WAVE_SAMPLES.append(value)
    if int(VERBOOSE) == 1:
        print INVERSE_SIN_WAVE_SAMPLES[:]

def appendGenerateSounds(value, VERBOOSE): #Add Values to the generate sounds file.
    generateSounds.append(value)
    if int(VERBOOSE == 1):
        print generateSounds[:]

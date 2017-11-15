import globalQueue

#This is a proof of concept test for active noise cancling.  
#Each file will act as a library, calling functions from each one as needed.
#This file gathers settings about the frequency which we want to cancel.

#Function to take a frequency of the sound to be generated
def FREQUENCY_GRABBER():
    global GENERATE_FREQUENCY
    GENERATE_FREQUENCY = int(raw_input("\nENTER FREQUENCY IN HERZT (IN BASE 0: 10kHz is 10000): "))

    if GENERATE_FREQUENCY < 10: #Confirm if the sound is valid.
        print "FREQUENCY TOO LOW! ENTER NEW FREQUENCY"
        FREQUENCY_GRABBER() #Recursively call back to pick again.
    elif GENERATE_FREQUENCY > 20000: #Confirm again.
        print "FREQUENCY TOO HIGH! ENTER NEW FREQUENCY"
        FREQUENCY_GRABBER() #Recursively call back to pick again.

    print "\nSelected frequency is " + str(GENERATE_FREQUENCY) + "hz"
    #Display a confirmation of what the user picked.

    RESPONSE = raw_input("Is this correct? Yes or No: ") #Confirm if the selection is right or not.
    if RESPONSE.lower() == "no" or RESPONSE.lower() == "n": #Check answer
        print "ENTER A NEW FREQUENCY"
        FREQUENCY_GRABBER() #If the user fucked up, they are redirected to pick a new sound again.
    #BUG: WHEN RESELECTING TWICE IN ONE RUN THE APP DOES NOT CORRECTLY RUN THE FUNCTION
    else:
        globalQueue.appendSampleSettings(GENERATE_FREQUENCY,globalQueue.VERBOOSE_SETTING) #APPEND THE VALUE TO THE GLOBAL QUEUE

def GET_DURATION(): #Get time for the frequency to play in the program
    global TIME
    TIME = int(raw_input("\nENTER A TIME DURATION OF THE FREQUENCY IN SECONDS: ")) #Get duration
    if TIME > 0: #Check for a valid duratio!
        print "A " + str(GENERATE_FREQUENCY) + "hz frequency will play for " + str(TIME) + " seconds."
    if TIME < 0:
        print "MUST HAVE A DURATION OVER 0!"
        GET_DURATION()
    
    globalQueue.appendSampleSettings(TIME,globalQueue.VERBOOSE_SETTING) #APPEND THE VALUE TO THE GLOBAL QUEUE!

def GET_SAMPLES():
    global SAMPLES
    print "NOTE: SAMPLES UNDER 1024 WILL LOOK STRANGE.  SAMPLES ABOVE 192000 WILL AS WELL."
    SAMPLES = int(raw_input("\nEnter a number of samples to take for each wave to be generated.  (A good value is 72000 for fast computing): "))
    if SAMPLES <= 0:
        print "MUST HAVE A SAMPLE RATE OVER 0!"
        GET_SAMPLES()
    globalQueue.appendSampleSettings(SAMPLES, globalQueue.VERBOOSE_SETTING)


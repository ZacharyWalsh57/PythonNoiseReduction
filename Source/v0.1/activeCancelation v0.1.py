import globalQueue #Lists shared between files
import sampleSettings #Settings of frequency to generate
import createSoundFile #Lib used to make the sound file
import waveformGrapher #Lib used to graph the sound files.
import generateSounds

print "Welcome to Active Noise Cancelation v 0.1!"
print "This program is used to demonstrate the ability of two sounds canceling one another out."
print "This causes the 'sound' output to be nothing! In other words, complete silence."

print "\nVerboose mode in this program allows you to see the values printed on screen as they are added to a global queue along with other things."
VERBOOSE = (raw_input("Would you like the program to run in verboose mode? (1=YES 0=NO): "))
globalQueue.VERBOOSE_SETTING = VERBOOSE

#Run setup function for the global lists:
globalQueue.initLists(globalQueue.VERBOOSE_SETTING)

sampleSettings.FREQUENCY_GRABBER()
sampleSettings.GET_DURATION()
sampleSettings.GET_SAMPLES()

print "\nPreparing to generate sound file, this may take a while."

createSoundFile.CSV()
createSoundFile.SIN_WAVE_GENERATOR(globalQueue.sampleSettings[0], globalQueue.sampleSettings[1], globalQueue.sampleSettings[2], globalQueue.createSoundFile[0])
createSoundFile.INVERSE_WAVE_GENERATOR(globalQueue.sampleSettings[0], globalQueue.sampleSettings[1], globalQueue.sampleSettings[2], globalQueue.createSoundFile[0])

print "\nSoundwave forms have been mapped!"
print "\nPlease note: CSV's that were generated with over 1024 samples or over 5 seconds may require a massive amount of RAM to open."
print "To see the values of a certian sample rate, enter the sample rate you want to evaluate and reduce the time to one second."
print "If you didn't generate CSV's, several values that are of importance are listed below:"
globalQueue.printLists()

print "\nDisplaying graphs of the two waves generated to ensure they are opposite phases...."
print "If the graphs do not appear to be opposite phases, please run the program again"
print "NOTE: SAMPLES BELOW 10000 WILL LOOK STAGGERED ON THE GRAPH. RETRY USING A DIFFERENT RATE IF NEEDED"
print "The graph has been saved locally as a file named WAVEFORMS.png"
waveformGrapher.graphWaveforms()

print "\nBegining the creation of the audio files now..."
generateSounds.monoStereo()

print "\nWAV Files have been created successfully!"
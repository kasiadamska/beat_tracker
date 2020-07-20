#import libraries
import os
import numpy as np
import librosa
import wave

#beattracker function
def beatTracker(inFile):
    y, sr = librosa.load(os.path.join(inFile))
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    librosa.frames_to_time(beats[:20], sr=sr)

    # measure the onset strength by computing a spectrum flux onset strength envelope
    onset_env = librosa.onset.onset_strength(y, sr=sr,aggregate=np.median)
    #estimate the tempo from onset correlation, pick beats
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
    print('Tempo(bpm):', tempo)
    print(' ')

    beats_all = np.around(librosa.frames_to_time(beats), decimals=10)

    #print for 4/4
    print('Tactus:', beats_all[0], beats_all[1], beats_all[2], beats_all[3])

    #print for 3/4
    #print('Tactus:', beats_all[0], beats_all[1], beats_all[2])

    #print all
    #print('Tactus:', beats_all)

    print(' ')
    print('Downbeats (first beat of each bar):')
    downbeats = beats_all[::4]
    #downbeats_waltz = beats_all[::3]

    #print in columns
    for x in range(len(downbeats)):
        print(downbeats[x])
    #save to txt file
    np.savetxt("estimated_beats.txt", beats_all, fmt="%g")
    return beats, downbeats

########################################################################s
###### PLEASE CHANGE PATH AND FILE NAME FOR TESTING
###### 'wav/genre/filename.wav'
beats, downbeats = beatTracker('wav/ChaCha/Albums-Cafe_Paradiso-05.wav')

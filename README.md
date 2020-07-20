# beat_tracker
Beat Tracker implemented using Librosa library. 

I have implemented this method by using librosa’s dynamic programming beat tracker function librosa.beat.beat_track and the librosa.onset.onset_strength function to compute the spectral flux onset strength envelope.
After running beatTracker.py , the following values will be printed in the terminal: tempo in bpm, all beats of the first bar and the first beats of each bar (downbeats).
Finally, all beat times are saved into a text file estimated_beats.txt for further evaluation. The file is overwritten every time a new audio file is loaded to the beat tracker for individual evaluation.

Librosa Documentation: https://librosa.github.io/librosa/generated/librosa.beat.beat_track.html https://librosa.github.io/librosa/generated/librosa.beat.plp.html

mir_eval Documentation: https://craffel.github.io/mir_eval/#mir-eval

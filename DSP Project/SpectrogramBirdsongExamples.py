# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:23:39 2022

@author: G00372842
"""

# -*- coding: utf-8 -*-
"""
@author: Michelle Lynch
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# Read in original audio
# Note, the Song Thrush xeno-canto audio was originally .mp3, converted to .wav using Audacity
#rate, audio = wavfile.read('../Audio/xenocanto/XC255239 - Song Thrush - Turdus philomelos.wav')
# The Nightingales audio works better with a threshold of vmin=20 in pcolormesh
rate, audio = wavfile.read('myself.wav')

 # Average the stereo channels, comment out for mono audio files
# audio = np.mean(audio, axis=1)
 # Total number of audio samples   
N = audio.shape[0]       
 # Length of audio track in seconds         
L = N / rate                  
print(f'Audio length: {L:.2f} seconds')

# Spectrogram calculation using scipy
freqs_sp, times_sp, spec_sp = signal.spectrogram(audio, fs=rate, window='hanning',
                                                 nperseg=1024, noverlap=1024-100,
                                                 detrend=False, scaling='spectrum')
# Calculate the magnitude of the spectrum in decibels
spec_db_sp = 10*np.log10(spec_sp)

# Function to plot the original audio in the time-domain
def plot_time_domain():
    fig = plt.figure(figsize=(14,10))
    ax = fig.add_subplot(111)
    ax.plot(np.arange(N) / rate, audio)
    ax.set_title('Birdsong', fontsize=26, pad=10, color='sienna');
    ax.set_xlabel('Time (s)', fontsize=20, labelpad=10)
    ax.set_ylabel('Amplitude', fontsize=20, labelpad=10);

# Function to plot the spectrogram, parameters may require tuning depending on the audio file
def plot_spec_scipy():
    fig, ax = plt.subplots(figsize=(18,14))
    im = ax.pcolormesh(times_sp, freqs_sp/1000, spec_db_sp, vmax=spec_db_sp.max(), vmin=20, cmap=plt.cm.Reds, linewidth=10)
    #im = ax.pcolormesh(times_sp, freqs_sp/1000, spec_db_sp, vmax=spec_db_sp.max(), vmin=20, cmap=plt.cm.gist_yarg, linewidth=10)
    cb = fig.colorbar(im, ax=ax, orientation="horizontal")
    ax.set_ylabel('Frequency (kHz)', fontsize=26, labelpad=10)
    ax.set_xlabel('Time (s)', fontsize=26, labelpad=10);
    ax.set_title('Birdsong Spectrogram', fontsize=26, pad=10, color='sienna');
    ax.set_title('Recording One', fontsize=26, pad=10, color='sienna');
    ax.set_ylim(0, 15)
    ax.tick_params(axis='both', which='both', labelsize=22, length=0)
    cb.set_label('Power (dB)', fontsize=26, labelpad=10)
    cb.ax.tick_params(labelsize=22)
    
plot_time_domain();
plot_spec_scipy();
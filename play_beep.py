import simpleaudio as sa
import numpy as np
from time import sleep

FREQUENCY = 800  # Frequency of the signal
SAMPLING = 44100  # Frequency of the sample taking
SECONDS = .05


# Morse Code timing
# short mark, dot or dit (  ▄ ): 1
# longer mark, dash or dah (  ▄▄▄ ): 111
# intra-character gap (between the dits and dahs within a character): 0
# short gap (between letters): 000
# medium gap (between words): 0000000
# https://en.wikipedia.org/wiki/Morse_code#Timing


def play_dit(secs=SECONDS):
    # Generate an array of seconds*sampling steps to form the sine wave
    t = np.linspace(start=0, stop=secs, num=int(SAMPLING * secs), endpoint=False)
    # Sine wave
    note = np.sin(FREQUENCY * t * 2 * np.pi)
    # Ensure that the note is 16 bit
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
    # convert to 16 data
    audio = audio.astype(np.int16)
    # playback
    audio_obj = sa.play_buffer(audio_data=audio, num_channels=1, bytes_per_sample=2, sample_rate=SAMPLING)
    audio_obj.wait_done()


def play_dah(secs=SECONDS * 3):
    play_dit(secs=secs)


def letter_gap():
    sleep(SECONDS * 3)


def word_gap():
    sleep(SECONDS * 7)

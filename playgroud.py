from pedalboard import load_plugin, Pedalboard, Reverb
from pedalboard.io import AudioFile, AudioStream
import numpy as np
import simpleaudio
import librosa
import os
import pygame.midi as midi

plugin = load_plugin("C://Program Files//Common Files//VST3//TAL-NoiseMaker.vst3//Contents//x86_64-win//TAL-NoiseMaker.vst3")

pedalboard = Pedalboard([
    plugin,
    Reverb(room_size=0.25),
])


midi.init()
default_id = midi.get_default_input_id()
midi_input = midi.Input(device_id=default_id)

pressed_keys = set()

a = pow(2, 1/12)

try: 
    while True:
        if midi_input.poll():
            read_event = midi_input.read(num_events=16)
            print(read_event)
            if read_event[0][0][0] == 144:
              for evnt in read_event:
                pressed_keys.add(evnt[0][1])
            elif read_event[0][0][0] == 128:
              try:
                for evnt in read_event:
                  pressed_keys.remove(evnt[0][1])
              except:
                print("whoops")

        for key in pressed_keys:
          tone_offset = (key - 48)
          print(tone_offset, 220 * pow(a, tone_offset))
          tone = librosa.tone(220 * pow(a, tone_offset), sr=44100, duration=0.05)
          output = pedalboard.process(np.array( [tone, tone] ), 44100)
          buf = simpleaudio.play_buffer(output, 2, 4, 44100)
except KeyboardInterrupt as err:
    print("Stopping...")

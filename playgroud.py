from pedalboard import load_plugin, Pedalboard, Reverb
from pedalboard.io import AudioFile, AudioStream
import numpy as np
import simpleaudio
import librosa

plugin = load_plugin("/Library/Audio/Plug-Ins/Components/TAL-NoiseMaker.component")

pedalboard = Pedalboard([
    plugin,
    Reverb(room_size=0.25),
])

while True:
  key = input("a, b, or c?")
  if key == "a":
     break
  elif key == "b":
    tone = librosa.tone(440, sr=44100, duration=0.1)
  elif key == "c":
    tone = librosa.tone(450, sr=44100, duration=0.1)

  output = pedalboard.process(np.array( [tone, tone] ), 44100)
  buf = simpleaudio.play_buffer(output, 2, 4, 44100)
  buf.wait_done()

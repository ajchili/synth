from pedalboard import load_plugin
from pedalboard.io import AudioFile
import numpy as np
import librosa

plugin = load_plugin("/Library/Audio/Plug-Ins/Components/TAL-NoiseMaker.component")

tone = librosa.tone(440, sr=44100, duration=5)

output = plugin.process(np.array( [tone, tone] ), 44100)

with AudioFile('processed-output.wav', 'w', 44100, output.shape[0]) as f:
  f.write(output)
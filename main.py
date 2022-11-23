from playaudio import Audio
from directions import Directions
audio = Audio()
text = audio.record()

Directions(text)

print(text)
# audio.play(response)

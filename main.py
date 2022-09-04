from playaudio import Audio
from directions import Directions
audio = Audio()
audio.record()
text = audio.speech_to_text()

text = str(text)
text = text.lower()

Directions(text)

print(text)
# audio.play(response)

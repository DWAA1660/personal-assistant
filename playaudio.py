from playsound import playsound
from pocketsphinx import LiveSpeech
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
from config import API_TOKEN
class Audio():
    def __init__(self, *args):
        pass
    def play(text, repeat=False):

        if repeat is False:    
            speach = gTTS(text=text, lang='en', slow=False)
            speach.save('tts.wav')

            playsound('tts.wav')
        else:
            playsound('tts.wav')

    # def speech_to_text(self):

        # headers = {"Authorization": f"Bearer {API_TOKEN}"}
        # API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"

        # def query(filename):
        #     with open(filename, "rb") as f:
        #         data = f.read()
        #     start_time = time.time()
        #     response = requests.request("POST", API_URL, headers=headers, data=data)
        #     print(f"Fetched response in {int(time.time()) - int(start_time)} seconds")
        #     return json.loads(response.content.decode("utf-8"))

        # data = query("sample1.flac")
        # return str(data['text'])
    

        
    
    def record(self):
        for phrase in LiveSpeech():
            text = str(phrase)
            break
        
        return text
        
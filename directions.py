import difflib, wikipedia
from wikipedia import PageError
from difflib import SequenceMatcher, get_close_matches
from email.mime import audio
from playaudio import Audio
from data import jokes, riddles
import secrets

aliases = {
    'say': 'say',
    'hey': 'say',
    'they': 'say',
    'google': 'google',
    'repeat': 'repeat',
    'tell': 'tell',
    'lookup': 'google',
    'what': 'repeat',
    
}

class Directions():
    def __init__(self, said_word):
        self.said_word = said_word
        options = [
            'say',
            'google',
            'repeat',
            'tell',
        ]
        for option in aliases.keys():
            
            said_word_list = self.said_word.split(' ')
            # print(option, said_word_list)
            if self.similar(said_word_list[0], option) >= 0.4:
                function = getattr(self, option)
                function(said_word)
                return
        possibilitys = get_close_matches(said_word_list[0], list(aliases.keys()))
        for possibility in possibilitys:
            print(possibility)
            function = getattr(self, possibilitys[possibility])
            function(said_word)
            break
    
    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def say(self, said_word):
        words = said_word.split(' ')
        words.pop(0)
        words = ' '.join(words)
        Audio.play(words)
        
    def google(self, said_word):
        words = said_word.split(' ')
        words.pop(0)
        words = ' '.join(words)
        try:
            results = wikipedia.summary(words, sentences=2)
        except PageError:
            Audio.play('No results found')
            return
        print(results)
        
        Audio.play(results)
    
    def tell(self, said_word):
        options = [
            'joke',
            'riddle',
        ]
        said_words = said_word.split(' ')
        for word in said_words: 
            if (matches := get_close_matches(word, options)) != []:
                if 'joke' in matches:
                    Audio.play(secrets.SystemRandom().choice(jokes))
                elif 'riddle' in matches:
                    Audio.play(secrets.SystemRandom().choice(riddles))
        
    def repeat(self, said_word):
        Audio.play(text='Repeat', repeat=True)

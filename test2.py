import time
import os


lyrics = [
    "Uyamuya sayonara karui memai",
    "Anata no inai genshoukai",
    "Daremo yomenai karute",
    
]

def clear_screen():
   
    os.system('cls' if os.name == 'nt' else 'clear')

def show_lyrics_with_animation(lyrics, delay=4):
    for line in lyrics:
        clear_screen()
        print(line)
        time.sleep(delay)

show_lyrics_with_animation(lyrics)
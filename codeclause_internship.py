# CodeclauseInternship_Musicplayer

import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music(file_path):
    stop_music()
    play_music(file_path)

if __name__ == "__main__":
    music_files = ["Apna_Bana.mp3", "Tere_vaste.mp3", "zihaal.mp3","Kesariya.mp3"]
    current_track = 0

    play_music(music_files[current_track])

    while True:
        command = input("Enter Your Command 'stop', 'next', or 'exit' => ")

        if command == "stop":
            stop_music()
        elif command == "next":
            current_track = (current_track + 1) % len(music_files)
            next_music(music_files[current_track])
        elif command == "exit":
            stop_music()
            break
        else:
            print("Invalid command. Please enter 'stop', 'next', or 'exit'.")

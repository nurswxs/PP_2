import pygame

playlist = [
    "music/2.wav",
    "music/1.wav",
    "music/3.mp3"
]

current_track = 0
is_playing = False


def play():
    global is_playing
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    is_playing = True


def stop():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False


def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play()


def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play()


def get_track_name():
    return playlist[current_track].split("/")[-1]

def get_position():
    pos = pygame.mixer.music.get_pos()
    if pos == -1:
        return 0
    return pos // 1000
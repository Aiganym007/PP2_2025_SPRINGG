import pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Music Player")

screen=pygame.display.set_mode((700,700))
playlist = [r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\labb7\2task\music\e.mp3", r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\labb7\2task\music\q.mp3", r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\labb7\2task\music\w.mp3"]
current_track = 0
music_st = True  

def playmusic(song_index):
    global music_st
    pygame.mixer.music.load(playlist[song_index]) 
    pygame.mixer.music.play() 
    music_st = False

running = True
while running:
    screen.fill((255,255,255))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                if music_st:
                    playmusic(current_track) #play music
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop() #stop music
                music_st = True
            elif event.key == pygame.K_n: 
                current_track = (current_track + 1) % len(playlist) #next music
                playmusic(current_track)
            elif event.key == pygame.K_b: 
                current_track = (current_track - 1) % len(playlist) #previous music
                playmusic(current_track)


pygame.quit()
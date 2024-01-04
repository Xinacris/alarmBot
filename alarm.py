import pygame
import random
import time

# Initialize Pygame
pygame.init()

min_wait = 1
max_wait = 5

# Load the sound
sound = pygame.mixer.Sound("alarm.wav")
# Generate a random integer between 1 and 10

while True:
  wait_time = random.randint(min_wait, max_wait)
    
  print(f"Waiting for alarm for {wait_time} minutes...")
  start_time = time.time()

  # Play the sound for the specified time
  while time.time() - start_time < wait_time*60:
    pass

  # Start playing the alarm in a separate thread (non-blocking)
  sound.play()
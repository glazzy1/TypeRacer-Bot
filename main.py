import os
import time
import pyautogui

os.system('cls && title [typeracer.com typer] - Main Menu')
speed = input(
    '[1] Legit\n'
    '[2] Fast\n'
    '[3] Pro\n'
    '[4] Hacker\n\n'
    '[>] Select a speed: '
)

if speed.upper() in ('LEGIT', '1'):
    speed = 0.2
elif speed.upper() in ('FAST', '2'):
    speed = 0.1
elif speed.upper() in ('PRO', '3'):
    speed = 0.05
elif speed.upper() in ('HACKER', '4'):
    speed = 0.025
else:
    print('\n[!] Invalid option.')
    os.system(
        'title [typeracer.com typer] - Restart required && '
        'pause >NUL && '
        'title [typeracer.com typer] - Exiting...'
    )
    time.sleep(3)
    os._exit(0)

text = input('\n[>] Text: ')
searching = True
os.system('title [typeracer.com typer] - Waiting for match to start...')

while searching:
    try:
        pyautogui.click('txtInput.png')
    except TypeError:  # Image not located
        continue
    os.system('title [typeracer.com typer] - Typing...')
    searching = False

start_time = time.time()
try:
    pyautogui.write(text, interval=speed)
except pyautogui.FailSafeException:
    print('\n[!] Stopped due to mouse being located at a corner of the screen — SAFE MODE')
    os.system('title [typeracer.com typer] - Stopped && pause >NUL')
else:
    stop_time = time.time()
    print(f'\n[!] Elapsed Time: {round(stop_time - start_time, 2)} seconds')
    os.system('title [typeracer.com typer] - Finished && pause >NUL')

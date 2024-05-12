import numpy as np
import pyautogui
import mss
from time import sleep, time
from PIL import Image, ImageOps
from webbrowser import open

pyautogui.useImageNotFoundException(False)
cactus_count = 0
start_time = time()


def should_jump():
    with mss.mss() as sct:
        monitor = {"top": 500, "left": 715, "width": 40, "height": 35}
        img = np.array(sct.grab(monitor))
        img = Image.fromarray(img)  # Convert numpy array to PIL image
        grayimg = ImageOps.grayscale(img)
        a = sum(map(sum, grayimg.getcolors()))
    return np.sum(a) != 1655


def jump():
    global cactus_count
    global start_time
    ratio = round(time() - start_time) / 100
    pyautogui.keyDown('space')
    sleep(0.001 * (1 - ratio))
    pyautogui.keyUp('space')
    sleep(0.001 * (1 - ratio))
    cactus_count += 1
    return


def start():
    open('https://googledino.com')
    sleep(3)
    pyautogui.press('space')
    sleep(2)
    return


def the_end():
    print(f'🌵 Пройдено кактусов: {cactus_count}.')
    print(f'⌛️ За {round(time() - start_time)} секунд.')
    pyautogui.hotkey('ctrl', 'w')
    return


def main():
    start()
    while True:
        if (pyautogui.locateOnScreen('game_over.png', region=(835, 355, 300, 200), grayscale=True, confidence=0.8)
                is not None):
            the_end()
            break
        elif should_jump():
            jump()


if __name__ == '__main__':
    main()

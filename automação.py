import pyautogui
import time

# Pausa de 1 segundo entre cada comando pyautogui
pyautogui.PAUSE = 1

# Mover o mouse para a posição (100, 100)
pyautogui.moveTo(100, 100, duration=1)

# Clicar na posição atual do mouse
pyautogui.click()

# Escrever texto
pyautogui.write('Olá, Mundo!', interval=0.1)

# Pressionar Enter
pyautogui.press('enter')

# Capturar uma imagem da tela
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

# Mover o mouse em relação à posição atual
pyautogui.moveRel(200, 0, duration=1)

# Duplo clique
pyautogui.doubleClick()

# Arrastar o mouse
pyautogui.dragTo(300, 300, duration=1)

# Ver a posição atual do mouse
current_mouse_position = pyautogui.position()
print(f"Posição atual do mouse: {current_mouse_position}")

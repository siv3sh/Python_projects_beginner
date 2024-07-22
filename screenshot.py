import time
import pyautogui
from pathlib import Path
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    

    directory = Path('/Users/siv3sh/screenshot_data')
    directory.mkdir(parents=True, exist_ok=True)  
    
    file_path = directory / f'{name}.png'
    
  
    time.sleep(5)
    
    try:

        img = pyautogui.screenshot(str(file_path))
        print(f'Screenshot saved to: {file_path}')
        
        img.show()
    except Exception as e:
        print(f'An error occurred: {e}')


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    text = "Take screenshot",
    command = screenshot
    )

button.pack(side = tk.LEFT )
close = tk.Button(
    frame,
     text = "Quit",
    command = quit
)
close.pack(side = tk.LEFT)


root.mainloop()

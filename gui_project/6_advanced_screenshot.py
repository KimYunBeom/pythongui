import time
import keyboard
from PIL import ImageGrab

def screenshot():
  # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
  curr_time = time.strftime('_%Y%m%d_%H%M%S')
  img = ImageGrab.grab()
  img.save('image{}.png'.format(curr_time)) # image_20200601_102030.png

keyboard.add_hotkey('f9', screenshot) # 사용자가 F9 키를 누르면 스크린샷 저장
# keyboard.add_hotkey('ctrl+shift+s', screenshot) # 조합키 가능

keyboard.wait('esc') # 사용자가 esc 를 누를때까지 프로그램 수행

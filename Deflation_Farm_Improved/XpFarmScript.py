import cv2 
import time
import pyautogui
import keyboard

Game_started = False
in_Game = False
count = 0

input("Press ENTER to begin the script, once started you may have to restart pc to get it to stop. ")
time.sleep(5)

Game_started = True
in_Game = True


### FUNCTIONS 

#Image Finder Function 
def image_locater(image, clicks = 0, off_x=0, off_y=0):
    position = pyautogui.locateCenterOnScreen(image, confidence=.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pyautogui.moveTo(position, duration=.1)
        pyautogui.moveRel(off_x, off_y)
        pyautogui.click(clicks=clicks, interval=.3)
pass
        

#Puts you into a game of infernal on deflation
def into_game():
        #Click Play
        image_locater('Images\Play_Button.png',1)
        time.sleep(0.1)

        #Click Expert
        image_locater('Images\Expert_Button.png',1)
        time.sleep(0.01)

        #Click Infernal
        time.sleep(0.3)
        pyautogui.click(1307, 661)
        time.sleep(1)

        #Click Easy
        image_locater('Images\Easy_Button.png',1)
        time.sleep(0.01)

        #Click Deflation
        image_locater('Images\Deflation_Button.png',1)
        time.sleep(5)

        #Click Ok
        image_locater('Images\OK.jpg',1 )
        time.sleep(0.1)
        return 0
    
#Clicking and placing sniper monkey
def sniper_monk():
     pyautogui.dragTo(1544, 600, 0.01)
     keyboard.press_and_release('z')
     time.sleep(0.02)
     pyautogui.click(1544, 600)
     time.sleep(0.01)
     pyautogui.click(1544, 600)

     #Bottom Path Faster Firing
     image_locater('Images\Fast_Firing.png', 1)
     pyautogui.leftClick()
     time.sleep(0.01)

     pyautogui.leftClick()
     time.sleep(0.01)

     pyautogui.leftClick()
     time.sleep(0.01)

     image_locater('Images\Vision.png', 1)
     pyautogui.leftClick()
     time.sleep(0.01)
pass
     

# EDITORS COMMENT ----- Can Make this cleaner with seperate functions. (Come Fix ME!!)
#Place Alchemists, Upgrade Alchemists
def alch():
     pyautogui.dragTo(1608, 513, 0.01)
     keyboard.press_and_release('f')
     time.sleep(0.02)
     pyautogui.click(1608, 513)
     time.sleep(0.01)
     pyautogui.click(1608, 513)

     #Top Path Stim
     image_locater('Images\Larger_potions.png', 1)
     pyautogui.leftClick()
     time.sleep(0.01)

     pyautogui.leftClick()
     time.sleep(0.01)

     pyautogui.leftClick()
     time.sleep(0.01)

     #Middle Path Stronger Acid
     image_locater('Images\Stronger_acid.png', 1)
     pyautogui.leftClick()
     time.sleep(0.02)

     #Alchemist Number 2 1594, 671
     pyautogui.dragTo(1594, 671, 0.01)
     keyboard.press_and_release('f')
     time.sleep(0.02)
     pyautogui.click(1594, 671)
     time.sleep(0.01)
     pyautogui.click(1594, 671)

     #Upgrades For Alch 2 Top Path
     image_locater('Images\Larger_potions.png', 1)
     pyautogui.leftClick()
     time.sleep(0.01)

     pyautogui.leftClick()
     time.sleep(0.01)

     pyautogui.leftClick()
     time.sleep(0.01)

     #Bottom Path Upgrades for Alch 2 
     image_locater('Images\Faster_Throwing.png', 1)
     pyautogui.leftClick()
     time.sleep(0.1)
### Looping functions
while in_Game == True:
     into_game()
     time.sleep(0.4)
     sniper_monk()
     time.sleep(0.4)
     alch()
     time.sleep(0.4)

     #Start game after towers placed
     time.sleep(0.3)
     pyautogui.click(1815, 998)
     time.sleep(0.1)
     pyautogui.click(1815, 998)

     #Checking for level up
     inGame_time = 0
     while inGame_time <= 16:
          pyautogui.leftClick(741, 794)
          time.sleep(1)
          pyautogui.leftClick(999, 0)
          time.sleep(4)
          pyautogui.leftClick(741, 794)
          time.sleep(1)
          pyautogui.leftClick(999, 0)
          time.sleep(4)
          time.sleep(9)
          inGame_time+=1

     else:
          count+=1
          image_locater('Images\win_next.png', 1)
          time.sleep(0.1)
          image_locater('Images\Home_Icon.png', 1)
          print('Congrats you completed '+ str(count) + ' runs.')

          # EDIT THIS NUMBER TO DECIDE HOW LONG SCRIPT WILL RUN DEFAULT IS 100. Number set will determine how many games of deflation will be played.
          if count >= 100:
               in_Game = False
               pass

     time.sleep(5)
else:
     print("An unexpected error occured...that/'s weird")



# Computer_Vision_Projects_2_Touchless_Screen_from_Scratch
This repository is dedicated to one of my computer vision projects for COVID-19. Precisely, building a touchless screen from scratch with Python. This logic can be used in principal in public places (train stations, ATMs, etc.) to avoid direct contact.


An application consists of the Interface and Logic. Both components have two parts - responsible for movement of the coursor and its click/push. 

To run the program simply write:
```
python Touchless_Screen.py
```

Initial interface should look like this:
<img width="1272" alt="Touchless_Screen_Interface" src="https://user-images.githubusercontent.com/18334850/124047314-35b22300-da14-11eb-8541-6e011dd8cacb.png">

Holding a marker shows on the screen:
![image](https://user-images.githubusercontent.com/18334850/124361233-4a6a0300-dc2e-11eb-9cb4-24f0223c3a15.png)


Actual control happens with the marker of a given color. Based on its color and threshold value (given by a user/developer), one can start controling the coursor's movement and clicking functionalities. 

A short animation representing the cursor movement:
![Touchless_Screen_Cursor_Movement4](https://user-images.githubusercontent.com/18334850/124370691-b07c7780-dc7a-11eb-8a1f-1263744af035.gif)


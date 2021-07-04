# Computer_Vision_Projects_2_Touchless_Screen_from_Scratch
This repository is dedicated to one of my computer vision projects for COVID-19. Precisely, building a touchless screen from scratch with Python. This logic can be used, in principle, in public places (train stations, ATMs, etc.) to avoid direct contact.


An application consists of the Interface and Logic. Both components have two parts - responsible for movement of the coursor and its click/push. 

To run the program simply write:
```
python Touchless_Screen.py
```

Initial interface should look like this:
<img width="1392" alt="Touchless_Screen_Interface" src="https://user-images.githubusercontent.com/18334850/124370715-e02b7f80-dc7a-11eb-868b-725ed88bae39.png">


Holding a marker shows on the screen:
<img width="1392" alt="Touchless_Screen_Interface_1" src="https://user-images.githubusercontent.com/18334850/124370721-eae61480-dc7a-11eb-8e53-4eec216dae9b.png">


Actual control happens with the marker of a given color. Based on its color and threshold value (given by a user/developer), one can start controling the coursor's movement and clicking functionalities. 
<img width="1392" alt="Touchless_Screen_Interface_2" src="https://user-images.githubusercontent.com/18334850/124370728-f5081300-dc7a-11eb-9d4d-930f0c8df9a0.png">


A short animation representing the cursor movement:
![Touchless_Screen_Cursor_Movement4](https://user-images.githubusercontent.com/18334850/124370691-b07c7780-dc7a-11eb-8a1f-1263744af035.gif)


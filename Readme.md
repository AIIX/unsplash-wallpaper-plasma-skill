# mycroft-unsplash-wallpaper-plasma-skill
This skill allows users to use unsplash images as wallpapers based on their category of choice (nature, sports, aircrafts, etc) on the plasma desktop.

#### Installation of skill:
* Download or Clone Git
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "mycroft-unsplash-wallpaper-plasma-skill". (Clone does not require this step)
* Copy the mycroft-unsplash-wallpaper-plasma-skill folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora: 
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Kubuntu / KDE Neon: 
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus and Python Psutil package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

##### How To Use: 
###### Play Music/Song
- "Hey Mycroft, change wallpaper type aircrafts"
- "Hey Mycroft, change wallpaper abstract"
- "Hey Mycroft, new wallpaper type nature"
- "Hey Mycroft, new wallpaper sports" 

## Current state

Working features:
* Change wallpaper

Known issues:
* None

TODO:
* Change wallpaper to random type when no utterance type is mentioned

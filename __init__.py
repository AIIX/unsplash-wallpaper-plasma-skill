import sys
import dbus
import requests
import random
import os
import time
from bs4 import BeautifulSoup
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)

class UnsplashPlasmaWallpaperSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(UnsplashPlasmaWallpaperSkill, self).__init__(name="UnsplashPlasmaWallpaperSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        unsplash_plasma_desktopskill_intent = IntentBuilder("UnsplashKeywordIntent").\
            require("UnsplashPlasmaDesktopSkillKeyword").build()
        self.register_intent(unsplash_plasma_desktopskill_intent, self.handle_unsplash_plasma_desktopskill_intent)
        
    def handle_unsplash_plasma_desktopskill_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(
                message.data.get('UnsplashPlasmaDesktopSkillKeyword'), '')
        searchString = utterance
        rawrinpt = str(searchString)
        url = 'https://unsplash.com/search/' + rawrinpt
        i = int(1)
        cut = 20
        baseURL = 'https://unsplash.com/'
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        data = soup.findAll(
                'a',
                attrs={
                    'class': '_23lr1'
                }
        )
        img = random.choice(data)
        fullHREF = img.get('href')
        fileSave = fullHREF[cut:]
        link = '{}{}/download'.format(baseURL[:-1], fullHREF)
        ossep = os.path.sep
        directory = os.path.realpath(os.getcwd() + ossep + "pictures" + ossep)
        if not os.path.exists(directory):
            time.sleep(1)
            os.makedirs(directory)
            
        currdir = os.getcwd()
        f = open(directory + ossep + fileSave + '.jpg', 'wb')
        f.write(requests.get(link).content)
        f.close()
        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript('var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file://' + currdir + '/pictures/' + fileSave + '.jpg' + '")}', dbus_interface = "org.kde.PlasmaShell")
        
        #self.speak_dialog("krunner.search", data={'Query': searchString})

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return UnsplashPlasmaWallpaperSkill()

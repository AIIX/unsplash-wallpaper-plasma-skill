import sys
import dbus
import requests
import random
import os
import time
from io import open as iopen
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)

class UnsplashPlasmaWallpaperSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(UnsplashPlasmaWallpaperSkill, self).__init__(name="UnsplashPlasmaWallpaperSkill")
        
    @intent_handler(IntentBuilder("UnsplashKeywordIntent").require("UnsplashPlasmaDesktopSkillKeyword").build())        
    def handle_unsplash_plasma_desktopskill_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(
                message.data.get('UnsplashPlasmaDesktopSkillKeyword'), '')
        searchString = utterance
        rawrinpt = str(searchString)
        category = rawrinpt
        size = '1920x1080'
        file_url = 'https://source.unsplash.com/' + size + '/' + '?' + category
        suffix_random = str(random.randint(1111,9999))
        file_name = category + suffix_random
        i = requests.get(file_url)
        if i.status_code == requests.codes.ok:            
            ossep = os.path.sep
            directory = os.path.realpath(os.getcwd() + ossep + "pictures" + ossep)
            if not os.path.exists(directory):
                time.sleep(1)
                os.makedirs(directory)
            
            with iopen(directory + ossep + file_name + '.jpg', 'wb') as file:
                file.write(i.content)
                file.close()
                
        currdir = os.getcwd()
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.plasmashell","/PlasmaShell") 
        remote_object.evaluateScript('var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file://' + currdir + '/pictures/' + file_name + '.jpg' + '")}', dbus_interface = "org.kde.PlasmaShell")
        
        #self.speak_dialog("krunner.search", data={'Query': searchString})

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return UnsplashPlasmaWallpaperSkill()

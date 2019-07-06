# guided by: https://projects.raspberrypi.org/en/projects/the-all-seeing-pi
# see the project output at: https://twitter.com/SunsetIFB102

from twython import Twython

# imports keys and tokens from seperate auth file
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)

# takes photo 
from picamera import PiCamera
import random

# set up the camera
camera = PiCamera()
camera.resolution = (800,480)
camera.hflip = True
camera.start_preview() # camera.start_preview(alpha=128)

from time import gmtime, strftime

# the image file will be named after the time it was taken
output = strftime("/home/pi/sunsetBot/Image-%d-%m%H:%M.png", gmtime())

# caption options
messages = ["Isn't this beautiful?", 
        "According to all known laws of aviation there is no way a bee should be able to fly",
        "Ooh pretty", "The sun is setting soon", 
        "Sunsets are proof that no matter what happens, every day can end beautfully",
        "Such sun so set", "It is the end of the day and the sky looks like this",
        "Aren't these clouds cool? (Hope there's actually clouds in this picture)",
        "Sunsets are great", "Sunsets are cool", "Here's a picture of the sky",
        "Here's a picture of the sunset"]

# takes picture
def take_picture():
    camera.capture(output)
    camera.stop_preview()  
    print("Picture taken!")

take_picture()

def send_tweet():
    twitter = Twython(
    consumer_key,   
    consumer_secret,
    access_token,
    access_token_secret)

    image = open(output,'rb')
    response = twitter.upload_media(media=image)

    message = random.choice(messages)
    twitter.update_status(status=message, media_ids=[response['media_id']])
    print("tweeted :", message)        


send_tweet()

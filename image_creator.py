from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timezone, timedelta
import time

def make_ordinal(n): #Thank you Florian Brucker
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def create_image():
  now = datetime.fromtimestamp(time.time())
  tomorrow =  now + timedelta(days=1)
  formatted_tomorrow = tomorrow.strftime(f"%B {make_ordinal(tomorrow.day)}")

  background = Image.new("RGBA", (1200,730), color="white")

  homealone = Image.open("homealone.jpg")
  background.paste(homealone, box=(0,100))

  text_image = Image.new("RGBA", (1200,100), color="white")
  font = ImageFont.truetype("arial.ttf", 70)
  draw = ImageDraw.Draw(text_image)
  draw.text((-10,0), f"Tomorrow is {formatted_tomorrow}", font=font, fill=(0,0,0,255))
  background.paste(text_image, box=(0,0))

  background = background.resize((200, 120), Image.ANTIALIAS)
  background = background.resize((1200,720), Image.ANTIALIAS)
  background.save("image.png", "PNG")
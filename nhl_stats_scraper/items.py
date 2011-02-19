# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Game(Item):
    # define the fields for your item here like:
    date = Field()
    homeTeam = Field()
    awayTeam = Field()
    homeScore = Field()
    awayScore = Field()
    
    pass

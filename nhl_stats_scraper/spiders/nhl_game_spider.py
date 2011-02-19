from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from nhl_stats_scraper.items import Game

class NhlGameSpider(BaseSpider):
    name = "nhl_games"
    allowed_domains = ["nhl.com"]
    start_urls = [
        "http://www.nhl.com/ice/scores.htm?date=02/01/2011"
    ]

    def parse(self, response):
        dateFields = response.url.split("=")[-1].split("/")
        args = (dateFields[2], dateFields[0], dateFields[1])
        date = "%s-%s-%s" % args

        hxs = HtmlXPathSelector(response)
        games = hxs.select("//div[@class='sbGame']/div[2]")

        items = []
	for game in games:
            home = game.select(".//td[@class='sbHomeTeam']/..")
            away = game.select(".//td[@class='sbAwayTeam']/..")
            item = Game()
            item['date'] = date
            item['homeTeam'] = home.select("./td[@class='sbHomeTeam']/div[1]/text()").extract()
            item['awayTeam'] = away.select("./td[@class='sbAwayTeam']/div[1]/text()").extract()
            item['homeScore'] = home.select("./td[starts-with(@id,'toh')]/text()").extract()
            item['awayScore'] = away.select("./td[starts-with(@id,'toa')]/text()").extract()
            items.append(item)
        return items

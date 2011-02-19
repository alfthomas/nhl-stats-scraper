# Scrapy settings for nhl_stats project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'nhl_stats_scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['nhl_stats_scraper.spiders']
NEWSPIDER_MODULE = 'nhl_stats_scraper.spiders'
DEFAULT_ITEM_CLASS = 'nhl_stats_scraper.items.Game'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.98 Safari/534.13'


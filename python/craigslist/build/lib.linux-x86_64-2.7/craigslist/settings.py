# Scrapy settings for craigslist project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'craigslist'

SPIDER_MODULES = ['craigslist.spiders']
NEWSPIDER_MODULE = 'craigslist.spiders'


ITEM_PIPELINES = {'craigslist.pipelines.CraigslistPipeline' : 1 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist (+http://www.yourdomain.com)'

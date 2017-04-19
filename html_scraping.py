# http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests

# the html page where the data is
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')

# Use page.content rather than page.text because html.fromstring implicitly expects bytes as input.
tree = html.fromstring(page.content)

# Page data is contained in two elements - one is a div with title ‘buyer-name’ and the other is a span with class ‘item-price’:
# <div title="buyer-name">Carson Busses</div>
# <span class="item-price">$29.95</span>

# This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices

# EOF

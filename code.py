from pprint import pprint
from datetime import datetime
from utils import get_fundamentals

URL_FUNDAMENTALS      = 'https://www.moneycontrol.com/india/stockpricequote/plastics/cosmofirst/CF08'
URL_QUARTERLY_RESULTS = 'https://www.moneycontrol.com/financials/cosmofilms/results/consolidated-quarterly-results/CF08'
data = {}

data['scrape_time'] = datetime.now()
data['fundamentals'] = get_fundamentals(URL_FUNDAMENTALS)
# data['quarterly_results'] = get_quarterly_results(URL_QUARTERLY_RESULTS)

pprint(data)
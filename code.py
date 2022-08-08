from pprint import pprint
from datetime import datetime
from utils import get_fundamentals, get_quarterly_results, get_balance_sheet_data, get_cash_flow_data, get_ratios_data

URL_FUNDAMENTALS      = 'https://www.moneycontrol.com/india/stockpricequote/plastics/cosmofirst/CF08'
URL_QUARTERLY_RESULTS = f'https://www.moneycontrol.com/financials/{URL_FUNDAMENTALS.split("/")[-2]}/results/consolidated-quarterly-results/{URL_FUNDAMENTALS.split("/")[-1]}'
URL_BALANCE_SHEET     = f'https://www.moneycontrol.com/financials/{URL_FUNDAMENTALS.split("/")[-2]}/consolidated-balance-sheetVI/{URL_FUNDAMENTALS.split("/")[-1]}'
URL_CASH_FLOW         = f'https://www.moneycontrol.com/financials/{URL_FUNDAMENTALS.split("/")[-2]}/consolidated-cash-flowVI/{URL_FUNDAMENTALS.split("/")[-1]}'
URL_RATIOS            = f'https://www.moneycontrol.com/mc/widget/mcfinancials/getFinancialData?classic=true&referenceId=ratios&requestType=C&scId={URL_FUNDAMENTALS.split("/")[-1]}'
data = {}

data['scrape_time']       = datetime.now()
data['fundamentals']      = get_fundamentals(URL_FUNDAMENTALS)
data['quarterly_results'] = get_quarterly_results(URL_QUARTERLY_RESULTS)
data['balance_sheet']     = get_balance_sheet_data(URL_BALANCE_SHEET)
data['cash_flow']         = get_cash_flow_data(URL_CASH_FLOW)
data['ratios']            = get_ratios_data(URL_RATIOS)

pprint(data, sort_dicts=False)
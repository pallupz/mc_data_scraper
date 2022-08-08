import requests
from bs4 import BeautifulSoup
from typing import Dict

def get_fundamentals(URL: str) -> Dict:
    output = {}
    output['url'] = URL

    try:
        page = requests.get(URL)
        page.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    else:
        soup = BeautifulSoup(page.text, 'html.parser')

        overviews = soup.find_all('div', 'oview_table')
        for item in overviews:
            if item.find('td', 'nseopn bseopn'):
                output['open'] = float(item.find('td', 'nseopn bseopn').text.strip().replace(',', ''))
            if item.find('td', 'nseprvclose bseprvclose'):
                output['prev_close'] = float(item.find('td', 'nseprvclose bseprvclose').text.strip().replace(',', ''))
            if item.find('td', 'nsevol bsevol'):
                output['volume'] = float(item.find('td', 'nsevol bsevol').text.strip().replace(',', ''))
            if item.find('td', 'nsevalue bsevalue'):
                output['value_lakhs'] = float(item.find('td', 'nsevalue bsevalue').text.strip().replace(',', ''))
            if item.find('span', 'nsebeta'):
                output['beta'] = float(item.find('span', 'nsebeta').text.strip().replace(',', ''))
            if item.find('td', 'nsevwap bsevwap'):
                output['vwap'] = float(item.find('td', 'nsevwap bsevwap').text.strip().replace(',', ''))
            if item.find('td', 'nseHP bseHP'):
                output['high'] = float(item.find('td', 'nseHP bseHP').text.strip().replace(',', ''))
            if item.find('td', 'nseLP bseLP'):
                output['low'] = float(item.find('td', 'nseLP bseLP').text.strip().replace(',', ''))
            if item.find('td', 'nseH52 bseH52'):
                output['52_week_high'] = float(item.find('td', 'nseH52 bseH52').text.strip().replace(',', ''))
            if item.find('td', 'nseL52 bseL52'):
                output['52_week_low'] = float(item.find('td', 'nseL52 bseL52').text.strip().replace(',', ''))
            if item.find('td', 'nseceps bseceps'):
                output['eps_ttm'] = float(item.find('td', 'nseceps bseceps').text.strip().replace(',', ''))
            if item.find('td', 'nsepe bsepe'):
                output['pe_ttm'] = float(item.find('td', 'nsepe bsepe').text.strip().replace(',', ''))
            if item.find('td', 'nsesc_ttm bsesc_ttm'):
                output['pe_sector'] = float(item.find('td', 'nsesc_ttm bsesc_ttm').text.strip().replace(',', ''))
            if item.find('td', 'nsebv bsebv'):
                output['book_value_ps'] = float(item.find('td', 'nsebv bsebv').text.strip().replace(',', ''))
            if item.find('td', 'nsepb bsepb'):
                output['price_to_book'] = float(item.find('td', 'nsepb bsepb').text.strip().replace(',', ''))
            if item.find('td', 'nsepb bsepb'):
                output['face_value'] = float(item.find('td', 'nsefv bsefv').text.strip().replace(',', ''))
            if item.find('td', 'nsedy bsedy'):
                output['div_yield'] = float(item.find('td', 'nsedy bsedy').text.strip().replace(',', ''))
            if item.find('td', 'nsev20a bsev20a'):
                output['20d_avg_vol'] = float(item.find('td', 'nsev20a bsev20a').text.strip().replace(',', ''))
            if item.find('td', 'nsed20ad bsed20ad'):
                output['20d_avg_delivery'] = float(item.find('td', 'nsed20ad bsed20ad').text.strip().replace(',', ''))
            
        return output
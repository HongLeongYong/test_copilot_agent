import requests
from bs4 import BeautifulSoup

def fetch_exchange_rates():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'title': '牌告匯率'})
        rows = table.find_all('tr')

        exchange_rates = []
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) > 0:
                currency = cols[0].find('div', {'class': 'visible-phone'}).text.strip()
                cash_buy = cols[1].text.strip()
                cash_sell = cols[2].text.strip()
                spot_buy = cols[3].text.strip()
                spot_sell = cols[4].text.strip()
                exchange_rates.append({
                    'currency': currency,
                    'cash_buy': cash_buy,
                    'cash_sell': cash_sell,
                    'spot_buy': spot_buy,
                    'spot_sell': spot_sell
                })
        return exchange_rates
    else:
        print("Failed to fetch exchange rates.")
        return []

if __name__ == "__main__":
    rates = fetch_exchange_rates()
    for rate in rates:
        print(rate)
import requests
import bs4 as bs
#from string import split
from time import asctime

valet1 = "https://blockchain.info/address/115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn"
valet2 = "https://blockchain.info/address/12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw"
valet3 = "https://blockchain.info/address/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94"
exchange_url = "http://www.xe.com/currency/xbt-bitcoin"
all_valets = [valet1, valet2, valet3]


def wannacry_calc(url_list):
	bitcoin_list = []
	victims_list = []
	for valet in url_list:
		s = requests.get(valet)
		sauce = s.text
		soup = bs.BeautifulSoup(sauce, "lxml")
		for table in soup.find_all(id="total_received"):
			full = table.string
			btc = full.string.split(" ")
			bitcoin_list.append(float(btc[0]))
		for table in soup.find_all(id="n_transactions"):
			victims_list.append(int(table.string))
	print_func(bitcoin_list, victims_list)


def print_func(btc_list, victims_list):
	print("\n  ----WannaCry Ransomware earnings tracker----\n")
	get_date()
	print("\tValet\tBitcoins\tVictims")
	print("\t#1\t%.4f\t\t%d" % (btc_list[0], victims_list[0]))
	print("\t#2\t%.4f\t\t%d" % (btc_list[1], victims_list[1]))
	print("\t#3\t%.4f\t\t%d" % (btc_list[2], victims_list[2]))
	print("\n\tTotals:")
	print("\t%.4f BTC - %.2f EURO\n\t%d Victims paid\n" %(sum(btc_list), get_rate() * sum(btc_list), sum(victims_list)))
	print("\tBitcoin price: %s" % (get_rate()))
	print("")

	return


def get_rate():
	s = requests.get(exchange_url)
	sauce = s.text
	soup = bs.BeautifulSoup(sauce, "lxml")
	cell = soup.find_all("td", {"class": "rateCell"})[1]
	cell = float(cell.string)
	return cell


def get_date():
	date = asctime()
	date = date.split(" ")
	print("\t\t%s %s %s" % (date[4], date[1], date[2]))
	print("\t\t   %s\n" % (date[3][:-3]))
	return


wannacry_calc(all_valets)

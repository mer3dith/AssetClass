pre_growth = ['ADA', 'CHZ', 'DOT']
emerging = ['AVAX', 'CELO', 'MATIC', 'BNB', 'CRO', 'FTM', 'PALM']
mature = ['BTC', 'ETH', 'DOGE', 'BCH', 'BSV', 'DASH', 'EOS', 'ETC', 'SOL', 'TRX', 'XRP', 'ZEC']

ticker = input("Please enter a crypto asset symbol: ")



if ticker.upper() in pre_growth:
    asset_class = 'Pre-Growth'
    print(f"The asset tier for {ticker.upper()} is: {asset_class}.")
    print("This asset is supported by address screening and has limited transaction monitoring support. No support in Storyline or Reactor.")
elif ticker.upper() in emerging:
    asset_class = 'Emerging'
    print(f"The asset tier for {ticker.upper()} is: {asset_class}.")
    print("This asset is supported by address screening, KYT- except indirect exposure alerts, and Storyline. No support for Reactor.")
elif ticker.upper() in mature:
    asset_class = 'Mature'
    print(f"The asset tier for {ticker.upper()} is: {asset_class}.")
    print("This asset is fully supported by all of our products, including Reactor.")
else:
    asset_class = 'N/A: this asset is not in one of the currently supported tiers'


def get_data(value):
	r = requests.get(bitstamp_URL % value)
	file_json = json.loads(r.text)
	df = pd.DataFrame(file_json, index=[0])
	df.to_csv (r'CryptoTable.csv', index = False, header=True)

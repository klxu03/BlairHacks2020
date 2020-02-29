from os import getenv 
from dotenv import load_dotenv
from requests import get
import urllib.parse

def product_info(ingr=None, upc=None):
	"""Return a JSON object with the nutritional info of the given food.
	Relies on the Edamam API, with API keys in .env.
	Based on either the name of the file or the barcode (Universal Product Code)."""
	load_dotenv() # load app id, key
	url = "https://api.edamam.com/api/food-database/parser"
	payload = {
		"app_id": getenv("FOOD_DATA_APP_ID"),
		"app_key": getenv("FOOD_DATA_APP_KEY"),
	}
	if ingr: payload["ingr"] = ingr # 'ingr' is a parameter if it is given as input
	if upc: payload["upc"] = upc # same with 'upc'
	params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
	response = get(url, params=params)
	return response.json()

#print(product_info(ingr="1 large apple"))
#print(product_info(upc="0857183005120"))
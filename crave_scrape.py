import requests
import random
import time
from bs4 import BeautifulSoup

print()
print("-------------------------------")
print("-------  Craver Scraper -------")
print("-------------------------------")
print()

food_path = input("\nWhachu cravin'? ")
food_path = food_path.replace(' ', '+')

geo_path = input("Where you at? ")
geo_path = geo_path.replace(' ', '+')


base_url = "https://www.yellowpages.com/search?search_terms="+ food_path +"&geo_location_terms="
url      = base_url + geo_path + "%2C+CA"

print('\n...rolling the magical food dice...')

html   = requests.get(url)
soup   = BeautifulSoup(html.content, "html.parser")
g_data = soup.find_all("div", {"class":"info"})

names     = ['']*30
addresses = ['']*30

i = 0
for item in g_data:
	address = ''
	try:
		if i < 30:
			names[i] = item.contents[0].find_all("a", {"class":"business-name"})[0].text
	except:
		pass
	if i < 30:
		try:
			address += item.find("p", class_="adr").find_all("span")[0].text + ', '
		except:
			pass
		try:
			address += item.find("p", class_="adr").find_all("span")[1].text
		except:
			pass
		try:
			address += item.find("p", class_="adr").find_all("span")[-2].text + ' '
		except:
			pass
		try:
			address += item.find("p", class_="adr").find_all("span")[-1].text
		except:
			pass
		addresses[i] = address
	i += 1

roll_again = 'y'
while(roll_again.lower() == 'y'):
    j = random.randint(0,29)

    print('\nRestaurant:', names[j])
    print('Address:   ', addresses[j],'\n\n')
    roll_again = input("Already been here?\nRoll again by typing 'y': ")

from plyer import notification as nt
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
	nt.notify(
		title= title,
		message= message,
		app_icon= "O://Python_Tutorials//corona.ico",
		timeout= 1000
	)

def getData(url):
	r = requests.get(url)
	return r.text

if __name__ == "__main__":

	htmlData = getData("https://www.mohfw.gov.in/")


	soup = BeautifulSoup(htmlData, 'html.parser')

	myDataStr = ""
	for tr in soup.find_all('tbody')[7].find_all('tr'):
		myDataStr += tr.get_text()
	myDataStr = myDataStr[1:]
	itemList = myDataStr.split("\n\n")

	states = ['Delhi', 'Total number of confirmed cases in India']
	for item in itemList[0:28]:
		dataList = item.split('\n')
		if dataList[0] in states:
			nTitle = 'Cases of CoronaVirus Live Count'
			nText = f"{dataList[0]}: {dataList[1]}"
			notifyMe(nTitle, nText)

		


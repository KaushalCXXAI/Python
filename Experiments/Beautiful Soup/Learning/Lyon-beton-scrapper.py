from bs4 import BeautifulSoup
import requests
url = "https://lyon-beton.com/"
print("code:", requests.get(url))
content = requests.get(url).text
soup = BeautifulSoup(content,'lxml')
data = soup.find("div", class_="slider js-slider").prettify()
print(data)
file = open("slider js-slider.html","w")
file.write(data)
file.close()
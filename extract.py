import requests
from bs4 import BeautifulSoup

def getlinks(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    anchor_tags = soup.find_all('a')
    
    links = [tag.get('href') for tag in anchor_tags if tag.get('href')]

    return links

def savelinks(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(f"{link}\n")

def main(url, filename):
    links = getlinks(url)
    savelinks(links, filename)
    print(f"Found {len(links)} links. Links saved to {filename}")

if __name__ == "__main__":
    url = 'https://flocard.app/' 
    filename = 'links.txt' 
    main(url, filename)

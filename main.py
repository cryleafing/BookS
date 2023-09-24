import requests
from bs4 import BeautifulSoup

# URL of the book site
url = 'https://books.toscrape.com'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the book listings (assuming multiple books are on the page)
    book_listings = soup.find_all('article', class_='product_pod')

    # Loop through the book listings and extract information
    for book in book_listings:
        # the book title
        title = book.find('h3').find('a')['title']

        # the book URL
        book_url = book.find('h3').find('a')['href']

        # get the star rating class
        star_rating = book.find('p', class_='star-rating')['class'][1]

        # print all of the info needed
        print(f'Title: {title}')
        print(f'Book URL: {book_url}')
        print(f'Star Rating: {star_rating}')
        print()

else:
    print('Cannot retrieve the webpage.')
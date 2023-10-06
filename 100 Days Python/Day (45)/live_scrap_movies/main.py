import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

# Send a GET request to the website
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all h3 elements with the specified class
    movie_elements = soup.find_all('h3', class_='listicleItem_listicle-item__title__hW_Kn')

    # Reverse the list of movie elements
    movie_elements.reverse()

    # Create or open the movies.txt file for writing
    with open('movies.txt', 'w', encoding='utf-8') as file:
        # Loop through the reversed movie elements and write them to the file
        for movie in movie_elements:
            movie_title = movie.text.strip()  # Get the text content of the h3 element
            file.write(movie_title + '\n')  # Write the movie title to the file

    print("Movies scraped and saved to movies.txt in ascending order.")
else:
    print("Failed to retrieve the website.")

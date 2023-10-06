import csv

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate  # Import the tabulate library

# Get user input for the date in YYYY-MM-DD format
date = input("Enter the date (YYYY-MM-DD): ")

# Construct the URL based on the user's input
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# Send a GET request to the Billboard Hot 100 chart URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all song elements using the updated <h3> tag
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    artist_name_spans = soup.select("li ul li span")
    artist_names = [artist.getText().strip() for artist in artist_name_spans]
    selected_artists = [artist_names[i] for i in range(0, len(artist_names), 7)]
    # print(song_names)
    # print(selected_artists)
    table_data = [(i + 1, song, artist) for i, (song, artist) in enumerate(zip(song_names, selected_artists))]
    table_headers = ["Number", "Song Title", "Artist Name"]
    print(tabulate(table_data, headers=table_headers, tablefmt="pretty"))

       # Save the table to a CSV file with the specified date format
    with open(f"{date}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Number", "Song Title", "Artist Name"])
        # Write the data rows
        writer.writerows(table_data)

else:
    print("Failed to retrieve the Billboard Hot 100 chart for the specified date.")

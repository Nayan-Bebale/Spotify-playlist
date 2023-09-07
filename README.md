# Billboard 100 Playlist Generator
This Python script creates a Spotify playlist of the top 100 songs on the Billboard 100 chart for a specified date. It first scrapes the Billboard website to get the list of songs, then uses the Spotify API to search for the songs and add them to a new playlist.

## Requirements
Python 3.7+
Requests
BeautifulSoup4
spotipy
SpotifyOAuth
Installation
### 1. Clone the repository:
<p>git clone https://github.com/[your-username]/billboard-100-playlist-generator.git</p>


### 2. Install the dependencies:

pip install -r requirements.txt

## Usage
To create a playlist of the top 100 songs on the Billboard chart for a specified date, run the following command:

python trial.py [date]

where [date] is the date of the Billboard chart in the format YYYY-MM-DD. For example, to create a playlist of the top 100 songs on the Billboard chart for January 1, 2023, you would use the following command:

python trial.py 2023-01-01

## Contributing
Contributions are welcome! Please open an issue or pull request if you have any improvements or suggestions.

## Look's like
![Image alt text](Screenshot (3).png width="100")

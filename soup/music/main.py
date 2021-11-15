"""Scraping music charts based on date input"""
from icecream import ic
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
import spotipy
from dotenv import load_dotenv
import os

def main():
    # get date input from the user
    date_check = input("Date to listen (yyyy-mm-dd) ?? ").strip()

    # get spotify credentials
    load_dotenv()
    ChartPlaylist(date_check).track_uris()



@dataclass
class ChartPlaylist:
    date : str

    def soup_parser(self):
        """parse the billboard.com url for inputed date
        Returns:
            :param m_dict : rank:[artist:song] dict
            :type m_dict : dict
        """
        date_check = self.date

        # billboard.com url
        url = f'https://www.billboard.com/charts/hot-100/{date_check}'

        # get response
        response = requests.get(url)
        webpage = response.text

        # parsed soup object
        soup = BeautifulSoup(webpage,'html.parser')

        # get container
        chart_container = soup.find(name='ol',class_='chart-list__elements')

        # get rank
        rank_list = [int(rank.getText().strip()) for rank in soup.find_all(name="span", class_="chart-element__rank__number")]

        # get songs
        song_list = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]

        # get artists
        artist_list = [artist.getText() for artist in soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")]

        # create dictionary with key = rank and value = [artist,song]
        m_dict = {}
        for rank in rank_list:
            m_dict[rank] = [artist_list[rank-1],song_list[rank-1]]

        return m_dict
    
    def spotify_creds(self):
        """Use spotipy module and saved credentials to create a spotify object that can retrieve song uris
        Returns:
            :param sp : spotify object for specified credentials and redirect_uri
            :type sp : Class"""

        # get credentials from environment variables in .env file
        client_id_ = os.environ.get('CLIENT_ID')
        client_secret_ = os.environ.get('CLIENT_SECRET')
        redirect_uri_ = os.environ.get('REDIRECT_URI')

        # create spotify object and create token
        sp = spotipy.Spotify(
            auth_manager= spotipy.oauth2.SpotifyOAuth(
                client_id= client_id_, 
                client_secret= client_secret_, 
                redirect_uri= redirect_uri_, 
                scope="playlist-modify-private", 
                cache_path="token.txt",
                show_dialog=True,
            )
        )
        return sp
      
    def track_uris(self):
        
        # get top-100 dict
        music_dict = self.soup_parser()

        # get spotify object
        sp = self.spotify_creds()

        # possible track year
        track_year = int(self.date.split('-')[0])

        track_uris = []

        for rank in music_dict:
            result = sp.search(q=f"artist:{music_dict[rank][0]} track:{music_dict[rank][1]} year:{str(track_year)}")
            
            try: 
                uri = result['tracks']['items'][0]['uri']
                track_uris.append(uri)
            
            except IndexError:
                try:
                    result = sp.search(q=f"track:{music_dict[rank][1]}")
                    uri = result['tracks']['items'][0]['uri']
                    track_uris.append(uri)
                
                except IndexError:
                    ic(f'Unable to find track:{music_dict[rank][1]}')

        return track_uris
        


if __name__ == '__main__':
    main()
    


# Import module
import requests

# Create Soundcharts API client
class SoundchartsClient(object):
    base_url = "https://customer.api.soundcharts.com/api/"

    # Constructor
    def __init__(self, x_app_id, x_api_key):
        self.headers = {
            'x-app-id': x_app_id,
            'x-api-key': x_api_key
        }

    # Get resource generic function
    def get_resource(self, endpoint, params=None, data=None):
        url = f"{self.base_url}{endpoint}"

        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code not in range(200,299):
            return{}
        return response.json()
    
    # Get Spotify playlists by type
    def get_playlists_by_type(self, offset=0, limit=100, type='editorial'):
        endpoint = f"v2.20/playlist/by-type/spotify/{type}"

        params = {
            'countryCode': 'FR',
            'offset': offset,
            'limit': limit,
            'sortBy': 'audience',
            'sortOrder': 'desc'
        }

        return self.get_resource(endpoint, params=params)
    
    # Get Spotify playlist's tracklist dates
    def get_playlist_tracklist_dates(self, endDate='', period=90, offset=0, limit=100, playlist_id='playlist_id'):
        endpoint = f"v2.20/playlist/{playlist_id}/available-tracklistings"

        params = {
            'endDate': endDate,
            'period': period,
            'offset': offset,
            'limit': limit
        }

        return self.get_resource(endpoint, params=params)
    
    # Get Spotify playlist's tracklist by date
    def get_playlist_tracklist_by_date(self, offset=0, limit=100, playlist_id='playlist_id', date='date'):
        endpoint = f"v2.20/playlist/{playlist_id}/tracks/{date}"

        params = {
            'offset': offset,
            'limit': limit
        }

        return self.get_resource(endpoint, params=params)
    
    # Get track's Spotify streams by date
    def get_track_streams_by_date(self, startDate='', endDate='', track_id=''):
        endpoint = f"v2/song/{track_id}/audience/spotify"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)
    
    # Get track's metadata
    def get_track_metadata(self, track_id='track_id'):
        endpoint = f"v2.25/song/{track_id}"

        return self.get_resource(endpoint)
    
    # Get artist's first track date
    def get_first_track_date(self, offset=0, limit=100, sortBy='releaseDate', sortOrder='asc', artist_id=''):
        endpoint = f"v2.21/artist/{artist_id}/songs"

        params = {
            'offset': offset,
            'limit': limit,
            'sortBy': sortBy,
            'sortOrder': sortOrder
        }

        return self.get_resource(endpoint, params=params)

    # Get artist's Spotify streams by date
    def get_artist_streams_by_date(self, startDate='', endDate='', artist_id=''):
        endpoint = f"v2/artist/{artist_id}/streaming/spotify/listening"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)

    # Get playlist's followers by date
    def get_playlist_followers_by_date(self, startDate='', endDate='', playlist_id='playlist_id'):
        endpoint = f"v2.20/playlist/{playlist_id}/audience"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)
    
    # Get artist's first album
    def get_first_album_date(self, offset=0, limit=100, sortBy='releaseDate', sortOrder='asc', artist_id=''):
        endpoint = f"v2.34/artist/{artist_id}/albums"

        params = {
            'offset': offset,
            'limit': limit,
            'sortBy': sortBy,
            'sortOrder': sortOrder
        }

        return self.get_resource(endpoint, params=params)
    
    # Get playlist_followers by date
    def get_playlist_followers_by_date(self, startDate='', endDate='', playlist_id='playlist_id'):
        endpoint = f"v2.20/playlist/{playlist_id}/audience"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)
    
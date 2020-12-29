from googleapiclient.discovery import build

api_key = 'AIzaSyBtBWY7xE-WWBls5G7we0sCvjoMlq2PyVo'

youtube_api = build('youtube', 'v3', developerKey=api_key)
search_terms = "airwavemusic"
results = youtube_api.search().list(q=search_terms, part='snippet', type='video',
                                    order='viewCount', maxResults=50).execute()
publishedAt = results['items'][0]['snippet']['publishedAt']
print(publishedAt)

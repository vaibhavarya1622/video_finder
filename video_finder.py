import pandas as pd
from googleapiclient.discovery import build


def get_the_news(api_key):
    """This function gets the result as a pandas dataframe """
    youtube, api = search_the_api(api_key)
    df = pd.DataFrame(columns=('index','Title', 'link', 'publishAt', 'channel Title'))

    for i, item in enumerate(api['items']):
        index = i
        title = item["snippet"]["title"]
        link = "https://www.youtube.com/watch?v="+item["id"]
        publishAt = item["snippet"]["publishedAt"]
        channel_title = item["snippet"]["channelTitle"]
        df.loc[i] = [index, title, link, publishAt, channel_title]

    print_results(df)


def print_results(df):
    """The function prints the dataframe """
    for i in range(5):
        video=df.iloc[i]
        title=video['Title']
        link=video['link']
        publishAt=video['publishAt']
        channel_title=video['channel Title']
        print("Video #{}:\nThe video '{}' , from a channel {} published at {} and can be viewed here: {}\n"\
        .format(i+1, title,channel_title,publishAt, link))
        print("==========================\n")




def search_the_api(api_key):
    """This function fetch the results from the api and return it to get_the_news"""
    youtube = build('youtube', 'v3', developerKey=api_key)
    youtube_api = youtube.videos().list(part='snippet,id,status', videoCategoryId='10',
                                        chart='mostPopular', regionCode='PE').execute()
    return youtube, youtube_api

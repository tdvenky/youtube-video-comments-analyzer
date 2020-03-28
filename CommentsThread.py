from googleapiclient.discovery import build


def main():
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    youtube = build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId="DSxhgejP0u4"
    )

    response = request.execute()

    comments = []
    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            if item['snippet']['totalReplyCount'] > 0:
                sub_comments = item['replies']['comments']
                for sub_item in sub_comments:
                    comments.append(sub_item['snippet']['textOriginal'])
            comments.append(comment)

        if 'nextPageToken' in response:
            response = youtube.commentThreads().list(
                part="snippet,replies",
                pageToken=response['nextPageToken'],
                videoId="DSxhgejP0u4"
            ).execute()
        else:
            break

    # print(comments)
    print(len(comments))


if __name__ == '__main__':
    main()

import requests
from django.shortcuts import render


def instaloader(request):
    if not request.GET:
        download_url = None
    else:
        link = request.GET['link']
        print(link)
        download_url = get_download_url(link)
        print(download_url)

    return render(request, 'instagram/instagram_page.html', context={'download_url': download_url})


def get_download_url(link):
    link = link.split('?')[0]
    try:
        link_for_json = '{}?__a=1'.format(link)
        request_json = requests.get(link_for_json)
    except Exception as err:
        print(err)
        return False

    if int(request_json.status_code) != 200:
        return False

    media = request_json.json()['graphql']['shortcode_media']
    list_download_urls = []
    if 'edge_sidecar_to_children' in media:
        posts_json = media['edge_sidecar_to_children']['edges']
        for post_json in posts_json:
            if '.mp4' in str(post_json):
                post_download_url = post_json['node']['video_url']
            else:
                post_download_url = post_json['node']['display_url']
            list_download_urls.append(post_download_url)
    else:
        if 'video_url' in media:
            post_download_url = media['video_url']
        else:
            post_download_url = media['display_url']
        list_download_urls.append(post_download_url)

    return list_download_urls

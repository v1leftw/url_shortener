import requests
import argparse
import os
import json
import sys
from dotenv import load_dotenv
load_dotenv()


def get_args():
    parser = argparse.ArgumentParser(
        description='Bitlink to get click counts or URL to make it short'
    )
    parser.add_argument(
        'url',
        help='URL. Example: http://bit.ly/2K0kpnk'
    )
    return parser.parse_args()


def get_headers():
    token = os.getenv('token')
    headers = dict()
    headers['Authorization'] = 'Bearer {}'.format(token)
    headers['Content-Type'] = 'application/json'
    return headers


def get_data_from_the_server(method, url, headers=get_headers(), data=None):
    response = None
    try:
        response = requests.request(
            method,
            url,
            headers=headers,
            json=data,
            timeout=3
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if is_json(response.text):
            if response.json()['message'] == 'NOT_FOUND':
                return None
        raise
    return response


def get_short_link(url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    data = dict()
    data['long_url'] = url
    response = get_data_from_the_server('post', api_url, data)
    return response.json()['link']


def get_clicks(bitlink):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(
        bitlink
    )
    response = get_data_from_the_server('get', api_url)
    return response.json()['total_clicks']


def is_bitlink(bitlink):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(bitlink)
    response = get_data_from_the_server('get', api_url)
    return bool(response)


def is_json(data):
    try:
        json_data = json.loads(data)
    except ValueError:
        return False
    return True


def get_result(url):
    try:
        if is_bitlink(url):
            return 'Clicks count: {}'.format(get_clicks(url))
        else:
            return 'Your link: {}'.format(get_short_link(url))
    except requests.exceptions.HTTPError as http_error:
        return http_error
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.RequestException
    ) as conn_error:
        return 'Connection error \n {}'.format(conn_error)
    except:
        return 'Something very bad happened \n {}'.format(sys.exc_info()[1])


if __name__ == '__main__':
    url = get_args().url
    print(get_result(url))

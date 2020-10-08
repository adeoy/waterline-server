import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


def remove_space(val, space=' ', default=''):
    val = val or default
    return space.join(val.split())


def clean_str(val, default=''):
    return remove_space(val, default=default)


def clean_int(val, default=0):
    if val is None:
        return default
    val = remove_space(val)
    val = re.sub('[^0-9]', '', val)
    if len(val) == 0:
        return default
    return int(val)


def clean_float(val, default=0.0):
    if val is None:
        return default
    val = remove_space(val)
    val = re.sub('[^0-9\.]', '', val)
    if len(val) == 0:
        return default
    return float(val)


def make_safe_request(url, method='GET', ok_soup=True, data=None, headers=None, session=None, cookies=None,
                      redirection=0):
    if len(url) == '':
        return None

    if session is None:
        session = requests.session()

    session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, ' \
                                        'like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    if headers:
        for k, v in headers.items():
            session.headers[k] = v

    if cookies:
        session.cookies = cookies

    try:
        if method == 'GET':
            resp = session.get(url)
        elif method == 'HEAD':
            resp = session.head(url)
        elif method == 'POST':
            resp = session.post(url, data=data)
        else:
            print(f'[ERR] --> method: {method} | {url}')
            return None

        code = resp.status_code
        if code == 200:
            if ok_soup:
                return BeautifulSoup(resp.text, 'lxml')
            else:
                return resp
        elif redirection and (code == 301 or code == 302):
            redirection -= 1
            url = resp.headers.get('Location', '')
            return make_safe_request(url, method=method, ok_soup=ok_soup, data=data, headers=headers,
                                     session=session, cookies=cookies, redirection=redirection)
        else:
            print(f'[ERR] --> status_code: {code} | {url}')
            return None
    except Exception as e:
        print(f'[ERR] --> {url}')
        print(e)
        return None


def image_from_url_is_valid(url):
    resp = make_safe_request(url, method='HEAD', ok_soup=False)
    if resp is None:
        print(f'Not valid image: {url}')
        return False
    else:
        headers = resp.headers
        content_type = headers.get('Content-Type', '')
        if 'image' in content_type:
            return True
        else:
            print(f'Not valid image: {content_type}')


def get_safe_data(item, get='get_text', default=''):
    if item:
        if get == 'get_text':
            return item.get_text()
        else:
            return item.get(get, default)
    return default


def get_safe_item(soup, css_select, get='get_text', default=''):
    temp = soup.select_one(css_select)
    return get_safe_data(temp, get, default)


def get_safe_items(soup, css_select, idx=None, get='get_text', default=''):
    temp = soup.select(css_select)
    if temp:
        n = len(temp)
        if idx is not None and idx < n:
            return get_safe_data(temp[idx], get, default)
        else:
            return [get_safe_data(subitem, get, default) for subitem in temp]
    else:
        if idx is not None:
            return ''
        else:
            return []


def get_current_date():
    return datetime.now().isoformat()[:10]

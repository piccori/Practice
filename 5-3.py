import requests

OECD_ROOT_URL = 'http://stats.oecd.org/sdmx-json/data'


def make_OECD_request(dsname, dimensions, params=None, roo_dir=OECD_ROOT_URL):
    if params is None:
        params = {}

    dim_args = ['+'.join(d) for d in dimensions]
    dim_str = '.'.join(dim_args)
    url = roo_dir + '/' + dsname + '/' + dim_str + '/all'
    print('Requesting URL: ' + url)
    return requests.get(url, params=params)


reaponse = make_OECD_request('QNA', (('USA', 'AUS'), ('GDP', 'B1_GE'), ('CUR', 'VOBARSA'), ('Q')), {
                             'startTime': '2009-Q1', 'endTime': '2010-Q1'})

if reaponse.status_code == 200:
    json = reaponse.json()
    key = json.keys()
    print(json['header'])
    print('--------------------\n')
    print(json['dataSets'])
    print('--------------------\n')
    print(json['structure'])
    print(json.keys())
else:
    print(reaponse.status_code)


REST_EU_ROOT_URL = 'http://restcountries.eu/rest/v1'


def REST_country_request(field='all', name='', params=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    if params is None:
        params = {}
    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')
    url = '%s/%s/%s' % (REST_EU_ROOT_URL, field, name)
    print('Reqursting URL: ' + url)
    response = requests.get(url, params=params, headers=headers)
    if not response.status_code == 200:
        raise Exception('Request failed with status code ' +
                        str(response.status_code))
    return response


response = REST_country_request('currency', 'usd')
json = response.json()
for key, value in json[0].items():
    print(key, str(value).encode('UTF-8'))

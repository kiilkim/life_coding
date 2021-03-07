# Python 샘플 코드 #


from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://apis.data.go.kr/B551172/UterineCancerRegistryMetaInfoService/getUterineCancerRegistryMetaInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('resultType') : 'JSON' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)
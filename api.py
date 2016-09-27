from secrets import key

url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=aapl&key="

requests.get(url + key)
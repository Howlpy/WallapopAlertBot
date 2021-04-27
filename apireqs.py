import requests,json

def basicSearch(keyword):
    url = "https://api.wallapop.com/api/v3/general/search?&keywords={}&language=es_ES&order_by=newest&start=0&step=4".format(keyword.replace(' ','+'))
    res = requests.get(url).json()
    return res
    '''for i in res['search_objects']:
        title = i['title']
        cost = i['price']
        print(title + " --- " + str(cost))'''









if __name__ == "__main__":
    pass
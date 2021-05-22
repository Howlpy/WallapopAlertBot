import requests,json


def remove_duplicates(products):
    array = []
    for x in products:
        if x not in array:
            array.append(x)
    return array

def basicSearch(keyword,price):
    url = "https://api.wallapop.com/api/v3/general/search?density_type=20&experiment=variation_query_expansion_v2&filters_source=quick_filters&keywords={}&language=es_ES&max_sale_price={}&start=0&step={}"
    products = []
    responses = []
    for i in range(1,10):
        res = requests.get(url.format(keyword.replace(' ','+'),price,i)).json()
        try:
            responses.append(res)
        except Exception as e:
            print(e)
            break
    responses = remove_duplicates(responses)
    for res in responses:
        for i in res['search_objects']:
            if keyword not in i['title'] or i['price'] == 0:
                pass
            else:
                title = i['title']
                cost = i['price']
                products.append([title,cost])
    return products









if __name__ == "__main__":
    pass
class GofoodEndpointsMixin(object):
    def gofood_deals(self):
        return self._call_api("gofood/v1/deals")
    
    def gofood_consumer_v3_restaurants(self, collection='NEAR_ME', **kwargs):
        """
        :param collection: NEAR_ME, NEW_MERCHANT, BEST_SELLER, 
            PARTNERS (promo antar), 24_HOURS, AFFORDABLE_PRICE, MOST_LOVED
        :param kwargs: See below
        :Keyword Arguments:
            - **avg_rating_min**: value: `4.5` or `4`
            - **page**
            - **tag**: PROMO
            - **open_now**: 'true'
            - **price_level**: 1=under 16k, 2=16k-40k, 3=40k-100k, 4=more than 100k. 
        :return:
        """
        data = {
            'campaign': 'gofood:platter:food:shortcut',
            'collection': collection,
            'filter_enabled': 'true',
            'source': 'SHUFFLE'
        }
        data.update(kwargs)
        return self._call_api("gofood/consumer/v3/restaurants", params=data)

    def gofood_filters(self):
        data = {
            'type': 'RESTAURANT_LIST'
        }
        return self._call_api("gofood/consumer/v1/filters", params=data)
import utils.common as com


class Scraper:
    def __init__(self, ses):
        self.ses = ses

    @staticmethod
    def extract_data(info_items, product):
        data = {}
        for k, v in info_items.items():
            css = v['css']
            _type = v['type']
            get = v['get']

            if _type == 'str' or _type == 'int' or _type == 'float':
                val = com.get_safe_item(product, css, get)
            else:
                val = com.get_safe_items(product, css)

            if _type == 'int':
                data[k] = com.clean_int(val)
            elif _type == 'float':
                data[k] = com.clean_float(val)
            elif _type == 'str_list':
                data[k] = val
            else:
                data[k] = com.clean_str(val)
        return data

    def extract_products(self, url_page, products_css, info_items, css_next_page):
        """
        Extract the products found in HTML website

        Parameters:
            url_page (str): Webpage URL
            products_css (str): CSS Selector that identifies all product container
            info_items (dict): Contains CSS Selector of the data to extract
            css_next_page (str): CSS Selector that identifies the link to the next page (pagination)
        """

        print(f'  - {url_page}')
        soup = com.make_safe_request(url_page, session=self.ses)
        if soup is None:
            return

        products = soup.select(products_css)
        next_page = com.get_safe_item(soup, css_next_page, 'href')

        for product in products:
            data = self.extract_data(info_items, product)
            if data.get('url', '') == 0:
                continue
            yield data

        if next_page:
            yield from self.extract_products(next_page, products_css, info_items, css_next_page)

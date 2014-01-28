import re
import mechanize
from bs4 import BeautifulSoup


class AllegroError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def allegro_api(product, external_data={}):
    try:
        browse = mechanize.Browser()
        url = "http://www.allegro.pl/"
        browse.open(url)
    except mechanize.URLError:
        raise AllegroError("No connection")

    browse.select_form(nr=0)
    browse.form['string'] = product
    browse.submit()

    browse.select_form(nr=1)
    for label, value in external_data.items():
        browse.form[str(label)] = [str(value)]
    browse.submit()

    allegro_html = browse.response().read()

    soup = BeautifulSoup(allegro_html)
    proposed_product = soup.find('article')

    if proposed_product is None:
        raise AllegroError("No product")

    price = proposed_product.find(
        'span',
        {'class': 'buy-now dist'}
    )
    price = price.text[11:-3]
    price = float(price.replace(',', '.').replace(' ', ''))

    img_div = proposed_product.find('div', {'class': 'photo'})
    img_urls = img_div.get('data-img')
    regex = re.compile('\[.*,"(.*)"\]')
    img = regex.findall(img_urls)[0]

    url_path = proposed_product.find('a')['href']
    full_url = ''.join(["http://www.allegro.pl", url_path])

    return {
        'price': price,
        'url': full_url,
        'img': img,
    }

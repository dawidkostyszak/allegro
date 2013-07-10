import mechanize
from bs4 import BeautifulSoup


class AllegroError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def allegro_api(product):
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
    browse.form['offerTypeBuyNow'] = ['1']
    browse.form['standard_allegro'] = ['1']
    browse.form['startingTime'] = ['']
    browse.form['endingTime'] = ['']

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

    url_path = proposed_product.find('a')['href']

    full_url = ''.join(["http://www.allegro.pl", url_path])

    return price, full_url

import mock
import unittest
from lib.allegro_module import *


class SerwerTestCase(unittest.TestCase):

    @mock.patch('mechanize.Browser')
    def test_api_response(self, Browser):

        f = open('./fixtures/allegro_response', 'r')
        data = f.read()
        f.close()

        browse = Browser()
        browse.response().read.return_value = data

        price, url = allegro_api('laptop')

        self.assertEqual(
            price,
            138.00
        )

        self.assertEqual(
            url,
            'www.allegro.pl/drukarka-do-laptopa-hp-460-cb-przebieg-5000str-i3348727701.html'
        )

    @mock.patch('mechanize.Browser')
    def test_error_network(self, Browser):

        f = open('./fixtures/allegro_no_item_response', 'r')
        data = f.read()
        f.close()

        browse = Browser()
        browse.response().read.return_value = data

        self.assertRaises(
            AllegroError,
            allegro_api,
            'somethingproduct'
        )


if __name__ == "__main__":
    unittest.main()

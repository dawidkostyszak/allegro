import mock
import unittest
import lib


class SerwerTestCase(unittest.TestCase):

    @mock.patch('lib.mechanize.Browser')
    def test_api_response(self, Browser):

        f = open('allegro_response', 'r')
        data = f.read()
        f.close()

        browse = Browser()
        browse.response().read.return_value = data

        price, url = lib.allegro_api('laptop')

        self.assertEqual(
            price,
            138.00
        )

        self.assertEqual(
            url,
            'www.allegro.pl/drukarka-do-laptopa-hp-460-cb-przebieg-5000str-i3348727701.html'
        )

    @mock.patch('lib.mechanize.Browser')
    def test_error_network(self, Browser):

        f = open('allegro_no_item_response', 'r')
        data = f.read()
        f.close()

        browse = Browser()
        browse.response().read.return_value = data

        self.assertRaises(
            lib.AllegroError,
            lib.allegro_api,
            'aksgfkagfkjsafgak'
        )


if __name__ == "__main__":
    unittest.main()

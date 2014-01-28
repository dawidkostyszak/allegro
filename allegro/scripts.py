import sys
import argparse
from lib import allegro_api


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("product", nargs=1, help="product")
    parser.add_argument("external_data", nargs=2, help="external_data")

    args = parser.parse_args()

    if args.product is None:
        print "lib.py usage: lib.py product external_data(not required)"
    else:
        print allegro_api(args.product[0], args.product[1])

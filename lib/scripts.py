import sys
import argparse
from lib import allegro_api


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("product", nargs=1, help="product")

    args = parser.parse_args()

    if args.product is None:
        print "lib.py usage: lib.py product"
    else:
        print allegro_api(args.product[0])

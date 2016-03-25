
import argparse
from time import sleep

from minipager.pager import alert_if_down

def build_parser():
    """
    Builds the parser for the command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number',
            help='The phone number to send alerts to.',
            type=str,
            required=True)
    parser.add_argument('-p', '--pages',
            help='The web pages to monitor for downtime alerts',
            type=str,
            required=True,
            nargs='+')
    parser.add_argument('-s', '--status-codes',
            help='Status codes considered "up". The complement of this set is considered a down site.',
            type=int,
            required=False,
            default=[200],
            nargs='+')
    return parser


def loop_check_alert(number, pages, codes):
    """
    Alert the given phone numbers if the given pages change their HTTP status to one
    of the given statuses.
    """
    while True:
        print("Polling...")
        alert_if_down(*pages, number=number, allowed_codes=codes)
        sleep(1)


def main():
    parser = build_parser()
    args = parser.parse_args()
    print('Number: {}'.format(args.number))
    print('Pages: {}'.format(', '.join(args.pages)))
    print('Allowed Status Codes: {}'.format(', '.join(map(str, args.status_codes))))
    loop_check_alert(args.number, args.pages, args.status_codes)

if __name__ == '__main__':
    main()

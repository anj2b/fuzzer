import argparse
import discover as d
import test as t
import sys

def main():
    pass

if __name__ == "__main__":
      
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--custom-auth', nargs='?', type=str)
    parent_parser.add_argument('url')
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title='Commands', description='The commands the app can run', dest='cmd')
    """Discover"""
    discover_parser = subparsers.add_parser('discover', parents=[parent_parser])
    discover_parser.add_argument('--common-words', nargs='?', type=str, required=True)

    """Test"""
    test_parser = subparsers.add_parser('test', parents=[parent_parser])
    test_parser.add_argument('--common-words', nargs='?', type=str, required=True)
    test_parser.add_argument('--vectors', nargs='?', type=str, required=True)
    test_parser.add_argument('--sensitive', nargs='?', type=str, required=True)
    test_parser.add_argument('--timeout', nargs='?', type=int, default=500, required=False)

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()

        if args.cmd == 'discover':  
            print("Discovering: " + args.url + "\n")
            d.discover(args)
	
        elif args.cmd == 'test':
            print("Testing on url: " + args.url + "\n")
            res = d.discover(args)
            inputs = res[0]
            browser = res[1]
            t.test(inputs, args, browser)
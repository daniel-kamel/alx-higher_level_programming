#!/usr/bin/python3
'''
7-add_item.py module doc
'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    '''
    main function doc
    '''
    items = []

    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        items.append(arg)

    try:
        json_items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        save_to_json_file(items, 'add_item.json')
    else:
        json_items += items
        save_to_json_file(json_items, 'add_item.json')


if __name__ == '__main__':
    main()

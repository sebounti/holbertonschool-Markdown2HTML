#!/usr/bin/python3


"""
Markdown to HTML Converter
Task 1: convert heading
"""
# Task 0-Start a script
# This script takes two arguments: first is a markdown file name and the
# second is an html output filename
if __name__ == '__main__':

    import sys
    import os.path

    def markdown2html():
        '''markdown2html - converts markdown to html'''
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

sys.exit(0)

#!/usr/bin/python3
"""
Openai terminal interface
"""
import openai
import sys
import json

def load_key(filename):
    """load api key from file
    file must contain openai api key in json string
    """
    if not isinstance(filename, str):
        print('Error: Invalid file name')
        print('Exitin...')
        sys.exit(1)
    try:
        with open(filename, 'r') as fp:
            return json.load(fp)
    except FileNotFoundError:
        print('Error: could not find file key.json')
        print('exiting...')
        sys.exit(1)

def get_result(prompt=''):
    """get Completion from davinci"""
    response = openai.Completion.create(prompt=prompt
                ,model='text-davinci-003'
                ,temperature=0.7
                ,n=1
                ,max_tokens=1700
            )
    return response.choices[0].text


def main():
    """main entry"""
    prompt = ''
    s=''
    openai.api_key = load_key('key.json')
    while 1:
        s = input('? ')
        if s == 'q':
            break
        prompt += '\n' + s
    if prompt != '':
        result = get_result(prompt)
        if sys.argv[1]:
            with open(sys.argv[1], 'w') as fp:
                fp.write(result.strip())
        print(result.strip())


if __name__ == '__main__':
    main()

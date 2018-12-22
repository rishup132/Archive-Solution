import os,json,pprint,requests,validators
from datetime import datetime, timedelta

data = {}

def question_link():
    while True:
        data['question_link'] = input('Enter the question_link : ')

        if validators.url(data['question_link']):
            request = requests.get(data['question_link'])

            if request.status_code != 200:
                print('\nThe question link does not exist.\n')
            else:
                break
        else:
            print('\nThe question link is not a proper URL.\n')

    with open('base.json') as f:
        available_data = json.load(f)

    for i in available_data['questions']:
        if i['question_link'] == data['question_link']:
            print('\nResponse is available in database. Please select another response.\n')
            exit()

def implementation_level():
    temp = ['basic','advance','expert']

    while True:
        data['implementation_level'] = input('Enter the implementation_level : ').lower()

        if data['implementation_level'] not in temp:
            print('\nResponse is not correct. Please try another response.\n')
        else:
            break

def difficulty_level():
    temp = ['easy','medium','hard']

    while True:
        data['difficulty_level'] = input('Enter the difficulty_level : ').lower()

        if data['difficulty_level'] not in temp:
            print('\nResponse is not correct. Please try another response.\n')
        else:
            break

instruction = '\n\nBasic Instructions :\n'
instruction += '\tauthor                : Name of the person who wants to add the problem.\n'
instruction += '\tplatform              : Name of the site where the question exist.\n'
instruction += '\tquestion_name         : Enter the name of the question you want to add as written on site page.\n'
instruction += '\tquestion_link         : Enter the full URL of the question.\n'
instruction += '\timplementation_level  : Enter any of the following == basic, advance, expert\n'
instruction += '\tdifficulty_level      : Enter any of the following == easy, medium, hard\n'
instruction += '\ttags                  : Specify tags to the problem with comma seperated.\n\n'

print(instruction)

data['author'] = input('Name of the author : ').lower()
data['platform'] = input('Name of the platform : ').lower()
data['question_name'] = input('Enter the question_name : ')

question_link()
implementation_level()
difficulty_level()

data['tags'] = input('Enter the tags : ').lower()

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, data['question_name'])

files = ['solution.cpp','summary.txt','details.json']

if not os.path.exists(final_directory):
   os.makedirs(final_directory)

for i in files:
    open(final_directory+'/'+i,'w+')

with open('base.json') as f:
    available_data = json.load(f)

data['submited_time_and_date'] = datetime.now()
# if len(available_data['questions']) == 0:
#     data['id'] = 1
# else:
#     data['id'] = available_data['questions'][-1]['id'] + 1

available_data['questions'].append(data)

with open('base.json', 'w') as outfile:
   json.dump(available_data, outfile, indent=4, sort_keys=True, default=str)

with open(final_directory+'/'+'details.json', 'w') as outfile:
   json.dump(data, outfile, indent=4, sort_keys=True, default=str)
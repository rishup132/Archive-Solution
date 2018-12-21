import os
import json

data = {}

instruction = '\n\nBasic Instructions :\n'
instruction += '\tauthor                : Name of the person who wants to add the problem.\n'
instruction += '\tplatform              : Name of the site where the question exist.\n'
instruction += '\tquestion_name         : Enter the name of the question you want to add as written on site page.\n'
instruction += '\tquestion_link         : Enter the full URL of the question.\n'
instruction += '\timplementation_level  : Enter any of the following == basic, advance, expert\n'
instruction += '\tdifficulty_level      : Enter any of the following == easy, medium, hard\n'
instruction += '\ttags                  : Specify tags to the problem with comma seperated.\n\n'

print(instruction)

data['author'] = input('Name of the author : ')
data['platform'] = input('Name of the platform : ')
data['question_name'] = input('Enter the question_name : ')
data['question_link'] = input('Enter the question_link : ')
data['implementation_level'] = input('Enter the implementation_level : ')
data['difficulty_level'] = input('Enter the difficulty_level : ')
data['tags'] = input('Enter the tags : ')

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, data['question_name'])

files = ['solution.cpp','summary.txt','details.json']

if not os.path.exists(final_directory):
   os.makedirs(final_directory)

for i in files:
    new_file = open(final_directory+'/'+i,'w+')

new_file.write(json.dumps(data))
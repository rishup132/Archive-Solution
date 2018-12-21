import os
import json

data = {}

data['author'] = input('Name of the author : ')
data['platform'] = input('Name of the platform : ')
data['question_name'] = input('Enter the question_name : ')
data['question_link'] = input('Enter the question_link : ')
data['implementation_level'] = input('Enter the implementation_level : ')
data['difficulty_level'] = input('Enter the difficulty_level : ')
data['tags'] = input('Enter the tags with comma seprated : ')

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, data['question_name'])

files = ['solution.cpp','summary.txt','details.json']

if not os.path.exists(final_directory):
   os.makedirs(final_directory)

for i in files:
    new_file = open(final_directory+'/'+i,'w+')

json_data = json.dumps(data)

new_file.write(json_data)
import json 
import os

def fix_json_format(input, output):
    with open(input, 'r', encoding='utf-8') as file:
        content = file.read()
        
    object = content.strip().split('\n')
    
    fixed_objects = []
    
    for obj in object:
        try:
            json_object = json.loads(obj)
            fixed_objects.append(json_object)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON object: {obj}")
    
    with open(output, 'w', encoding='utf-8') as file:
        json.dump(fixed_objects, file, indent=4)


input = './recipes.json'
output = './fixed_recipes.json'

# Check if path exist
if not os.path.exists(input):
    print(f"File {input} does not exist")
    print(f"Current directory: {os.getcwd()}")
    
fix_json_format(input, output)
import pandas as pd
import json
import os

filename = r"C:\Users\liton\OneDrive\Desktop\recipe_scraper\fixed_recipes.json"

# Check if file path exists
if not os.path.exists(filename):
    print ("File does not exist")
    
with open(filename, 'r', encoding='utf-8') as file:
    try:
        data = json.load(file)
        print("JSON is valid.")
    except json.JSONDecodeError as e:
        print("JSON is invalid:", e)

df = pd.read_json(filename)

print(df)
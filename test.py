import json

def generate_field():
    with open("cogs/help.json", "r" , encoding='utf-8') as f:
        help = json.load(f)
    print(help)

generate_field()


import json

if __name__ == '__main__':
    with open('data/recipes_with_nutritional_info.json') as f:
        with open('data/instructions.txt', 'w') as f_out:
            recipes = json.load(f)
            for recipe in recipes:
                for instruction in recipe['instructions']:
                    f_out.write(instruction['text'] + '\n')
            print('finished')

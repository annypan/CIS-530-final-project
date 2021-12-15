import random
import json
import math

if __name__ == '__main__':
    with open('data/recipes_with_nutritional_info.json') as f:
        # with open('data/instructions.txt', 'w') as f_out:
        #     recipes = json.load(f)
        #     for recipe in recipes:
        #         for instruction in recipe['instructions']:
        #             f_out.write(instruction['text'] + '\n')
        #     print('finished')
        lines = []
        recipes = json.load(f)
        for recipe in recipes:
            for instruction in recipe['instructions']:
                lines.append(instruction['text'])
        random.shuffle(lines)
        size = len(lines)
        train_lines = lines[:math.floor(size * 0.8)]
        val_lines = lines[math.floor(size * 0.8):math.floor(size * 0.9)]
        test_lines = lines[math.floor(size * 0.9):]
        with open('data/train.txt', 'w') as f_out:
            for line in train_lines:
                f_out.write(line + '\n\n\n')
        with open('data/valid.txt', 'w') as f_out:
            for line in val_lines:
                f_out.write(line + '\n\n\n')
        with open('data/test.txt', 'w') as f_out:
            for line in test_lines:
                f_out.write(line + '\n\n\n')
        print('finished')

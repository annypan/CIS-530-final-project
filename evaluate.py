import json
from argparse import ArgumentParser


def evaluate(pred_path, ground_truth_path):
    with open(f'data/{ground_truth_path}') as f:
        ground_truth = json.load(f)
        with open(f'predictions/{pred_path}') as f_pred:
            pred = json.load(f_pred)
            total_correct = 0
            total_recalled = 0
            total_ground_truth = 0
            total_predicted = 0
            for ingredient in ground_truth:
                ground_truth_substitutes = ground_truth[ingredient]
                predicted_substitutes = pred[ingredient]
                total_correct += get_num_correct(
                    ground_truth_substitutes, predicted_substitutes)
                total_recalled += get_num_recalled(
                    ground_truth_substitutes, predicted_substitutes)
                total_ground_truth += len(ground_truth_substitutes)
                total_predicted += len(predicted_substitutes)
    print(
        f"Precision: {total_correct / total_predicted}, Recall:{total_recalled / total_ground_truth}")


def get_missing_ingredients(pred_path, ground_truth_path):
    with open(f'data/{ground_truth_path}') as f:
        ground_truth = json.load(f)
        with open(f'predictions/{pred_path}') as f_pred:
            pred = json.load(f_pred)
            missing_substitutes = {}
            for ingredient in ground_truth:
                missing_substitutes[ingredient] = list(set(
                    ground_truth[ingredient]) - set(pred[ingredient]))
    with open(f'evaluations/missing_ingredients.json', 'w') as f_out:
        json.dump(missing_substitutes, f_out, ensure_ascii=False)
    print("Missing ingredients can now be found at evaluations/missing_ingredients.json")


def get_num_correct(true, pred):
    num_correct = 0
    for ingredient in pred:
        if ingredient in true:
            num_correct += 1
    return num_correct


def get_num_recalled(true, pred):
    num_recalled = 0
    for ingredient in true:
        if ingredient in pred:
            num_recalled += 1
    return num_recalled


parser = ArgumentParser()
parser.add_argument("-p", "--predicted", dest="pred_path",
                    required=True, help="path to the model's prediction file")
parser.add_argument("-g", "--ground_truth", dest="ground_truth_path",
                    required=True, help="path to the ground truth file")
parser.add_argument("-gm", "--get_missing", dest="get_missing_ingredients",
                    required=False, help="set to True to output the missing ingredients")
args = parser.parse_args()
evaluate(args.pred_path, args.ground_truth_path)
if args.get_missing_ingredients:
    get_missing_ingredients(args.pred_path, args.ground_truth_path)

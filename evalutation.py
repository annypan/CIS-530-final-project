import json


def evaluate(data_path):
    with open('data/ground_truth.json') as f:
        ground_truth = json.load(f)
        with open(f'data/{data_path}') as f_pred:
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
    return total_correct / total_predicted, total_recalled / total_ground_truth


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


if __name__ == "__main__":
    pass

from math import log
import operator



__all__ = [
    'shannon_entropy',
    'split_dataset',
    'choose_best_feature_to_split',
    'majority_count',
    'create_tree',
    'classify'
]



def shannon_entropy(dataset: list) -> float:
    ''' 
    Calculates Shannon information entropy.
    The higher the entropy, the more mixed up the data is.'''
    
    number_of_entries = len(dataset)
    lables_counts = {}

    for feature_vector in dataset:
        current_label = feature_vector[-1]
        if current_label not in lables_counts.keys():
            lables_counts[current_label] = 0
            lables_counts[current_label] += 1

    shannon_entropy_value = 0.0

    for key in lables_counts:
        probability = float(lables_counts[key]) / number_of_entries
        shannon_entropy_value -= probability * log(probability, 2)

    return shannon_entropy_value


def split_dataset(dataset: list, axis: int, value) -> list:
    new_dataset = []
    for feature_vector in dataset:
        if feature_vector[axis] == value:
            reduced_feature_vector = feature_vector[:axis]
            reduced_feature_vector.extend(feature_vector[axis+1:])
            new_dataset.append(reduced_feature_vector)
    return new_dataset


def choose_best_feature_to_split(dataset: list) -> int:
    number_of_features = len(dataset[0]) - 1
    base_entropy = shannon_entropy(dataset)
    best_info_gain = 0.0
    best_feature = -1

    for i in range(number_of_features):
        feature_list = [example[i] for example in dataset]
        unique_values = set(feature_list)
        new_entropy = 0.0

        for value in unique_values:
            subdataset = split_dataset(dataset, i, value)
            probability = len(subdataset) / float(len(dataset))
            new_entropy += probability * shannon_entropy(subdataset)

        info_gain = base_entropy - new_entropy

        if (info_gain > best_info_gain):
            best_info_gain = info_gain
            best_feature = i

    return best_feature

def majority_count(class_list: list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
            class_count[vote] += 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

def create_tree(dataset: list, labels: list) -> dict:
    class_list = [example[-1] for example in dataset]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(dataset[0]) == 1:
        return majority_count(class_list)

    best_feature = choose_best_feature_to_split(dataset)
    best_feature_label = labels[best_feature]

    tree = { best_feature_label : {} }
    del(labels[best_feature])

    feature_values = [example[best_feature] for example in dataset] 
    unique_values = set(feature_values)
    for value in unique_values:
        sublabels = labels[:]
        tree[best_feature_label][value] = create_tree(split_dataset(dataset, best_feature, value), sublabels)
    
    return tree


def classify(input_tree: dict, feature_labels: list, test_vector: list) -> dict:
    first_key = list(input_tree.keys())[0]
    second_tree = input_tree[first_key]
    feature_index = feature_labels.index(first_key)
    class_label = None
    for key in second_tree.keys():
        if test_vector[feature_index] == key:
            if isinstance(second_tree[key], dict):
                class_label = classify(second_tree[key], feature_labels, test_vector)
            else:
                class_label = second_tree[key]

    return class_label


def json_save_tree(name: str, tree: dict):
    import json
    with open('{}.json'.format(name), 'w') as fp:
        fp.write(json.dumps(tree))

def json_load_tree(name: str) -> dict:
    import json
    with open('{}.json'.format(name), 'r') as fp:
        return json.loads(fp.read())
    return {}

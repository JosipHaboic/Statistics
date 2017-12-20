from trees import (
    shannon_entropy, 
    split_dataset, 
    choose_best_feature_to_split, 
    create_tree, 
    classify, 
    json_save_tree, 
    json_load_tree
)


DATA = [
    [1, 1, 1, 3, 'yes'],
    [1, 2, 1, 3, 'yes'],
    [1, 0, 1, 3, 'maybe'],
    [0, 1, 1, 3, 'maybe'],
    [0, 2, 1, 3, 'maybe'],
    [0, 0, 0, 0, 'no'],
    [0, 0, 1, 0, 'no'],
    [0, 0, 2, 0, 'no'],
    [0, 0, 3, 0, 'no'],
    [3, 3, 3, 3, 'error'],
    [3, 3, 2, 3, 'error'],
    [3, 2, 3, 3, 'error'],
]

LABELS = ['no surfacing', 'flippers', 'poissoinous', 'x']

SHANON_ENTROPY = shannon_entropy(DATA)
SPLITED_DATASET = split_dataset(DATA, 0, 1)
BEST_FEATURE = choose_best_feature_to_split(DATA)
TREE = create_tree(DATA, LABELS[:])

CLASSIFICATIONS = [
    classify(TREE, LABELS, [1, 0, 0, 1]),
    classify(TREE, LABELS, [1, 1, 0, 2]),
    classify(TREE, LABELS, [0, 1, 0, 3]),
    classify(TREE, LABELS, [0, 0, 0, 2]),
    classify(TREE, LABELS, [1, 2, 1, 1]),
    classify(TREE, LABELS, [0, 1, 0, 3])
]

import pprint
pprint.pprint((SHANON_ENTROPY, SPLITED_DATASET, BEST_FEATURE, TREE, CLASSIFICATIONS))

from json import load, dumps
from collections import defaultdict
import os

def load_to_default_dict(data):
    """Helper function to load the typo_data as a defaultdict of sets."""
    typo_dict = defaultdict(set)
    typo_dict.update({word: set(incorrect_words) for word, incorrect_words in data.items()})
    return typo_dict


def open_typo_file(path):
    """Open a file with typos and return the data as a defaultdict of sets."""
    with open(path, "r") as f:
        return load(f, object_hook=load_to_default_dict)


def save_typo_data(path, data):
    """Save the data as a dictionary with the values being lists instead of sets."""
    with open(path, "w") as f:
        f.write(
            dumps({word: list(incorrect_words) for word, incorrect_words in data.items()},
                  indent=4,
                  sort_keys=True))

def save_stats_file(path, data):
    """Save statistics about typos."""
    with open(path, "w") as f:
        f.write(
            dumps({wrong_word: counter for wrong_word, counter in data.items()},
                  indent=4,
                  sort_keys=True))

def open_stats_file(path):
    """Open a file with statistics on wrong words and return the data as a defaultdict of sets."""
    if os.path.exists(path):
        with open(path, "r") as f:
            return load(f)
    else:
        return {}

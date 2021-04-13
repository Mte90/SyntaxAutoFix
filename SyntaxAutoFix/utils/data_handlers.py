from json import load, dumps
from collections import OrderedDict
import os

def open_typo_file(path):
    """Open a file with typos and return the data as a defaultdict of sets."""
    with open(path, "r") as f:
        return load(f, object_hook=OrderedDict)


def save_typo_data(path, data):
    """Save the data as a dictionary with the values being lists instead of sets."""
    data = dict(sorted(data.items()))
    with open(path, "w") as f:
        f.write(dumps(data, indent=4))


def save_stats_file(path, word, amount):
    """Save statistics about typos."""
    stats = open_stats_file(path)
    if word in stats:
        stats[word] += amount
    else:
        stats[word] = amount

    with open(path, "w") as f:
        f.write(dumps(stats, indent=4, sort_keys=True))


def open_stats_file(path):
    """Open a file with statistics on wrong words and return the data as a defaultdict of sets."""
    if os.path.exists(path):
        with open(path, "r") as f:
            return load(f)
    else:
        return {}

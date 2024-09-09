"""
Module to generate array with random numbers
"""

import subprocess


def random_array(arr):
    """Function to generate array"""
    shuffled_num = None

    for index, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[index] = int(shuffled_num.stdout)
    return arr

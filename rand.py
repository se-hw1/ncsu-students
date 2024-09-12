"""
This module contains utilities for generating random arrays.
"""

import subprocess

def random_array(arr):
    """
    Fills the input array with random integers between 1 and 20.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The input list filled with random integers.
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"],
            capture_output=True,
            check=True  # Ensure subprocess exits with success
        )
        arr[i] = int(shuffled_num.stdout)
    return arr


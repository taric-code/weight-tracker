"""Get all data from files.

Pull data from file and give the needed data to program.

Note:
    This function only read and return needed data.
"""

import csv
from pathlib import Path


def met(file: Path) -> dict[str, float]:
    """Get MET value from file.

    Read the csv and return the data need.

    Args:
        file (Parh): Url of file as Path object.

    Returns:
        dict: Activity and there MET value.
    """
    with file.open("r", newline="", encoding="utf-8") as csvfile:
        file_data = csv.DictReader(csvfile) #Openthe csv file and read it

        filtered_data = {d["Activity Description"] : d["MET Value"] for d in file_data} #get only Activity and MET values

        return filtered_data



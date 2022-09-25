import json
import os
from datetime import datetime


class JsonData(object):
    def __init__(self):
        pass

    # Static Methods
    # --------------
    @staticmethod
    def save_json_data(data_dict):
        """
        Saves JSON data file from registered data_dict.
        :param data_dict: Registered date.
        :return: None
        """
        JsonData.check_candidates_json_folder()

        json_data = json.dumps(data_dict)
        file = open("candidates_json/{}".format(JsonData.get_filename()), "w")
        file.write(json_data)
        file.close()

    @staticmethod
    def json_data_exists():
        """
        Checks if JSON data exists inside the folder
        :return: bool
        """
        if len(JsonData.get_json_data_files()) > 0:
            return True
        return False

    @staticmethod
    def get_json_data_files():
        """
        Get JSON files located on the listed folder.
        :return: list
        """
        JsonData.check_candidates_json_folder()
        return os.listdir('candidates_json/')

    @staticmethod
    def check_candidates_json_folder():
        """
        Checks if candidates_json folder was created on the root of the project and creates one if not
        :return: None
        """
        if not os.path.isdir("candidates_json"):
            os.mkdir("candidates_json")

    @staticmethod
    def get_filename():
        """
        Gets filename for generated files
        :return: None
        """
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        return "{}_{}.{}".format("candidates", now, "json")

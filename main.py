import json

from core.little_glue import LittleGlue


def main(*args, **kwargs):
    data = kwargs.get("data")
    little_glue = LittleGlue(**data)
    little_glue.generate()

    # TODO: Integrate with Google Fire and develop a interactive menu to generate new little glues


if __name__ == '__main__':
    # Mocked data
    file = open("candidates_json/my_candidates.json", "r")
    data = json.loads(file.read())
    main(data=data)

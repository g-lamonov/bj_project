import json


class WorkWithJson:

    @staticmethod
    def open_file():
        with open('gameHistory.json', 'r') as f:
            data = json.loads(f.read())
            return data

    @staticmethod
    def write_file(data):
        with open('gameHistory.json', 'w') as f:
            json.dump(data, f, indent=2, separators=None)
            f.write('\n')

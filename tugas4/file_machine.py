import json
import logging
import base64
from file import Dire

p = Dire()


class FileMachine:
    def process(self, string_to_process):
        s = string_to_process
        cstrings = s.split(' ')
        try:
            command = cstrings[0].strip()
            if command == 'upload':
                logging.warn('upload')
                name = cstrings[1].strip()
                file = cstrings[2].strip()
                p.upload_data(name, file.encode())
                return 'OK'
            elif command == 'list':
                result = p.list_data()
                dictionary = {'status': 'success', 'data': result}
                return json.dumps(dictionary)
            elif command == 'download':
                name = cstrings[1].strip()
                result = p.download_data(name)
                return result[0]
            else:
                return 'ERROR COMMAND'
        except:
            return 'ERROR'


if __name__ == '__main__':
    pm = FileMachine()
    # input = 'input.txt'
    result = pm.process('list')
    print(result)

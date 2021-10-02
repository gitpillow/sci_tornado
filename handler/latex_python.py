import re
from tornado.web import RequestHandler
import re
import json

class LatexMatrix(RequestHandler):
    def post(self):
        matrix = []
        raw = str(self.request.body)
        print(raw)
        lines = raw.split('\\n')
        for line in lines:
            find = re.match('([-\\d]+\\s*\\&?\\s*)+', line)
            if (find):
                numbers = find.group()
                numbers = numbers.replace('&', '')
                print(line)
                print(numbers)
                numbers_arr = [int(i) for i in re.split('\\s+', numbers.strip())]
                matrix.append(numbers_arr)
        self.write(json.dumps(matrix))
                

                

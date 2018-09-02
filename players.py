import json

def writeToJSONFile(Path, filename, data):
    filePathNameWExt = './' + path + '/' + filename + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)



path = './'
fileName = 'example1'

data = {}

data['test'] = 'test2'
data['hello'] = 'world'

writeToJSONFile(path, fileName, data)

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

player1_name = input('имя игрока 1 ')
player1_money = 500
player2_name = input("имя игрока 2")
player2_money = 600
player1 = {'name' : player1_name, 'money' : player1_money}
player2 = {'name' : player2_name, 'money' : player2_money}

db = {}
db['player1'] = player1
db['player2'] = player2

if '__name__' != '__main__':
    for key in db:
        print(key, '=>\n', db[key])

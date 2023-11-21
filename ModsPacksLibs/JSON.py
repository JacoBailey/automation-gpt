import json

class JSON:
    def __init__(self, json_file_loc):
        try:
            unpwJsonFile = open(json_file_loc, 'r')
        except FileNotFoundError:
            print('Please ensure that the username/password containing \'UN_PW.json\' exists and is located in the \'User_Supplied_Data\' folder.')
        self.__jsonFileContents = unpwJsonFile.read()

    def json_Unpw_Parser(self):
        try:
            UnPwDict = json.loads(self.__jsonFileContents)
        except ValueError:
            return print('Invalid UN/PW file. Please fix JSON UN/PW file and ensure JSON data is formatted correctly.')
        username, password = UnPwDict['username'], UnPwDict['password']
        if username == '' or password == '':
            return Exception('Empty username or password in \'UN_PW.json\' file.')
        else:
            return username, password
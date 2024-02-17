import json

class InvalidUnpwJson(Exception):
    pass

class jsonHandler:
    def __init__(self, json_file_loc, *args):
        #Below if statement allows for optional non-file JSON data loading via string argument
        if json_file_loc == None:
            self.jsonFileContents = args[0]
        else:
            try:
                unpwJsonFile = open(json_file_loc, 'r')
            except FileNotFoundError:
                print('Please ensure that the username/password containing \'UN_PW.json\' exists and is located in the \'User_Supplied_Data\' folder.')
                raise FileNotFoundError
            self.jsonFileContents = unpwJsonFile.read()

    #TODO: UPDATE to return list for better test experience
    def json_Unpw_Parser(self): #TODO: Create regex to catch non-emails in username slot
        try:
            UnPwDict = json.loads(self.jsonFileContents)
        except ValueError:
            print('Invalid UN/PW file. Please fix JSON UN/PW file and ensure JSON data is formatted correctly.')
            raise ValueError
        username, password = UnPwDict['username'], UnPwDict['password']
        if username in [None,'','INSERT USERNAME HERE'] or password in [None,'','INSERT PASSWORD HERE']:
            print(f'username: {username}, password: {password}')
            raise InvalidUnpwJson('Invalid username or password in \'UN_PW.json\' file. Please fix username or password JSON data.')
        else:
            return username, password
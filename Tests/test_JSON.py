import pytest
from ..ModsPacksLibs import jsonHandler

class readJsonFile:
    #TODO: Valid file is read
    #TODO: Invalid file is excepted
    pass

class parseJsonData:
    def test_Json_Valid_Unpw_Data():
        JsonObject_Valid = jsonHandler('{"username":"personmcname@website.org","password":"123password"}')
        username, password = JsonObject_Valid.json_Unpw_Parser()
        assert username == 'personmcname@website.org' and password == '123password'
    
    def test_Json_Missing_Unpw_Data():
        JsonObject_MissingUnpw = jsonHandler('{"username":"","password":""}')
        with pytest.raises(InvalidUnpwJson):
            JsonObject_MissingUnpw.json_Unpw_Parser()

    def test_Json_Default_Unpw_Data():
        JsonObject_DefaultUnpw = jsonHandler('{"username":"INSERT USERNAME HERE","password":"INSERT PASSWORD HERE"}')
        with pytest.raises(InvalidUnpwJson):
            JsonObject_DefaultUnpw.json_Unpw_Parser()

    def test_Invalid_Json_Data_Format():
        JsonObject_InvalidJsonFormat = jsonHandler('{"username":"personmcname@website.org","password":"123password"')
        with pytest.raises(JSONDecodeError):
            JsonObject_InvalidJsonFormat.json_Unpw_Parser()
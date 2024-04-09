import pytest, os, re, sys, json
from pathlib import Path
#----------------------------------------------------------------------------
#----- Logic below ensures custom modules can be found by python/pytest -----
#----------------------------------------------------------------------------
testFilename = Path(__file__).name
testDirec_Str = re.sub(testFilename, '', str(__file__), count=1)
mainProgDirec_Str = re.sub(r'(/|\\)Tests(/|\\)', '', testDirec_Str, count=1)
sys.path.append(mainProgDirec_Str)
#----------------------------------------------------------------------------
import ModsPacksLibs

userSuppliedDataDirec_Obj = os.path.join(Path(mainProgDirec_Str), 'User_Supplied_Data')
unpwFilePath_Obj = os.path.join(userSuppliedDataDirec_Obj, 'UN_PW.json')
unpwInvalidFilePath_Obj = os.path.join(userSuppliedDataDirec_Obj, 'UN.json')



class Test_Read_Json_File:
    
    def test_Open_Valid_File(self):
        assert ModsPacksLibs.jsonHandler(unpwFilePath_Obj) != FileNotFoundError
    def test_Open_Invalid_File(self):
        with pytest.raises(FileNotFoundError):
            ModsPacksLibs.jsonHandler(unpwInvalidFilePath_Obj)
    def test_Manual_JSON_String_Loading(self):
        JsonObject_Valid = ModsPacksLibs.jsonHandler(None,'{"username":"personmcname@website.org","password":"123password"}')
        assert JsonObject_Valid.jsonFileContents == '{"username":"personmcname@website.org","password":"123password"}'


class Test_Json_Data_Parse:
    
    def test_Json_Valid_Unpw_Data(self):
        JsonObject_Valid = ModsPacksLibs.jsonHandler(None,'{"username":"personmcname@website.org","password":"123password"}')
        username, password = JsonObject_Valid.json_Unpw_Parser()
        assert username == 'personmcname@website.org' and password == '123password'
    
    #TODO: Combine the below tests into a parameterized version
        
    def test_Json_Missing_Unpw_Data(self):
        missingUnPwDataObject = ModsPacksLibs.jsonHandler(None,'{"username":"","password":""}')
        with pytest.raises(ModsPacksLibs.InvalidUnpwJson):
            missingUnPwDataObject.json_Unpw_Parser()

    def test_Json_Default_Unpw_Data(self):    
        defaultUnPwObject = ModsPacksLibs.jsonHandler(None,'{"username":"INSERT USERNAME HERE","password":"INSERT PASSWORD HERE"}')
        with pytest.raises(ModsPacksLibs.InvalidUnpwJson):
            defaultUnPwObject.json_Unpw_Parser()

    def test_Invalid_Json_Data_Format(self):
        invalidJsonDataObject = ModsPacksLibs.jsonHandler(None,'{"username":"personmcname@website.org","password":"123password"')
        with pytest.raises(ValueError):
            invalidJsonDataObject.json_Unpw_Parser()
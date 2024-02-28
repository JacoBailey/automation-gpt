import pytest, os, re, sys
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

root = ''
directories = ''
files = ''
validTestsProgDirectory = Path(re.sub(r'(/|\\)test_Filewalk.py','',str(__file__), count=1))
invalidTestsProgDirectory = os.path.join(Path(re.sub(r'(/|\\)Tests(/|\\)test_Filewalk.py','',str(__file__), count=1)), 'Test')
for root, dirs, files in os.walk(validTestsProgDirectory):
    root = root
    directories = dirs
    files = files



class Test_filewalk:

    def test_Valid_Directory_Filewalk(self):
        assert files == ModsPacksLibs.filewalk(validTestsProgDirectory)
    def test_Invalid_Directory_Filewalk(self):
            with pytest.raises(ModsPacksLibs.invalidDirectory):
                ModsPacksLibs.filewalk(invalidTestsProgDirectory)   
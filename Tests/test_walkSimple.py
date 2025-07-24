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

rootVar = ''
dirsVar = ''
filesVar = ''
validTestsProgDirectory = Path(re.sub(r'(/|\\)test_Walk_Simple.py','',str(__file__), count=1))
invalidTestsProgDirectory = os.path.join(Path(re.sub(r'(/|\\)Tests(/|\\)test_Walk_Simple.py','',str(__file__), count=1)), 'Test')
for root, dirs, files in os.walk(validTestsProgDirectory):
    rootVar = root
    dirsVar = dirs
    filesVar = files
    break

class Test_walkSimple:

    def test_Valid_Directory_Filewalk(self):
        walkSimpInst = ModsPacksLibs.walk_simple(validTestsProgDirectory)
        assert walkSimpInst.root == rootVar and walkSimpInst.dirs == dirsVar and walkSimpInst.files == filesVar

    def test_Invalid_Directory_Filewalk(self):
        with pytest.raises(ModsPacksLibs.invalidDirectory):
            walkSimpInst = ModsPacksLibs.walk_simple(invalidTestsProgDirectory)
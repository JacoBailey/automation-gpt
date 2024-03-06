import pytest, re, sys
from pathlib import Path
from unittest.mock import patch
#----------------------------------------------------------------------------
#----- Logic below ensures custom modules can be found by python/pytest -----
#----------------------------------------------------------------------------
testFilename = Path(__file__).name
testDirec_Str = re.sub(testFilename, '', str(__file__), count=1)
mainProgDirec_Str = re.sub(r'(/|\\)Tests(/|\\)', '', testDirec_Str, count=1)
sys.path.append(mainProgDirec_Str)
#----------------------------------------------------------------------------
import ModsPacksLibs

#TODO: Mock input
#TODO: Parameterize inputYesNo
#TODO: Cleanup formatting
#TODO: Create NoInput test

@patch('ModsPacksLibs.inputCorrectValidation.pyip.inputYesNo')
@patch('ModsPacksLibs.inputCorrectValidation.input')
class Test_Input_Correct_Validation:   

    @pytest.mark.parametrize('inputYesNoValue', ['yes', 'y', 'YES', 'Y', 'Yes' 'yEs', 'yeS', 'YEs', 'yES', 'YeS'])
    def test_YesInput(self, mock_input, mock_inputYesNo, inputYesNoValue):
        mock_input.return_value = 'test'
        mock_inputYesNo.return_value = inputYesNoValue
        assert ModsPacksLibs.inputCorrectValidation('test', 'testInput') == 'test'

    @pytest.mark.parametrize('inputYesNoValue', ['no', 'n', 'NO', 'N', 'No' 'nO'])
    def test_NoInput(self, mock_input, mock_inputYesNo, inputYesNoValue):
        mock_input.return_value = 'test'
        mock_inputYesNo.return_value = inputYesNoValue
        assert ModsPacksLibs.inputCorrectValidation('test', 'testInput') == 'test'
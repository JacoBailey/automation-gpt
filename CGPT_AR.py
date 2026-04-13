#CHAT GPT AUTO RESPONSE
#!python3

import ModsPacksLibs #Custom Modules
import pyperclip, re, os
import pyinputplus as pyip
from pathlib import Path
from seleniumbase import SB

input_pattern = re.compile(r'''(
                        (INSERT{1})
                        ((\s{1}[A-Z0-9]+)+)
                        )''', re.VERBOSE)
class NoTextFilesError(Exception):
    """Raised when no textfiles are found in a directory."""
    pass

class TemplateHasNoInputsError(Exception):
    """Raised when no input slots are found in template file."""
    pass
class Selectors:
    textarea_input = 'textarea[name*="prompt"]'
    submit_button = '#composer-submit-button'
    copy_button = 'button[aria-label="Copy response"]'

# Ensures program is run in the program file (primarily for IDE use)
os.chdir(Path(__file__).resolve().parent)

# Main program start + print program name
print('- - - - - - - - - - -\n- ChatGPT Automation -\n- - - - - - - - - - -')

# Locate all user-supplied prompt template file and add their files to a list
# - If there are no prompt files, it returns an exception
template_dir = Path(__file__).resolve().parent / 'Templates'
walk_obj = ModsPacksLibs.walkSimple.walk_simple(template_dir)
files = walk_obj.files
template_list = []
for file in files:
    if Path(file).suffix == '.txt':
        template_list.append(file)
if not template_list:
    raise NoTextFilesError('No textfile templates found in the \'Templates\' folder. Please add a textfile prompt to the \'Templates\' directory.')

# Ask the user to select a prompt to use from the prompt list, then read and save the prompt's contents
# - If there is only one prompt, it selects that prompt
if len(template_list) > 1:
    template_name = pyip.inputMenu(template_list, numbered = True)
else:
    template_name = template_list[0]
template = Path(template_dir) / template_name

# template fill logic loop
prompt = Path(template).read_text(encoding='utf8')
match = re.search(input_pattern, prompt)
if match is None:
    raise TemplateHasNoInputsError('No input slots found in user-selected template.')
while match is not None:
    slot = match.group().removeprefix('INSERT ')
    replacement = ModsPacksLibs.inputCorrectValidation(f'Please enter an input for: {slot}.', slot)
    prompt = re.sub(input_pattern, replacement, prompt, count=1)
    match = re.search(input_pattern, prompt)

#Automation to submit prompt to ChatGPT and return response
print('Starting automation.')
try:
    with SB(uc=True) as browser:
        # open site + browser
        browser.open('https://chatgpt.com/', timeout=15)
        
        # enter text into textarea box
        browser.wait_for_element_visible(Selectors.textarea_input, timeout=15)
        browser.type(Selectors.textarea_input, prompt, timeout=15)
        
        # click submit button
        browser.wait_for_element_clickable(Selectors.submit_button, timeout=15)
        browser.hover_and_click(Selectors.submit_button, Selectors.submit_button, timeout=15) # click submit button

        # click button to copy response
        browser.wait_for_element_clickable(Selectors.copy_button, timeout=120)
        browser.hover_and_click(Selectors.copy_button, Selectors.copy_button, timeout=30)
    
    print(f'Response copied to clipboard.\n------------------------------\n{pyperclip.paste()}')

except Exception as error:
    pyperclip.copy(prompt)
    print (f'Automation crashed.\nError: {error}\nManual fallback initiated.')
    print (f'----------\n{prompt}\n----------')
    print ('Prompt has been printed above and copied to clipboard for manual submission to ChatGPT.')
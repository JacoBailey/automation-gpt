#CHAT GPT AUTO RESPONSE
#!python3

import ModsPacksLibs #Custom Modules
import pyperclip, re, os, time
import pyinputplus as pyip
import seleniumbase
from pathlib import Path
from seleniumbase import SB
from dotenv import load_dotenv

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
    if Path(file).suffix != '.txt':
        continue
    else:
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

# Copy completed prompt to clipboard and print
# - This copy functions as a backup incase automation fails
pyperclip.copy(prompt)
print('Prompt copied to clipboard.')
time.sleep(1)
print('Starting automation.')

#Automation to submit prompt to ChatGPT and return response
with SB(uc=True) as browser:
    browser.open('https://chatgpt.com/', timeout=30)
    
    #Enter prompt and submit
    browser.wait_for_element_visible('#prompt-textarea > p', timeout=30)
    browser.set_text('#prompt-textarea > p', prompt, timeout=20)
    browser.wait_for_element_clickable('#composer-submit-button', timeout=20)
    browser.click('#composer-submit-button', timeout=20)

    #Copy response
    # - Solution uses a bit of a workaround. The original solution was simply to click the copy response button, but it seems that there is some security implementation preventing me from doing this so easily. As a workaround, I am copying the content by pulling in the response content directly, rather than relying on ChatGPT's conveniently supplied copy button.
    
    #TODO: May want to change back to button-based copy (we will see how versatile this workaround ends up being)
    # - Selector for button: 'div.flex.min-h-\[46px\].justify-start > div > button[aria-label="Copy"]'

    browser.wait_for_element_clickable(r'div.flex.min-h-\[46px\].justify-start > div > button[aria-label="Copy"]', timeout=30)
    response = browser.get_text(r'div[class="markdown prose dark:prose-invert w-full break-words dark markdown-new-styling"]')
    pyperclip.copy(response)

print(f'\nResponse copied to clipboard\n------------------------------\n{response}\n')
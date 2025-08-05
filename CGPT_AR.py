#CHAT GPT AUTO RESPONSE
#!python3

#TODO: Create tests for multi_selector_search
#TODO: Update program to handle user login + specific chat selection
#TODO: Download all necessary packages upon program download/initiation
#TODO: Ensure specific module/lib versions are chosen in requirements for added stability (update to current, then set specific version)
#TODO: Add docstrings to all classes, functions, etc.
#TODO: Fix formatting/escaping issue with CSS selector strings via raw strings (causing error print statements during program initial launch)

import ModsPacksLibs #Custom Modules
import pyperclip, re, os, time
import pyinputplus as pyip
import seleniumbase
from pathlib import Path
from seleniumbase import SB
from dotenv import load_dotenv

inputRegex = re.compile(r'''(
                        (INSERT{1})
                        ((\s{1}[A-Z0-9]+)+)
                        )''', re.VERBOSE)

#Ensures program is run in the program file (primarily for IDE use)
os.chdir(Path(__file__).resolve().parent)

#Temporarily commented out unpw handling until I have created proper handling for it
'''
#Locate progFileDirectory for user-supplied CGPT UN/PW and add UN/PW to program as individual variables
unpwJsonFilepath = Path(__file__).resolve().parents[1] / "CGPT.env"
load_dotenv(dotenv_path=unpwJsonFilepath)
username, password = os.getenv("USERNAME"), os.getenv("PASSWORD")
'''

#Dynamically locate and read all user-supplied prompt template files and add their names to a list (list will be used with a menu to ask user to pick a template)
#TODO: Convert all logic below to module?
templateFolderLocation = Path(__file__).resolve().parent / 'User_Supplied_Data' / 'Templates'
print(templateFolderLocation)
templateNamesList = []
walkObj = ModsPacksLibs.walkSimple.walk_simple(templateFolderLocation)
fileNames = walkObj.files
for fileName in fileNames:
        if Path(fileName).suffix != '.txt':
                continue
        else:
            templateNamesList.append(fileName)
if templateNamesList == []:
    raise Exception('No textfile templates found in the \'Templates\' folder. Please add a textfile prompt to the \'Templates\' directory before re-running the program.')

#Ask the user to select a prompt to use from the prompt list, then read and save the prompt's contents
#If there is only one prompt, it selects the prompt
#If there are no prompts, it returns an exception
if len(templateNamesList) > 1:
    selectedTemplateName = pyip.inputMenu(templateNamesList, numbered = True)
else:
    selectedTemplateName = templateNamesList[0]
selectedTemplate = os.path.join(templateFolderLocation, selectedTemplateName)

#Locate prompt input locations, have the user supply inputs, & fill in the prompt with the user-supplied inputs
prompt = Path(selectedTemplate).read_text(encoding='utf8')
templateInputSlots = inputRegex.findall(prompt) #TODO: Ensure a non-matched regex is handled
userInputsDict = {}
if templateInputSlots == ['']:
    print(f'No inputs found in \'{selectedTemplateName}\' file.{time.sleep(2)}\nProgram will continue without inputs.{time.sleep(2)}\nIf you would like to add inputs, please do so according to the program documentation/README.{time.sleep(2)}')
else:
    for inputSlot in range(len(templateInputSlots)):
        fullInputSlot = templateInputSlots[inputSlot][0]
        inputSlotName = templateInputSlots[inputSlot][2]
        while True:
            userInput = ModsPacksLibs.inputCorrectValidation(f'Please enter an input for: {inputSlotName}', inputSlotName)
            break
        userInputsDict[inputSlotName] = userInput
        prompt = prompt.replace(fullInputSlot, userInput)

#Automation to submit prompt to ChatGPT and return response
#TODO: Minimize/hide browser
with SB(uc=True) as browser:
    browser.open('https://chatgpt.com/', timeout = 30)
    
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

print(f'\nResponse copied to clipboard\n------------------------------\n{response}\n')
#CHAT GPT AUTO RESPONSE
#!python3

#TODO: Create a better solution for users to run program
#TODO Download all necessary packages upon program download/initiation

import ModsPacksLibs #Custom Modules
import pyperclip, re, os, time
import pyinputplus as pyip
from pathlib import Path
from seleniumbase import SB
import seleniumbase

def multiSelectorSearch(browserObject, list, timeout=0.5):
    for selector in list:
        try: 
            browserObject.wait_for_element_visible(selector,timeout = timeout)
            return selector
        except seleniumbase.common.exceptions.NoSuchElementException:
            continue

inputRegex = re.compile(r'''(
                        (INSERT{1})
                        ((\s{1}[A-Z0-9]+)+)
                        )''', re.VERBOSE)



#Dynamically locate filefolder for user-supplied CGPT UN/PW and add UN/PW to program as individual variables
#TODO: Create tests for exception handling to ensure proper functioning.
#TODO: Convert to module?
fileFolder = re.sub(r'(/|\\)CGPT_AR.py', '', str(__file__), count=1)
unpwJsonFileLoc = os.path.join(fileFolder, 'User_Supplied_Data', 'UN_PW.json')
unpwJsonFileContents = ModsPacksLibs.jsonHandler(unpwJsonFileLoc)
userUsername, userPassword = unpwJsonFileContents.json_Unpw_Parser()

#Dynamically locate and read all user-supplied prompt template files and add their names to a list (list will be used with a menu to ask user to pick a template)
#TODO: Create tests for exception handling to ensure proper functioning.
#TODO: Convert to module?
templateFolderLocation = os.path.join(fileFolder, 'User_Supplied_Data', 'Templates')
templateNamesList = []
fileNames = ModsPacksLibs.filewalk(templateFolderLocation)
for fileName in fileNames:
        if Path(fileName).suffix != '.txt':
                continue
        else:
            templateNamesList.append(fileName)
if templateNamesList == []:
    raise Exception('No textfile templates found in the \'Templates\' folder. Please add a textfile prompt to the \'Templates\' directory before re-running the program.')

#Ask the user to select a prompt to use from the prompt list, then read and save the prompt's contents
#If there is only one prompt, then it auto selects the prompt
#If there are no prompts, it returns an exception
if len(templateNamesList) > 1:
    selectedTemplateName = pyip.inputMenu(templateNamesList, numbered = True)
    selectedTemplate = os.path.join(templateFolderLocation, selectedTemplateName)
else:
    selectedTemplate = os.path.join(templateFolderLocation, templateNamesList[0])

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

#Open Browser and log in to CGPT, skip past pop-ups, enter prompt, and return result to terminal + copy to user's clipboard

#TODO: Handle invalid username and password
#TODO: Minimize/hide browser OR requests w/ undetected...?

with SB(uc=True) as browser:
    browser.open('https://chat.openai.com/auth/login')
    browser.wait_for_element_visible('button:nth-child(1)').click()
    activeUsernameSelector = multiSelectorSearch(browser, ['#email-input', '#username'])
    browser.wait_for_element_visible(activeUsernameSelector).send_keys(userUsername)
    activeContinueUsernameButtonSelector = multiSelectorSearch(browser, ['body > div > main > section > div > div > div > div.c74298dc3.c0ee5daba > div > form > div.c90212864 > button',  'continue-btn', '#root > div > main > section > div.login-container > button'])
    browser.wait_for_element_visible(activeContinueUsernameButtonSelector).click()
    browser.wait_for_element_visible('#password').send_keys(userPassword)
    activePasswordContinueButtonSelector = multiSelectorSearch(browser, ['#radix-\:rh\: > div > button', 'body > div.oai-wrapper > main > section > div > div > div > form > div.c90212864 > button', '#submit'])
    browser.wait_for_element_visible(activePasswordContinueButtonSelector).click()
    browser.wait_for_element_visible('#prompt-textarea').send_keys(prompt)
    activePromptSubmitButton = multiSelectorSearch(browser, ['#__next > div.relative.z-0.flex.h-full.w-full.overflow-hidden > div > main > div.flex.h-full.flex-col > div.w-full.pt-2.md\:pt-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:w-\[calc\(100\%-\.5rem\)\] > form > div > div.flex.w-full.items-center > div > button', 'div.group.w-full.text-token-text-primary.border-b.border-black\/10.dark\:border-gray-900\/50.bg-gray-50.dark\:bg-\[\#444654\] > div > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.justify-between.lg\:block > div.text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible > button', '#__next > div.relative.z-0.flex.h-full.w-full.overflow-hidden > div > main > div.flex.h-full.flex-col > div.w-full.pt-2.md\:pt-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:w-\[calc\(100\%-\.5rem\)\] > form > div > div.flex.w-full.items-center > div > button'])
    browser.wait_for_element_visible(activePromptSubmitButton).click()
    browser.wait_for_element_clickable('#__next > div.relative.z-0.flex.h-full.w-full.overflow-hidden > div > main > div.flex.h-full.flex-col > div.flex-1.overflow-hidden > div > div > div > div:nth-child(3) > div > div > div.relative.flex.w-full.flex-col.agent-turn > div.flex-col.gap-1.md\:gap-3 > div.mt-1.flex.justify-start.gap-3.empty\:hidden > div > span:nth-child(1) > button', timeout=120).click()

print('\nResponse copied to clipboard\n------------------------------')
print(pyperclip.paste(), '\n')
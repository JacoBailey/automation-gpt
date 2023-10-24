#CHAT GPT AUTO RESPONSE
#!python3

#TODO: Remove the below
#Currently using this fix for "chromedriver not compatible w/ chrome version 116" issue > https://github.com/ultrafunkamsterdam/undetected-chromedriver/pull/1478

#TODO: Create a better solution for users to run program

#TODO Download all necessary packages upon program download/initiation
from xml.sax.xmlreader import Locator
import ModsPacksLibs
import pyperclip, ssl, re, os, json, time
import undetected_chromedriver as uc
import pyinputplus as pyip
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Program Setup (Establish SSL/TLS, custom exceptions, regex patterns)
ssl._create_default_https_context = ssl._create_stdlib_context
inputRegex = re.compile(r'''(
                        (INSERT{1})
                        ((\s{1}[A-Z]+)+)
                        )''', re.VERBOSE)
class JSONDecodeError(Exception):
    'Please ensure that the JSON data is formatted correctly based on the program\'s documentation/README.'
    pass
class MissingPromptTemplateError(Exception):
    'Please ensure that there is at least one prompt template textfile within the \'User_Suppied_Data/Templates\' program directory.'
    pass


#Dynamically locate filefolder for user-supplied CGPT UN/PW and add UN/PW to program as individual variables
#TODO: Create tests for exception handling to ensure proper functioning.
fileFolder = re.sub(r'(/|\\)CGPT_AR.py', '', str(__file__), count=1)
unpwJsonFileLoc = os.path.join(fileFolder, 'User_Supplied_Data', 'UN_PW.json')
try:
    unpwJsonFile = open(unpwJsonFileLoc, 'r')
except FileNotFoundError:
    print('Please ensure that the username/password containing \'UN_PW.json\' exists and is located in the \'User_Supplied_Data\' folder.')
unpwJsonFileContents = unpwJsonFile.read()
try: #TODO: Test this to ensure correct funcionality
    UnPwDict = json.loads(unpwJsonFileContents)
except JSONDecodeError:
    print('Please fix JSON UN/PW file.')
userUsername, userPassword = UnPwDict['username'], UnPwDict['password']
if userUsername == '' or userPassword == '':
    raise Exception('Empty username or password in \'UN_PW.json\' file.')


#Dynamically locate and read all user-supplied prompt template files and add their names to a list (list will be used with a menu to ask user to pick a template)
#TODO: Create tests for exception handling to ensure proper functioning.
templateFolderLocation = os.path.join(fileFolder, 'User_Supplied_Data', 'Templates')
templateNamesList = []
for foldername, subfolders, filenames in os.walk(templateFolderLocation):
    for filename in filenames:
        if Path(filename).suffix != '.txt':
            if templateNamesList == [] and filename == filenames[-1]:
                raise Exception('No textfile templates found in the \'Templates\' folder. Please add a textfile before running the program.')
            else:
                continue
        else:
            templateNamesList.append(filename)


#Ask the user to select a prompt to use from the prompt list, then read and save the prompt's contents
#If there is only one prompt, then it auto selects the prompt
#If there are no prompts, it returns an exception
if len(templateNamesList) > 1:
    selectedTemplateName = pyip.inputMenu(templateNamesList, numbered = True)
    selectedTemplate = os.path.join(templateFolderLocation, selectedTemplateName)
elif len(templateNamesList) == 1:
    selectedTemplate = os.path.join(templateFolderLocation, templateNamesList[0])
else:
    raise MissingPromptTemplateError

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
            print(f'Please enter an input for: {inputSlotName}')
            userInput = input()
            if userInput == '':
                print(f'You have entered no input for: {inputSlotName}\nIs this correct?')
                yesOrNo = pyip.inputYesNo()
                if yesOrNo == 'yes':
                    break
                else:
                    continue
            break
        userInputsDict[inputSlotName] = userInput
        prompt = prompt.replace(fullInputSlot, userInput)


#Open Browser and log in to CGPT, skip past pop-ups, enter prompt, and return result to terminal + copy to user's clipboard
browser = uc.Chrome()
browser.get('https://chat.openai.com')

#TODO: Handle invalid username and password
#TODO: Minimize/hide browser OR requests w/ undetected...?

elementFinder = ModsPacksLibs.Automation(browser, 20, By.CSS_SELECTOR)
loginbutton = elementFinder.findElement('button:nth-child(1)')
loginbutton.click()
emailInput = elementFinder.findElement('#username')
emailInput.send_keys(Keys.ENTER)
pwInput = elementFinder.findElement('#password')
pwInput.send_keys(Keys.ENTER)
continueButton = elementFinder.findElement('body > div.oai-wrapper > main > section > div > div > div > form > div.c6d5cc3be > button')
continueButton.send_keys(Keys.ENTER)
popUP_OkayLetsGoButton = elementFinder.findElement('div.flex.flex-row.justify-end > button')
popUP_OkayLetsGoButton.click()
cgptChatbox = elementFinder.findElement('#prompt-textarea')
cgptChatbox.send_keys(prompt)
cgptChatbox_SendButton = elementFinder.findElement('div.flex.w-full.items-center > div > button')
cgptChatbox_SendButton.click()
clipboardButton = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.group.w-full.text-token-text-primary.border-b.border-black\/10.dark\:border-gray-900\/50.bg-gray-50.dark\:bg-\[\#444654\] > div > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.justify-between.lg\:block > div.text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible > button')))
clipboardButton.click()

browser.close()
print('\nResponse copied to clipboard\n------------------------------')
print(pyperclip.paste(), '\n')
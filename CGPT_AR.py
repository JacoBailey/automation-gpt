'''
CHAT GPT AUTO RESPONSE
---------------------
The purpose of this program is to return a response from chatgpt via, without the need to write a entire prompt or open the webpage. 
The program uses a pre-written prompt (and later - a template with CLAs / user inputs to create a prompt), logs in and submits it to ChatGPT, then
returns the result to the user.

Future plans
- CLA/Input support (if there is one or more missing required argument, the program requests it from the user via an input)
- Multi-template CLA suport
- New template support module
- Response update
- Login session maintenance

V1.0 Functionality
- Uses user prompt, Logs in and provides repsonse from ChatGPT
'''

#!python3

import argparse, selenium, time, pyperclip, ssl, re
import undetected_chromedriver as uc
import pyinputplus as pyip
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
ssl._create_default_https_context = ssl._create_stdlib_context

#TODO LATER: Turn this into a package (For selenium/undetected_chrome) - include functionality for slenium/undetected_chrome methods
#AutoBrowse.browser(browserObject from selenium/undetected_chrome) - used to import browser
#AutoBrowse.browseSelector(selector, click/sendkeys/etc.)
#AutoBrowse.browseXpath(...,...)
#etc...

def elementChecker(currentBrowser, element):
    while True:
        try:
            currentBrowser.find_element(By.CSS_SELECTOR, element)
        except selenium.common.exceptions.NoSuchElementException:
            time.sleep(1)
            continue
        break

inputRegex = re.compile(r'INSERT{1}((\s{1}[A-Z]+)+)')
templatesDict = {'content':
                 {'location':'...'},
                 'meta':
                 {'location':'...'},}
userInputsDict = {}

#TODO: Figure out how to make CLAs work with shell script
'''parser = argparse.ArgumentParser()
parser.add_argument("-temp", "--template", required=True, action='store', help="For selecting the prompt template.")
args = parser.parse_args()'''

print('Please select a template.')
template = pyip.inputMenu(list(templatesDict), numbered=True)
prompt = Path(templatesDict[template]['location']).read_text()
inputs = inputRegex.findall(prompt)

'''------------------------------------------------------'''

#Get user inputs
for inputSlot in range(len(inputs)):
    print(f'Please enter an input for: {inputs[inputSlot][0]}')
    userInput = input()
    userInputsDict[inputs[inputSlot][0]] = userInput

#Replace "INSERT HERES" with user inputs
for inputSlot in userInputsDict:
    prompt = prompt.replace('INSERT' + inputSlot, userInputsDict[inputSlot])

# Open Browser and Login
browser = uc.Chrome()
browser.get('https://chat.openai.com')
elementChecker(browser, '#__next > div.flex.h-full.w-full.flex-col.items-center.justify-center.bg-gray-50.dark\:bg-gray-800 > div.w-96.flex.flex-col.flex-auto.justify-center.items-center > div.flex.flex-row.gap-3 > button:nth-child(1)')
loginButton = browser.find_element(By.CSS_SELECTOR, '#__next > div.flex.h-full.w-full.flex-col.items-center.justify-center.bg-gray-50.dark\:bg-gray-800 > div.w-96.flex.flex-col.flex-auto.justify-center.items-center > div.flex.flex-row.gap-3 > button:nth-child(1)')
loginButton.click()
elementChecker(browser, '#username')
emailInput = browser.find_element(By.CSS_SELECTOR, '#username')
emailInput.send_keys('...')
emailInput.send_keys(Keys.ENTER)
elementChecker(browser, '#password')
pwInput = browser.find_element(By.CSS_SELECTOR, '#password')
pwInput.send_keys('...')
pwInput.send_keys(Keys.ENTER)

#Skip through popup
elementChecker(browser, '#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button')
cgptPopUp_Next1 = browser.find_element(By.CSS_SELECTOR, '#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button')
cgptPopUp_Next1.click()
elementChecker(browser, '#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-neutral.ml-auto')
cgptPopUp_Next2 = browser.find_element(By.CSS_SELECTOR, '#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-neutral.ml-auto')
cgptPopUp_Next2.click()
elementChecker(browser, '#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-primary.ml-auto')
cgptPopUp_Next3 = browser.find_element(By.CSS_SELECTOR, '#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-primary.ml-auto')
cgptPopUp_Next3.click()

#Enter Prompt
cgptChatbox = browser.find_element(By.CSS_SELECTOR, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea')
cgptChatbox.send_keys(prompt)
cgptChatbox_SendButton = browser.find_element(By.CSS_SELECTOR, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button')
cgptChatbox_SendButton.click()

#Copy Response
elementChecker(browser, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.flex-1.overflow-hidden > div > div > div > div.group.w-full.text-gray-800.dark\:text-gray-100.border-b.border-black\/10.dark\:border-gray-900\/50.bg-gray-50.dark\:bg-\[\#444654\] > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.justify-between.lg\:block > div.text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible > button.flex.ml-auto.gap-2.h-full.w-full.rounded-md.p-1.hover\:bg-gray-100.hover\:text-gray-700.dark\:text-gray-400.dark\:hover\:bg-gray-700.dark\:hover\:text-gray-200.disabled\:dark\:hover\:text-gray-400')
if template == 'meta':
    cgptChatbox = browser.find_element(By.CSS_SELECTOR, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea')
    cgptChatbox.send_keys('Rewrite it to be under 165 characters long.')
    cgptChatbox_SendButton = browser.find_element(By.CSS_SELECTOR, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button')
    cgptChatbox_SendButton.click()
    elementChecker(browser, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.flex-1.overflow-hidden > div > div > div > div:nth-child(4) > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.justify-between.lg\:block > div.text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible > button.flex.ml-auto.gap-2.h-full.w-full.rounded-md.p-1.hover\:bg-gray-100.hover\:text-gray-700.dark\:text-gray-400.dark\:hover\:bg-gray-700.dark\:hover\:text-gray-200.disabled\:dark\:hover\:text-gray-400')
    clipboardButton = browser.find_element(By.CSS_SELECTOR, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.flex-1.overflow-hidden > div > div > div > div:nth-child(4) > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.justify-between.lg\:block > div.text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible > button.flex.ml-auto.gap-2.h-full.w-full.rounded-md.p-1.hover\:bg-gray-100.hover\:text-gray-700.dark\:text-gray-400.dark\:hover\:bg-gray-700.dark\:hover\:text-gray-200.disabled\:dark\:hover\:text-gray-400')
    clipboardButton.click()
else:
    clipboardButton = browser.find_element(By.CSS_SELECTOR, '#__next > div.overflow-hidden.w-full.h-full.relative.flex > div > main > div.flex-1.overflow-hidden > div > div > div > div.group.w-full.text-gray-800.dark\:text-gray-100.border-b.border-black\/10.dark\:border-gray-900\/50.bg-gray-50.dark\:bg-\[\#444654\] > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.justify-between.lg\:block > div.text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible > button.flex.ml-auto.gap-2.h-full.w-full.rounded-md.p-1.hover\:bg-gray-100.hover\:text-gray-700.dark\:text-gray-400.dark\:hover\:bg-gray-700.dark\:hover\:text-gray-200.disabled\:dark\:hover\:text-gray-400')
    clipboardButton.click()
browser.close()

#Print Response
print('\nResponse copied to clipboard\nRESPONSE:\n------------------------------')
cgptResponse = pyperclip.paste()
print(cgptResponse, '\n')
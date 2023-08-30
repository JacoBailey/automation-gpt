Title

    ChatGPT Prompt Response Automation Tool

Project Description
    
    The purpose of this program is enable the user to optimize repetitive (but slightly different) ChatGPT workflows. It works by having the user select from a list of user-submitted text-prompt templates, then has the user submit input for the template, and automatically submits the prompt to ChatGPT and returns its response. This is a much more effecient process for repetitive ChatGPT work as it negates the need to manually fill in a prompt, visit the site and login, and retrieve the response from ChatGPT. It significantly cuts down on the required work steps and reduces the time by approximately 80-90% (prior to using this program, this would take around 10 minutes to do my personal ChatGPT workflows, now it usually takes around 1-2 minutes).

Technologies Used

    For the main logic of the program, I chose to use python. During my original creation of the program (outside of some basic CSS/HTML), it was the sole programming language which I knew and this was a personal project which I used to both optimize my work and solidify my knowledge of the language.

Challenges faced

    - ChatGPT's site changing selectors and dom structure (this made finding specific elements with selectors/xpath rather difficult)
    - Undetected_ChromeDriver package being incompatible with current chrome versions (using a temp fix)

Features

    Current Features
    - Easy template structure for users to create and use their own prompts
    - User-selectable input prompts for simplified workflows
    - Quick automation speed

    Planned Features
    - More straightforward and simplified download/setup/run process for users
    - Login session support (should significantly increase program speed due to removing the need to login during each run)
    - Conversation Mode Support (will enable users to provide more than one input to ChatGPT so entire ChatGPT conversation workflows can be automated, as opposed to singular inputs.)

Installation

    1. Download the files via GitHub: https://github.com/JacoBailey/automation-gpt
        - Click the green "code" button > "Download ZIP"
        - Save the ZIP somewhere on your device locally (icloud or similar cloud-based storage directories will not work)
    2. Unzip the file.
    3. Open Terminal/Powershell/etc. and run the following command(s) within the "...":

        " pip3 install pyperclip ssl re os json time pyinputplus pathlib selenium undetected_chromedriver "
        
        ALSO INSTALL THE COMMAND BELOW
        THIS IS A TEMP FIX WHICH WILL BE REMOVED WHEN THE BUG IS FIXED BY THE U.C. MODULE TEAM
       
        " pip3 install -e git+https://github.com/jdholtz/undetected-chromedriver.git@29551bd27954dacaf09864cf77935524db642c1b#egg=undetected_chromedriver "

Setup

    1. Open the program file (usually named 'automation-gpt-main').
    2. Open the "USER_SUPPLIED_DATA" folder.
    3. Open the 'UN_PW.json' file, replace the INSERT USERNAME HERE and INSERT PASSWORD HERE with your ChatGPT account username and password.
    4. Open the "Template" folder (this is where all of your prompt templates for ChatGPT will be kept).
    5. Using the example formatting which is showcased in the 'Example_Template.txt' file, create as many textfile prompt templates as you would like and save them in this folder.
        - Files MUST use formatting shown in the example file with each input slot starting with "INSERT" and the remaining text written in capitals, otherwise the program will not recgonize it.
        - After creating and saving your custom prompt templates, you are welcome to delete the 'Example_Template.txt' file so it will not be picked up and used by the program.

Run Instructions

    There are 2 options to run the program.

    A. Bash/Shell Script (recommended).
        - Google instructions on how to do this. There are many resources available online.
        - Use the filepath of the 'CGPT_AR.py' file for the Bash/Shell script.
    B. Terminal w/ Filepath.
        - Open the program file (should be named 'automation-gpt-main').
        - Copy the filepath for the 'CGPT_AR.py' file.
        - Open Terminal, Powershell, etc.
        - Enter 'python3 COPIED-FILEPATH-HERE' (Make sure to replace the COPIED-FILEPATH HERE with your filepath location which you just copied)
        - Click 'enter'

How To Contribute

    At this point in time, I will probably not be accepting contributions, but feel free to suggest changes.
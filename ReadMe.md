Title

    ChatGPT Automation Tool (for repeat workflows)

Project Description
    
    The purpose of this program is enable the user to optimize repetitive ChatGPT workflows. It works as follows:

    1. Create templates for each prompt you wish to submt to ChatGPT (with areas to input specific additional details for each new prompt submission).
    2. Select which prompt template to use from a list of your templates.
    3. Submit your inputs for the selected template.
    4. Watch as the tool automatically loads ChatGPT, submits the prompt, and copies the response to your clipboard.
    
    This is a much more effecient process for repetitive ChatGPT work as it negates the need to manually fill in a prompt, visit the site and login, and retrieve the response from ChatGPT, by conveniently packaging this operation into a single quick to use script. It significantly cuts down on the typical required steps and reduces the time by approximately 80-90%.

Technologies Used

    For the main logic of the program, I chose to use python. During my original creation of the program, it was the sole programming language which I knew and this was a personal project which I used to both as a means to optimize my work and to solidify my knowledge of the language.

Challenges faced

    - ChatGPT's site changing selectors and dom structure (this made finding specific elements with selectors/xpath rather difficult)
    - Undetected_ChromeDriver package being incompatible with current chrome versions (using a temp fix)
    - ChatCPT adding additional security preventing automated clicks to the copy button

Features

    Current Features
    - User-selectable input prompts for simplified workflows
    - Easy template syntax structure for users to create and use their own prompts
    - Quick automation speed

    Planned Features
    - Login + chat selection support
    - Conversation support (will enable users to provide additional prompt replies to ChatGPT after the initial, so conversation workflows can be automated, as opposed to solely singular inputs)

Installation
\*_This setup assumes you already have python installed on your machine - if you do not, please proceed with python install prior to performing the following setup_

    1. Download the files via GitHub: https://github.com/JacoBailey/automation-gpt
        - Click the green "code" button > "Download ZIP"
        - Save the ZIP somewhere on your device locally (icloud or similar cloud-based storage directories will not work)
    2. Unzip the file.
    3. Open Terminal/Powershell/etc.
    4. Navigate into program directory with "cd" command.
    5. Run the following command: 

        "pip install -r requirements.txt"

Setup

    1. Open the program file (will be named 'automation-gpt-main' unless you changed during download).
    2. Open the "Templates" folder (this is where all of your prompt templates for ChatGPT will be kept).
    3. Using the example formatting which is showcased in the example files, create as many textfile prompt templates as you would like and save them in this folder.
        - Files MUST use formatting shown in the example file with each input slot starting with "INSERT" and the remaining text written in capitals, otherwise the program will not recgonize it.
        - After creating and saving your custom prompt templates, you are welcome to delete the example template files so they will not be picked up and used by the program (**NOTE:** _you must always have atleast one valid template in this directory otherwise the program will not function correctly_)

Optional Setup

    * Move CGPT.env file outside of program directory > fill out with your username and password to enable login functionality

Run Instructions

    There are 2 options to run the program.

    1. Bash/Shell Script (recommended).
        - Google instructions on how to do this. There are many resources available online.
        - Use the filepath of the 'CGPT_AR.py' file for the Bash/Shell script.
    2. Terminal w/ Filepath.
        - Open the program file (should be named 'automation-gpt-main').
        - Copy the filepath for the 'CGPT_AR.py' file.
        - Open Terminal, Powershell, etc.
        - Enter 'python3 COPIED-FILEPATH-HERE' (Make sure to replace the COPIED-FILEPATH HERE with your filepath location which you just copied)
        - Click 'enter'

How To Contribute

    At this point in time, I will probably not be accepting contributions, but feel free to suggest changes, make note of bugs, etc..
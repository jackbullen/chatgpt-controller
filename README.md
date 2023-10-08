## Usage

**Step 1:** Start the chrome instance and navigate to [ChatGPT](https://chat.openai.com/)

#### Windows:

`"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_dev_session"`

#### Linux:

`google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_session"`

#### macOS:

`/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_session"`

**Step 2:** Open the GUI

`python3 gui.py`

**Step 3:** Enter the prompt, choose prompt builder, and click "Send"
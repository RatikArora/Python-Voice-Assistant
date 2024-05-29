# CHARLIE - Virtual Assistant

## Project Overview

CHARLIE is a virtual assistant designed to help users with various tasks, ranging from providing the current date and time to fetching information from the web. The assistant can respond to natural language queries and perform actions such as opening websites, launching applications, converting speech to text, and more.

## Features

### 1. Greetings
The assistant greets the user and asks how it can help.
```python
def greetings():
    speakandprinttext("Hello sir, how can I help you now?")
```

### 2. Date and Time
CHARLIE can provide the current date and time upon request.
```python
def tareek(n):
    din = date.today()
    if n == 1:
        din = din + timedelta(1)
        speakandprinttext(f"Tomorrow is: {din.strftime('%B %d, %Y')} sir!")
    else:
        speakandprinttext(f"Today's date is: {din.strftime('%B %d, %Y')} sir!")

def samay():
    waqt = datetime.now().time().strftime("%H:%M")
    speakandprinttext(f"It's {waqt}")
```

### 3. Open Websites
The assistant can open websites using the Chrome browser.
```python
def opensite(url):
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new_tab(url)
```

### 4. Voice Commands
CHARLIE uses voice commands to interact with the user. The following actions are supported:
- Introducing itself
- Responding to love declarations humorously
- Telling jokes
- Searching Google
- Fetching news
- Converting speech to text
- Opening and closing applications

### 5. Web Search and Information Retrieval
The assistant can perform web searches and retrieve information from Wikipedia.
```python
def googlesearch(query):
    # Implementation of Google search functionality

def wiki(query):
    # Implementation of Wikipedia search functionality
```

### 6. Application Control
CHARLIE can open and close applications on the user's system.
```python
def appopen(app_name):
    # Implementation to open applications

def appclose(app_name):
    # Implementation to close applications
```

### 7. Exiting the Application
The assistant can recognize when the user wants to end the session.
```python
def main1():
    while True:
        text = microphone()
        if "bye" in text or 'ok' in text or 'okay' in text or 'thank you' in text:
            return
```

## Usage

To run CHARLIE, simply execute the `main1` function. The assistant will start listening for commands and respond accordingly.

```python
if __name__ == "__main__":
    main1()
```

## Dependencies

- `microphone` from `speechtotext`: To capture audio input.
- `speakandprinttext` from `texttovoice`: To convert text responses to speech and print them.
- `webbrowser`: To open websites.
- `googlesearch` from `websearch`: To perform Google searches.
- `appopen` and `appclose` from `appopeneer`: To manage application execution.
- `wiki` from `wiki`: To fetch Wikipedia information.
- `news` from `news`: To fetch the latest news.
- `random`: To randomly select jokes.
- `stt` from `stt`: To convert speech to text.

## Installation

Ensure all dependencies are installed. You can install them using pip:

```bash
pip install speechtotext texttovoice websearch appopeneer wiki news stt
```

## Contribution

Feel free to contribute to the project by submitting issues or pull requests on GitHub. Your feedback is valuable for improving CHARLIE.

## License

This project is licensed under the MIT License.

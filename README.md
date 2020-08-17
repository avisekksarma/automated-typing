# Automated-typing

For running this project you need to download webdriver for Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
, find your chrome version and download the respective chromedriver.

**Now put the chromedriver in your PATH by extracting the file if needed to extract.**

---

**How to install and run it on your own machine**
- Clone the repository or download the zip file
- For zip file extract it, then cd into the directory 
- make virtualenv and install the packages into the environment by:
```
$ virtualenv venv
$ source venv/bin/activate (in Mac OS/linux) or $ venv\Scripts\activate (in windows)
$ pip install -r requirements.txt
```
- then run the singleperson.py by typing:
`$ python singleperson.py`
- then wait and watch as you cross over 100+ for the typing speed.

Now more fun part (i.e. match against other people in real time) 
- Run the multiplayer-keybr.py by typing:
`$ python multiplayer-keybr.py`
- then wait and watch as you win the race by mile and stun other paritcipants.

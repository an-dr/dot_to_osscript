"""
All package info is here. By defaults, opens URL with the repo
"""

info = {
    "name": "dot_to_osscript",
    "version": "0.3.1",
    "description": "Generate sh and ps1 scripts from .env files to apply for the process",
    "url": "https://github.com/an-dr/dot_to_osscript",
    "author": "Andrei Gramakov",
    "author_email": "mail@agramakov.me",
    "install_requires": [line.rstrip('\n') for line in open("requirements.txt")],  # reading requirements.txt content
    "license": "MIT",

}

if __name__ == '__main__':
    import webbrowser

    webbrowser.open(info["url"])

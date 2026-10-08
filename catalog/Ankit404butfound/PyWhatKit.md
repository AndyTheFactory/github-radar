---
repository: "Ankit404butfound/PyWhatKit"
github_id: 223073222
url: "https://github.com/Ankit404butfound/PyWhatKit"
description: "Send WhatsApp message at certain time and many other things."
starred_at: "2025-08-24T18:59:26Z"
language: "Python"
topics: ["hacktoberfest", "hacktoberfest-accepted", "hacktoberfest2021", "pywhatkit"]
homepage: ""
license: "MIT"
archived: false
---

# Ankit404butfound/PyWhatKit

Send WhatsApp message at certain time and many other things.

**GitHub:** https://github.com/Ankit404butfound/PyWhatKit

## README excerpt

> > I am a bit busy and not able to keep up with the issues, I am looking for active collaborators, please contact me if you are interested.
> > For commercial purposes please contact ankitrajmahapatra\gmail\com
> > [Buy me a coffee](https://buymeacoffee.com/ankitrajma)
> [PyWhatKit](https://pypi.org/project/pywhatkit/) is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it is one of the most popular library for WhatsApp and YouTube automation. New updates are released frequently with new features and bug fixes.
> # Links
> - **Join our discord server - https://discord.gg/2GBF5VSPDj
> - **Documentation - [Wiki](https://github.com/Ankit404butfound/PyWhatKit/wiki)**
> ## Installation and Supported Versions
> PyWhatKit is available on PyPi:
> python3 -m pip install pywhatkit
> pip3 install pywhatkit
> PyWhatKit officially supports Python 3.8+.
> ## Cloning the Repository
> git clone https://github.com/Ankit404butfound/PyWhatKit.git
> ## What's new in v5.4?
> Fix Flask import error
> ## What's new in v5.3?
> import pywhatkit
> pywhatkit.start_server()
> ### This method can be used to remotely control your PC using your phone (Windows only)
> - Make sure your PC and your phone are on same network, on your PC, Open Network and Internet Settings > Properties > Network Profile, make sure it's set to Private.
> - Run the above code and then open command prompt and type `ipconfig`.
> - Search for `IPv4 Address` and on your phone's browser type this address and append `:8000` at the end, example `192.168.0.1:8000`.
> - Try moving you finger and you should notice your cursor moving too.
> - You can also type and scroll too, enjoy.
> - More information here https://pywhatkit.herokuapp.com/remote-kit with the raw code.
> ## Features
> - Sending Message to a WhatsApp Group or Contact
> - Sending Image to a WhatsApp Group or Contact
> - Converting an Image to ASCII Art
> - Converting a String to Handwriting
> - Playing YouTube Videos
> - Sending Mails with HTML Code
> - Install and Use
> ## Usage
> import pywhatkit
> # Send a WhatsApp Message to a Contact at 1:30 PM
> pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)
> # Same as above but Closes the Tab in 2 Seconds after Sending the Message
> pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)
> # Send an Image to a Group with the Caption as Hello
> pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
> # Send an Image to a Contact with the no Caption
> pywhatkit.sendwhats_image("+91012345

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

PyWhatKit is a Python library for automating WhatsApp messaging, sending images, and playing YouTube videos at scheduled times. It also includes features such as converting images to ASCII art, converting strings to handwriting, and sending HTML emails.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "2635dfaa1d3f01780afd8c9b22a0633a9bc0711b5cd0f1448529a87240f73f0c"
  },
  "primary_domain": "applications",
  "secondary_domains": [
    "productivity",
    "developer-tools"
  ],
  "repository_type": "library",
  "capabilities": [
    "api-integration",
    "automation",
    "media-editing"
  ],
  "technologies": [
    "Python"
  ],
  "summary": "PyWhatKit is a Python library for automating WhatsApp messaging, sending images, and playing YouTube videos at scheduled times. It also includes features such as converting images to ASCII art, converting strings to handwriting, and sending HTML emails.",
  "use_cases": [
    "Scheduling WhatsApp messages to contacts or groups",
    "Automating YouTube video playback from Python scripts",
    "Converting images to ASCII art"
  ],
  "limitations": [
    "The maintainer reports limited capacity to address issues and is seeking collaborators",
    "Commercial use requires contacting the maintainer",
    "Remote control feature is documented as Windows-only"
  ],
  "suggested_terms": [
    "whatsapp automation python",
    "pywhatkit",
    "youtube automation python",
    "send whatsapp message schedule",
    "python ascii art"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->

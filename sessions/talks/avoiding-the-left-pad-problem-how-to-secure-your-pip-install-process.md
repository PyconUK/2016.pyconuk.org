title: 'Avoiding the "left-pad" problem: How to secure your pip install process'
subtitle:
speaker: aaron-bassett
video: https://www.youtube.com/watch?v=qt7TboNJGJg
slides: https://speakerdeck.com/aaronbassett/avoiding-the-left-pad-problem-how-to-secure-your-pip-install-process
---
When Azer Koçulu pulled 11 lines of code from npm he not only broke thousands of dependent packages but also prevented developers all over the world from deploying their code. This talk will show how you can harden your pip install process, ensure that packages have not been tampered with, protect against MITM attacks and even how to keep deploying if a package is deleted or if PyPI goes offline. 
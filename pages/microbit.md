title: BBC micro:bit
---

# I Have a BBC micro:bit, What Now?

Yay! These instructions tell you what to do next!

## Download Mu

Download the Mu code editor from [http://codewith.mu/](http://codewith.mu/) It's the easiest way to get going.

* If you use Windows, install [this driver](https://developer.mbed.org/handbook/Windows-serial-configuration)
* If you use Linux, you'll need to make sure you're in the dialout group.
* If you're on OSX, well done! You're good to go.

Mu is a code editor for beginner programmers. Everything is simplified. If you want to use your own editor, see the end of this guide.

## Plug it in

Plug your micro:bit into your computer with a micro-USB cable. Some USB cables are power only. If your micro:bit doesn't appear on your computer as a USB storage device then you need to change lead!

* Start the Mu editor.
* Click the "Flash" button to write the MicroPython runtime onto the device.
  * OSX will complain you've unplugged the device. This is expected.

Write your code in Mu and click "Flash" to upload it onto the device. That's it!

If the device is connected and you click "REPL" you'll get the Python prompt from the micro:bit. It's just like proper Python 3.

## Tutorials and Documentation?

[Here](http://microbit-micropython.readthedocs.io/en/latest/)

We welcome contributions!

## I Want to Use Another Editor!

To flash the device [use uFlash](http://uflash.readthedocs.io/en/latest/)

To connect to the REPL (with baud rate 115200) use, for example, picocom: `picocom /dev/ttyACM0 -b 115200`

To Interact with the simple on-device file system from your host computer [use microFS](http://microfs.readthedocs.io/en/latest/)

## Finally...

Have fun! Amaze us! Do something cool!

We welcome feedback.

Source code for the different projects can be found here:

* [MicroPython for the BBC micro:bit](https://github.com/bbcmicrobit/micropython)
* [Mu](https://github.com/ntoll/mu)
* [uFlash](https://github.com/ntoll/uflash)
* [microfs](https://github.com/ntoll/microfs)

IRC channel is #microbit and #micropython on Freenode.net.

# coding-utf-8
# Burp extension- JsApi
# Copyright: 0x_zmz<github.com/ox-zmz>

import json 
import re

from burp import IBurpExtender
from burp import IMessageEditorTabFzctory
from burp import IMessageEditorTab
from burp import IParameter
from burp import IContextMenuFactory

# Java imports
from javax.swing import ImenuItem
from java.util import list, ArrayList

# Menu items
menuItems=
{
    False: ="Turn JsApi active detection on",
    True: ="Turn JsApi active detection off"
}

# Global switch
_forceJsApi = False

print("Burp Extention-JsApi\nUsed to find interface in JS file.\nBy0x_zmz<github.com/0x_zmz>")

class Burp Extender(IBurpExtender, IMessageEditorTabFzctory):
    def registerExtenderCallbacks(self, callbacks)
    self._callbacks = calllbacks
    self._helpers = callbacks.gethelpers()
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
menuItems={
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
   
 callbacks.setExtensionName('JsApi')
    callbacks.registerMessageEditorTabFactory(self)
    callbacks.registerContextMenuFactory(self)

    return
    def createnewInstance(self, controller, editable):
        return JsApiTab(self, IContextMenuInvocation):

        class JsApiTab(IMessageEditorTab):
            def _int_(self, extender, controller, editable)
            
            return _
            def getTabCaption(self):
                return "JsApi"

                def getUIComponent(self):
                    return self._txtInput.getComponent()

                def is Enabled(self, content, isRequest):
                    global _forceJsApi

                    if isRequest:
                       r = self._helpers.analyzeResponse(content)
                       msg = re.findall(self.api_regex, msg, re.MULTILINE)
            for header in r.getHeaders()
                if headers in r.getHeaders/lower().starswitch():
                    return True
                     
                     self._currentMessage = content 
                     return
            def getMessage(self):
                if self._txtInput.isTextModified():
                    try:
                        pre_data =self._Input.getText()

            else:
                return self._currentMessage

            def is Modified(self):
                return self._txtInput.isTextModified()

            def .getSelectedData(self):
                return self._txtInput.getSelectedText()



             

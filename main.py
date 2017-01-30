#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from helpers import rotate_character, up_alpha, low_alpha
from caesar import encrypt

def build_page(txtarea_content):
    rot_label = "<label>Rotate by: </label>"
    rot_input = "<input type='number' name='rot'/>"

    message_label = "<label>Type a Message</label>"
    txt_area = "<textarea name='message'>" + txtarea_content + "</textarea>"

    submit = "<input type='submit' />"
    form = "<form method='post'>" + rot_label + rot_input + "<br>" + message_label + txt_area + "<br>" + submit + "</form>"

    header = "<h3>Web Caesar</h3>"
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rot"))
        the_caesar = encrypt(message, rotation)
        escape_caesar = cgi.es(the_caesar)
        content = build_page(escape_caesar)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

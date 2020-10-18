#!/usr/bin/env python3
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

import cgi, cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
user_inp = form.getvalue('fname')
print("Test input is: ",user_inp)

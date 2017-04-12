### A Script for sending mail in Python

This is a usefull script for sending email when there is no configured smtp server on the host. There are a few ways that you can use this file. First you need to fill in the following:
fromaddr
toaddr
server
server.login

With these initial settings the script will send email along with a line of text entered at the command line. For example, ./mail.py "This is a test"

The above configuration is simple and small enough for text message alerts.

If you uncomment the other three lines of code and fill in the From, To, and Subject then these are the fields that normally populate in a standard email.

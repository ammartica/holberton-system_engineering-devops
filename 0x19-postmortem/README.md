# Project 0x19-Postmortem

This is an incident report based on the Holberton School project [Web stack debugging #1](https://github.com/ammartica/holberton-system_engineering-devops/tree/master/0x0E-web_stack_debugging_1)

## Issue Summary:
We just installed Nginx as our web server but we are unable to connect to port 80. This is a potential problem for our customers because if they try to access our website using unencrypted hyper-text transfer protocol (HTTP), they will be unable to do so.

## Timeline:
 * When was the issue detected - 2022-04-25 00:00 (GMT-04:00)
 * How was the issue detected - During a routine test
 * Actions taken - Researched default installation files for enabled and available sites
 * Which team/individuals was the incident escalated to - Amisaday Martínez Campos
 * How the incident was resolved - changing the default file for enabled sites so it would listen to port 80 instead of port 8080

## Root cause and resolution
Since we were just beginning to start working with the server, we figured Nginx closed port 80 by default. We decided to look into the default files that come with Nginx.
This was indeed where the issue was. The default file for enabled sites was listening in on port 8080 instead of port 80. We decided to delete this file and create a symbolic link to the default file for available sites, which was listening in on port 80.
We then restarted the server to apply the changes and the issue was resolved.

## Corrective and preventative measures:
To avoid similar problems in the future, we should devise a protocol to always verify the default files after installing




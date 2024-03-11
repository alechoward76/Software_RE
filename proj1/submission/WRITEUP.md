# API Reversing

## Author
Alec Howard
## Time Taken
~ 2 Hours
## Overview
The purpose of this project was to show my ability to extract class files from a jar application, decompile them, and reverse engineer the functionality of the program, creating my own app that bypassed its limits. It allowed me to put a multitude of skills to work.
## Objectives
- Obtain the API Key (8DEC7CF5226BEA6A6E92CAC30A465384)
- Figure out the Required Routes ("/motd", "post_motd" & "/encrypt")
- Figure out how to bypass the time limit restraint (Create a proxy that excluded the limiting code)
- Create a proxy to access the server through

## Terminology
- Application Programming Interface (API): A way for two or more computer programs or components to communicate with each other. It is a type of software interface, offering a service to other pieces of software. 
- API Key: A unique identifier used to authenticate and authorize a user, developer, or calling program to an API.
- Proxy: A dedicated computer or a software system running on a computer that acts as an intermediary between an endpoint device, such as a computer, and another server from which a user or client is requesting a service.
## Key Technologies/Tools Used
- IntelliJ IDEA including Fernflower Decompiler
- 7zip file archiver
- Visual Studio Code
- Google Search Engine
## Challenges
My biggest challenge was interpreting the code and writing my own version of it in Python. When I was first looking at the class files, I had trouble focussing on the flow of the program, but once I slowed down and took it step-by-step, the challenge became alot more manageable. Additionally, an absurd chunk of the time it took me to complete this project was spent messing with my PATH variables so I could run the given jar app.
## Results/Findings
I found that the server that the application connected to used an API key to authenticate a user before sending them a message of the day and allowing them to send in a message and a key to be encrypted and returned. After this was done, some timeout was imposed on the user before they were able to submit another message. By analyzing the code, I was able to build a proxy that excluded the functionality of the timeout and allows for a user to send as many messages as they want back-to-back. Additionally I realized that there was a method hidden and never called that allowed me to post a message of the day to the server.
## Conclusion
This project tested both my reverse engineering skills, as well as my scripting skills. It was a fun exercise that left me with a sense of satisfaction.
## Code Snippets
*This code snippet prevented an error for Insecure Requests from printing out (see references)*
```urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)```

## References
https://networklessons.com/python/python-connect-with-api

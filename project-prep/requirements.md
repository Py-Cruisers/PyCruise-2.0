# Requirements

## Vision
- What is the vision of this product?
    - Providing streamlined convenience for launching applications and software environments.
- What pain point does this project solve?
    - Average user not knowing how to use a terminal to access the PyCrusie CLI
    - Also saves time when sifting through applications to launch for work, development, and entertainment software environments.
- Why should we care about your product?
    - Time is money! Our product saves users time and streamlines the development workflow. 



## Scope
- In | What will your product do?
    - Open multiple applications or files with single action or mouseclick.
    - Provide users the option to create their own sets of applications to open as custom environments
    - The script will be able to open a web browser to a specific url/website
    - The product will be housed in the MacOS menu bar

- Out | What will your product NOT do?
    - Stretch:
        - close applications 
    - upload personal custom environment settings to any resource online
    - Stretch:
        - package as downloadable software

## Functional Requirements
- User can manually add applications to open
- user can create a new mode with different applications
- user can open individual applications
- application exists as a standalone application
    - appears in applications bar and in menu bar

### Data Flow
- Our application's primary functions operate on and within the local file system to find and run various applications.

## NFR's
- Usability
    - Project will be a MacOS application
    - "" Will be simple and easy to use

- Error Handling
    - Our project will handle errors such as 
        - application not found/existing
        - produce useful error message to the user
# Automated Testing for OrangeHRM
Assessment: [AT Project 2](https://docs.google.com/document/d/11aHRJiFGg5lp7LSf2dTQ2VAPh0gFagivnDtTEBVzqzI/edit?usp=sharing)

This repository contains automated test cases for OrangeHRM application using selenium, Python and pytest. 
The tests are organized into two categories: admin-related tests and login-related tests. 

## Directory Structure

```plaintext
│  main.py
│  README.md
│
├───pageObjects
│  │  adminPage.py
│  │  loginPage.py
│  │  __init__.py
│
└───testCases
    │  test_admin.py
    │  test_login.py
    │  __init__.py
```

## Environment
    python==3.10.1

## Requirements
- pytest
- selenium


```commandline
pip install pytest==7.4.0
```

```commandline
 pip install selenium==4.11.2
```

## Running the Tests

To run all tests, navigate to the root and run
    
    python main.py


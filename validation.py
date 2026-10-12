import re

def name_validator(name):
    if not isinstance(name,str) or not re.match("^[a-zA-Z\s]{3,20}$",name):
        raise ValueError("Invalid Name")
    return name

def family_validator(family):
    if not isinstance(family,str) or not re.match("^[a-zA-Z\s]{3,50}$",family):
        raise ValueError("Invalid Family")
    return family

def code_validator(code):
    if not isinstance(code,int):
        raise ValueError("Invalid Code")
    return code

def age_validator(age):
    if not isinstance(age,int) or age>150:
        raise ValueError("Invalid Age")
    return age

def gender_validator(gender):
    if not isinstance(gender,str) or gender not in ["male","female"]:
        raise ValueError("Invalid Gender")
    return gender

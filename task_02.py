#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""function that can return a 'yes' or 'no' value equivalent of
truthy or falsy values."""

def bool_to_str(bval):
    if(bval):
        string = "Yes"
    else:
        string = "No"
    return string

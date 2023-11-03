import numpy as np 
import pandas as pd 

def extract_speaker(file_name):
    # Code to extract the file name
    label = file_name
    # Process it to get superfulous info out
    if "e" in label:
        label = label.split("e")[0].upper().strip()
        
    if "E" in label:
        label = label.split("E")[0].upper().strip()
        
    if "_" in label:
        label = label.split("_")[0].upper().strip()
        
    if "%" in label:
        label = label.split("%")[0].upper().strip()

    if "." in label:
        label = label.split(".")[0].upper().strip()

    return label
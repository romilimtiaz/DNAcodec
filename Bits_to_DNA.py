# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:51:35 2024

@author: Acer
"""
import cv2
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
def bits_to_dna_optimized(bits):
    # Create a mapping dictionary
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}

    # Use list comprehension for efficient string construction
    dna_list = [mapping[bits[i:i+2]] for i in tqdm(range(0, len(bits), 2))]

    # Join the list into a single string
    dna = ''.join(dna_list)

    # Write to file
    with open("dna_sequence.txt", "w") as file:
        file.write(dna)
    return dna
# Read the image
def process_chunk(chunk):
    return ''.join(np.unpackbits(chunk).astype(str))

def to_bitstream_parallel(image, num_threads=4):
    # Split the image into chunks
    chunks = np.array_split(image.flatten(), num_threads)
    
    # Process each chunk in parallel
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        bitstreams = executor.map(process_chunk, chunks)
    
    # Combine the results
    return ''.join(bitstreams)
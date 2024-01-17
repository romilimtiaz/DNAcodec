# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:52:14 2024

@author: Acer
"""
from tqdm import tqdm
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
def dna_to_bits(file_path):
    # Define the mapping from DNA characters to binary pairs
    mapping = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}

    # Read the DNA sequence from the file
    with open(file_path, "r") as file:
        dna_sequence = file.read()

    # Convert the DNA sequence to a binary string using list comprehension
    binary_list = [mapping[dna] for dna in tqdm(dna_sequence)]

    # Join the list into a single binary string
    binary_data = ''.join(binary_list)

    return binary_data


def bitstream_to_image(bitstream, image_shape, num_threads=4):
    # Calculate the length of each chunk
    chunk_size = len(bitstream) // (num_threads * 8)

    # Split the bitstream into chunks
    chunks = [bitstream[i:i + chunk_size * 8] for i in range(0, len(bitstream), chunk_size * 8)]

    def process_chunk_to_bytes(chunk):
        return bytes(int(chunk[i:i+8], 2) for i in range(0, len(chunk), 8))

    # Process each chunk in parallel to convert back to bytes
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        byte_chunks = executor.map(process_chunk_to_bytes, chunks)

    # Combine the byte chunks and create a numpy array
    byte_array = b''.join(byte_chunks)
    image_array = np.frombuffer(byte_array, dtype=np.uint8).reshape(image_shape)

    return image_array

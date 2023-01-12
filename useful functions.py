"""
I am using this to store useful functions for env sci and cheminformatics. JClokey
"""

# Tanimoto or Jaccard indexing is a bitwise method for comparing similarities of two binary strings
# This is useful for comparing chemical fingerprints such as the Pubchem substructure fingerprint 
# takes two binary strings
def tanimoto(fp1, fp2):
    
    # converts binary strings to binary integers (int base 2) 
    fp1 = int(fp1, 2)
    fp2 = int(fp2, 2)

    # Counts the 1s in each int and the number of pairs
    fp1_bits = bin(fp1).count('1')
    fp2_bits = bin(fp2).count('1')
    common_bits = bin(fp1 & fp2).count('1')

    # Computes and returns the tanimoto similarity from 0-1 as a float (1 being 100% similar, 0 being 0% similar) 
    return float(common_bits) / (fp1_bits + fp2_bits - common_bits)


# random binary generator
# this will create random binaries of any specified length as a string
# requires the random module to be imported

import random

def rand_binary_gen(bits):
    binary = ''
    for i in range(bits):
        binary += str(random.randint(0,1))
    return binary

"""
to create a dictionary of random binaries attached to a random chemical, with leading zeroes:
binaries = {}
for i in range(1000):
    binaries["Imaginary_chemical_{0}".format(str(i).zfill(6))] = rand_binary_gen(1024)
"""
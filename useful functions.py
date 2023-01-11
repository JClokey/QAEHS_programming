"""
I am using this to store useful functions I have made for env sci and cheminformatics
"""

# Tanimoto or Jaccard indexing is a bitwise method for comparing similarities of two binary strings
# This is useful for comparing chemical fingerprints such as the Pubchem substructure fingerprint 
# takes two binary strings
def tanimoto(fp1, fp2):
    
    # converts binary strings to binary integers (int base 2) 
    fp1 = int(fp1, 2)
    fp2 = int(fp2, 2)

    # Counts the 1s in each int and the number of pairs
    fp1_count = bin(fp1).count('1')
    fp2_count = bin(fp2).count('1')
    both_count = bin(fp1 & fp2).count('1')

    # Computes and returns the tanimoto similarity from 0-1 as a float (1 being 100% similar, 0 being 0% similar) 
    return float(both_count) / (fp1_count + fp2_count - both_count)

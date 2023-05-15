# This script is designed to read in two csv files and reformat the data for FORTRAN data structures.
# The two files (aij.4May23.csv and bij.4May23.csv) contain important benchmarking constant
# values to be used with an implicit solvent for biomolecular simulation
import pandas as pd

# Read in both base CSV files
aij = pd.read_csv("files\\aij.4May23.csv", header=None)
bij = pd.read_csv("files\\bij.4May23.csv", header=None)

# File writers for new files
aij_writer = open('aij.for_tinker.log', 'w')
bij_writer = open('bij.for_tinker.log', 'w')

# Go through all rows and split them into groups for printing
for i in range(0, 45):
    k = 0
    # Aij (3 values per line)
    a_values = aij.iloc[i]
    # Bij (7 values per line)
    b_values = bij.iloc[i]

    aij_writer.write(
        '      data aij(' + str(i+1) + ",:)/ " + '{:.10f}'.format(a_values[k]) + "d0, " + '{:.10f}'.format(a_values[k + 1]) +
        "d0, " + '{:.10f}'.format(a_values[k + 2]) + "d0, \n")
    bij_writer.write(
        '      data bij(' + str(i+1) + ",:)/ " + '{:.2f}'.format(b_values[k]) + "d0, " + '{:.2f}'.format(b_values[k + 1]) +
        "d0, " + '{:.2f}'.format(b_values[k + 2]) + "d0, " + '{:.2f}'.format(b_values[k + 3]) + "d0, " +
        '{:.2f}'.format(b_values[k + 4]) + "d0, \n")
    # Go through Aij
    k = 3
    while k < 40:
        aij_writer.write(
            '     &                ' + '{:.10f}'.format(a_values[k]) + "d0, " + '{:.10f}'.format(a_values[k + 1]) + "d0, " +
            '{:.10f}'.format(a_values[k + 2]) + "d0, \n")
        k = k + 3
    aij_writer.write(
        '     &                ' + '{:.10f}'.format(a_values[42]) + "d0, " + '{:.10f}'.format(a_values[43]) + "d0, " +
        '{:.10f}'.format(a_values[44]) + "d0 / " + "\n")

    # Go through Bij
    k = 5
    while k < 40:
        bij_writer.write(
            '     &                ' + '{:.2f}'.format(b_values[k]) + "d0, " + '{:.2f}'.format(b_values[k + 1]) + "d0, " +
            '{:.2f}'.format(b_values[k + 2]) + "d0, " + '{:.2f}'.format(b_values[k + 3]) + "d0, " +
            '{:.2f}'.format(b_values[k + 4]) + "d0, \n")
        k = k + 5
    bij_writer.write(
        '     &                ' + '{:.2f}'.format(b_values[40]) + "d0, " + '{:.2f}'.format(b_values[41]) + "d0, " +
        '{:.2f}'.format(b_values[42]) + "d0, " + '{:.2f}'.format(b_values[43]) + "d0, " +
        '{:.2f}'.format(b_values[44]) + "d0 / " + "\n")

aij_writer.close()
bij_writer.close()

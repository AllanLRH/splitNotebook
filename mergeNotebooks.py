#!/usr/bin/env python

from splitNotebook import loadNotebook, writeNotebook
import argparse


def mergeNotebooks(nbi, nbo):
    """
    Merged the notebook with the input data (nbi) and notebook with output data (nbo).
    """
    for cc, co in zip(nbi['cells'], nbo['cells']):
        if 'execution_count' in co:
            cc['execution_count'] = co['execution_count']
        if 'outputs' in co:
            cc['outputs'] = co['outputs']
    return nbi  # updated with merged data


def getCommonSubstring(a, b):
    """
    Starting from index 0, return the common substring for a and b.
    """
    ret = list()
    for i, j in zip(a, b):
        if i == j:
            ret.append(i)
        else:
            return ''.join(ret)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("MergeNotebook")
    parser.add_argument('inputNotebook', help="Notebook with input data.")
    parser.add_argument('outputNotebook', help="Notebook with output data.")
    parser.add_argument('-o', '--outputname', help="Filename of merged notebook.",
                        type=str, default=None)
    p = parser.parse_args()

    nbi = loadNotebook(p.inputNotebook)
    nbo = loadNotebook(p.outputNotebook)
    nbm = mergeNotebooks(nbi, nbo)
    if p.outputname is None:
        outputname = getCommonSubstring(p.inputNotebook, p.outputNotebook)
        outputname = outputname + '_merged.ipynb' if len(outputname) else 'mergedNotebook.ipynb'
    else:
        outputname = p.outputname
    writeNotebook(nbm, outputname)

#!/usr/bin/env python

import json
from copy import deepcopy
import argparse
import sys
import traceback


def loadNotebook(filename):
    """
    Load notebook as json structure.
    """
    with open(filename) as fid:
        nb = json.load(fid)
        return nb


def splitNotebook(jsonbook):
    """
    Split notebook (json structure) into two structures,
    one with the inputs and one with the outputs.
    """
    nbi = deepcopy(jsonbook)  # Notebook with inputs
    nbo = deepcopy(jsonbook)  # Notebook with outputs
    for cl in nbi['cells']:
        if 'outputs' in cl.keys():
            cl['outputs'] = []
        if 'execution_count' in cl.keys():
            cl['execution_count'] = None

    for cl in nbo['cells']:
        if 'source' in cl.keys():
            cl['source'] = ''
    return (nbi, nbo)


def makeNewNames(filename):
    """
    Append '_input' and '_output' to the end of the filename,
    but before the file-extension.
    """
    a, b = filename.split('.')
    nbin = a + '_input.' + b
    nbon = a + '_output.' + b
    return (nbin, nbon)


def writeNotebook(jsonbook, filename):
    with open(filename, 'w') as fid:
        json.dump(jsonbook, fid)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser("SplitNotebook")
        parser.add_argument('filename', help="Name of the notebook to be split")
        parser.add_argument('-i', '--nooutputnotebook', help="Don't make notebook containing output",
                            action='store_true', default=False)
        parser.add_argument('-o', '--outputnames',
                            help="Name(s) of output notebooks, provide names for both "
                            "notebooks unless the --nooutputnotebook flag is given.",
                            type=str, nargs='+')
        p = parser.parse_args()
        nb = loadNotebook(p.filename)
        nbi, nbo = splitNotebook(nb)
        if not p.outputnames:
            inpName, outName = makeNewNames(p.filename)
        else:
            if p.nooutputnotebook:
                inpName = p.outputnames[0]
            else:
                inpName, outName = p.outputnames
        writeNotebook(nbi, inpName)
        if not p.nooutputnotebook:
            writeNotebook(nbo, outName)
    except Exception as e:
        print("An exception occured in splitNotebook.py",
              "If you think it's a bug in the script, please open an issue on github:",
              "https://github.com/AllanLRH/splitNotebook/issues",
              "But please check your input arguments to the script before doing s0 :)",
              "And please post the following in the bug report, preferebly along with your notebook:",
              "\n"*3, "Short traceback:\n", traceback.format_exc(), "\n"*3, "Long traceback:\n",
              "\n".join(traceback.format_stack()), file=sys.stderr, sep="\n")
        sys.exit(1)

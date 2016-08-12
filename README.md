Split Jupyter notebooks into an inputs-notebook and an outputs-notebook, which is useful when placing a notebook under version control.

Currently a work in progress, but `splitNotebook.py` is the most mature of the two python programs.

Sample command line help string:

```
(py35)❯ ./splitNotebook.py --help
usage: SplitNotebook [-h] [-i] [-o OUTPUTNAMES [OUTPUTNAMES ...]] filename

positional arguments:
  filename              Name of the notebook to be split

optional arguments:
  -h, --help            show this help message and exit
  -i, --nooutputnotebook
                        Don't make notebook containing output
  -o OUTPUTNAMES [OUTPUTNAMES ...], --outputnames OUTPUTNAMES [OUTPUTNAMES ...]
                        Name(s) of output notebooks, provide names for
                        bothnotebooks unless the --nooutputnotebook flag is
                        given.

```

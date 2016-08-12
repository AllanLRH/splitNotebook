Split Jupyter notebooks into an inputs-notebook and an outputs-notebook, which is useful when placing a notebook under version control.

This is work in progress, and is missing al but the most basic error handling through the with statement.

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


```
(py35)❯ ./mergeNotebooks.py --help
usage: MergeNotebook [-h] [-o OUTPUTNAME] inputNotebook outputNotebook

positional arguments:
  inputNotebook         Notebook with input data.
  outputNotebook        Notebook with output data.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUTNAME, --outputname OUTPUTNAME
                        Filename of merged notebook.
```

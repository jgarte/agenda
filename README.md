
### Interactive agenda in the console

This script reads an [org agenda](https://orgmode.org/) file (i.e. a
regular org file with some active dates, see [agenda.org](./agenda.org)) and displays an interactive
and colored year calendar.

### Usage

`./agenda agenda.org --holidays France`


### Dependencies

```
pip install org-parse  # See https://github.com/karlicoss/orgparse
pip install holidays   # See https://github.com/dr-prodigy/python-holidays
```

### Example output

![](agenda.png)

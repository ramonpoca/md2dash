# md2dash

A python script to convert a Markdown file into a Dash Cheatsheet

## Dependencies

This script uses mistune to parse markdown

```bash
pip install mistune

```

## Usage

Just invoke it with the markdown file:

```bash
./md2dash README.md
```

then you can add the docset to dash by double clicking or using `open`.
Note that the docset name will be based on the name of the Markdown file.


```bash
open README.docset
```

## License

Licensed under the GNU General Public License v3.0

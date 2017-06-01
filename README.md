# md2dash

A python script to convert a Markdown file into a Dash Cheatsheet.

## Dependencies

This script uses mistune to parse markdown:

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

You can get the full usage with `-h`.


### Docset title

If not set with `-t/--title` the title will use the markdown file basename.

```bash
./md2dash -t "Crazy Potato" README.md
```

### Customizing headers

By default only headers 1 and 2 are added to the index. You can add additional or different types for different headers:

```bash
./md2dash -l 3 Section -l 4 Header README.md
```

## License

Licensed under the GNU General Public License v3.0.

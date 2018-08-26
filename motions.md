# Vim Text Objects: The Definitive Guide

## Cut and pastes

- `["x]y`: yank (to register x)
- `["x]p`: paste after
- `["x]P`: paste before
- Ctrl-R[x]: paste register x in insert mode

### Registers

1. The unnamed register `""`
2. 10 numbered registers `"0` to `"9`
3. The small delete register `"-`
4. 26 named registers `"a` to `"z` or `"A` to `"Z`
5. three read-only registers `":`, `".`, `"%`
6. alternate buffer register `"#`
7. the expression register `"=`
8. The selection and drop registers `"*`, `"+` and `"~` 
9. The black hole register `"_`
10. Last search pattern register `"/`

### Visuals

- v[motion]y - visual motion yank
- v[motion]p - visual motion paste 

## Structure of an Editing Command

    <number><command><text object or motion>

### Commands

- `c`: change.
- `d`: delete.
- `y`: yank.
- `>, <`: indent, dedent.
- `=`: reformat (reindent, break long lines, etc.).
- `cc,dd,yy,>>,<<,==`: Do on whole line.


## Plaintext Text Objects

### Words

- `aw`: a word (includes surrounding white space).
- `iw`: inner word (does not include surrounding white space).

### Sentences

- `as`: a sentence.
- `is`: inner sentence.

### Paragraphs

- `ap`: a paragraph.
- `ip`: inner paragraph.

### Finding

- `t<char>`: to <char> forwards excluded.
- `T<char>`: to <char> backwards excluded.
- `f<char>`: to <char> included.
- `F<char>`: to <char> backwards included.
- `e`: end of current word.
- `2e`: end of next next word.
- `/<text>`: Find <text>.
- `n`: Repeat find.
- `N`: Repeat backwards.

### Moving

- `w`: next word.
- `h,l`: <- ->.
- `j,k`: up, down.
- `$`: End of line.
- `0`: Beginning of line.

- `H,M,L`: Top, midddle, bottom of window.
- `G`: End of file.
- `gg`: beginning of file.
- `<n>G`: <n>th line .

### Programming Language Text Objects

#### Strings


- `a"`: a double quoted string.
- `i"`: inner double quoted string.
- `a'`: a single quoted string.
- `i'`: inner single quoted string.
- `a``: a back quoted string.
- `i``: inner back quoted string.

#### Parentheses

- `a)`: a parenthesized block.
- `i)`: inner parenthesized block.
- `%)`: Matching parenthesis.

#### Brackets

- `a]`: a bracketed block.
- `i]`: inner bracketed block.

#### Braces

- `a}`: a brace block.
- `i}`: inner brace block.

#### Markup Language Tags

- `at`: a tag block.
- `it`: inner tag block.
- `a>`: a single tag.
- `i>`: inner single tag.

## Vim Scripts Providing Additional Text Objects

### CamelCaseMotion

- `i,w`: inner camel or snake-cased word.

### VimTextObj

- `aa`: an argument.
- `ia`: inner argument.

### Indent Object

- `ai`: the current indentation level and the line above.
- `ii`: the current indentation level excluding the line above.

### Ruby Block

- `ar`: a Ruby block.
- `ir`: inner Ruby block.


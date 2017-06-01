#!/usr/bin/python
# coding: utf-8

import os, re, sqlite3
import argparse
import mistune
from mistune import Renderer
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

parser = argparse.ArgumentParser(description='Convert markdown to a dash cheat sheet.')
parser.add_argument('inputfile', type=argparse.FileType(), help='Markdown input file')
args = parser.parse_args()

FILE=args.inputfile.name
DOCSETNAME=FILE.split('.')[0]
print "Parsing %s into %s.docset" % (FILE, DOCSETNAME)

print "Creating paths..."
os.makedirs("%s.docset/Contents/Resources/Documents" % DOCSETNAME)

print "Creating plist..."
PLIST='''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleIdentifier</key>
	<string>cheatsheet</string>
	<key>CFBundleName</key>
	<string>%s</string>
	<key>DashDocSetFamily</key>
	<string>cheatsheet</string>
	<key>DashDocSetKeyword</key>
	<string>%s</string>
	<key>DashDocSetPluginKeyword</key>
	<string>%s</string>
	<key>DocSetPlatformFamily</key>
	<string>cheatsheet</string>
	<key>dashIndexFilePath</key>
	<string>index.html</string>
	<key>isDashDocset</key>
	<true/>
</dict>
</plist>
''' % (DOCSETNAME, DOCSETNAME.lower(), DOCSETNAME.lower())

with open("%s.docset/Contents/Info.plist" % DOCSETNAME, 'w') as f:
    f.write(PLIST)

print "Creating docSet.dsidx database..."

conn = sqlite3.connect('%s.docset/Contents/Resources/docSet.dsidx' % DOCSETNAME)
cur = conn.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = '%s.docset/Contents/Resources/Documents' % DOCSETNAME


class DashRenderer(Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)
    def reset_toc(self):
        self.toc_tree = []
        self.toc_count = 0

    def header(self, text, level, raw=None):
        rv = '<h%d id="toc-%d">%s</h%d>\n' % (
            level, self.toc_count, text, level
        )
        self.toc_tree.append((self.toc_count, text, level, raw))
        self.toc_count += 1
        return rv

    def render_toc(self, cursor, level=2):
        """Render TOC to SQLITE index.

        :param cursor: sqlite cursor for the inserts
        :param level: render toc to the given level
        """

        for toc in self.toc_tree:
            index, text, l, raw = toc
            path = "index.html#toc-%d" % index
            if l == 1:
                cursor.execute('INSERT INTO searchIndex(name, type, path) VALUES (?,?,?)', (text, 'Category', path))
            elif l == 2:
                cursor.execute('INSERT INTO searchIndex(name, type, path) VALUES (?,?,?)', (text, 'Category', path))
            elif l == 3:
                cursor.execute('INSERT INTO searchIndex(name, type, path) VALUES (?,?,?)', (text, 'Category', path))



toc=DashRenderer()

markdown = mistune.Markdown(renderer = toc)
toc.reset_toc()
text = markdown.parse(args.inputfile.read())
toc.render_toc(cur)
conn.commit()

with open(docpath + "/index.html",'w') as f:
    f.write(text)

    


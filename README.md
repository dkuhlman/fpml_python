# fpml_python

Python support for FpML (Financial products Markup Language) generated with `generateDS.py`

This archive contains Python modules generated from the FpML XML
schemas.  Using Python and these modules will enable you to do the
following:

- Read an FpML XML instance document and create instances of the
  relevant generated classes.

- Manipulate the instances of those classes using Python.

- Create new istances of the Python classes that represent FpML XML
  elements.

- Write (export) the FpML XML instance document.


## Notes on the generated files

Files in this repository with names `fpmllib/xxxxlib.py` contain the class
definitions for each element type defined in the XML Schema.

Files in this repository with names `fpmllib/xxxxxapp.py` contain
subclass definitions for the classes defined in the associated
`fpmllib/xxxxlib.py` file.  If you intend to write custom code that
uses the generated class definitions, you might want to consider
making a copy of the relevant `fpmllib/xxxxxapp.py` file, then
adding your application code to that file.

The XML schemas are those in the archive downloaded from this
location:
[http://www.fpml.org/spec/fpml-5-9-3-wd-3/xml/fpml-5-9-master-schema-and-key-gen-scripts.zip](http://www.fpml.org/spec/fpml-5-9-3-wd-3/xml/fpml-5-9-master-schema-and-key-gen-scripts.zip)


## More information

You can learn more about FpML here: http://www.fpml.org/

You can learn more about `generateDS.py` here:
[http://www.davekuhlman.org/#generateds-py](http://www.davekuhlman.org/#generateds-py)

You can learn more about the Python programming language here:
[https://www.python.org/](https://www.python.org/)


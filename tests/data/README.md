# Example data for attack

The examples are objects of MITRE ATT&CK v20.0, copied from MITRE's bundles
and written as YAML, under the licence that [NOTICE](../../NOTICE)
reproduces. The collection example has its contents cut to the objects of
the bundle example, and each file says so where it differs from MITRE's.

- `valid/` holds an example of each ATT&CK class. `tests/test_data.py`
  validates each, and checks that every ATT&CK class has one.
- `invalid/` holds a counter-example per constraint: a valid example with one
  thing broken. Its first line, `# Fails at: <JSON pointer>`, names where the
  validator must report it, and `tests/test_data.py` holds it to that.
- `attack-stix-data/` pins the ATT&CK release and holds the extract that the
  default tests validate; its README says how.

Each file is named `ClassName-suffix.yaml`, where `ClassName` is the class it
is an example of.

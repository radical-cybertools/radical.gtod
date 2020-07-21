
Package radical.gtod
====================

This Python package provides a single method, `gtod`, which returns the current
time in seconds since epoch (01.01.1970) with sub-second resolution.  The only
difference to time.time() is that this method also provides a binary tool,
`radical-gtod`, which is a *compiled* binary and does not require the invocation
of the Python interpreter (which can be costly for frequent calls to that tool
in a highly concurrent workflow environment).


License
-------

This software is released under the
[LGPL License v3.0](http://opensource.org/licenses/LGPL-3.0).


Usage
-----

* call `radical-gtod`



Releases
========

0.16
----

* The module for Qt widgets testing has been extracted to the separate PyQtest project.

0.15
----

* Widget for phasor diagrams with two scales (for voltage and current) have been added.

0.14
----

* Styles of phasors have been added: 'solid', 'dashed', and 'dotted'.

0.13
----

* The phasor can be made invisible.
* Argument 'end' in phasor diagram was marked as deprecated cause 'circle' is very slow. It is better to add more options for customizing the style of individual phasors.

0.12
----

* Now you can choose the end of the phasor: circle or arrow
* Some deprecated code has been removed

0.11
----

* Functions for getting the parts of version have been added

0.10
----

* The tool for testing of widgets now uses unittest
* Separate package for testing the sqlite schema
* nose2 is recommended to run tests

# 5. Verifying the installation

Run your favorite PyLith example or test problem to insure that PyLith was installed properly.

The output of running `pylith` with no arguments is.

```bash
 >> {default}::
 -- pyre.inventory(error)
 -- meshimporter.meshioascii.filename <- ''
 -- Filename for ASCII input mesh not specified.  To test PyLith, run an example as discussed in the manual.
 >> {default}::
 -- pyre.inventory(error)
 -- timedependent.homogeneous.elasticisotropic3d.label <- ''
 -- Descriptive label for material not specified.
 >> {default}::
 -- pyre.inventory(error)
 -- timedependent.homogeneous.elasticisotropic3d.simpledb.label <- ''
 -- Descriptive label for spatial database not specified.
 >> {default}::
 -- pyre.inventory(error)
 -- timedependent.homogeneous.elasticisotropic3d.simpledb.simpleioascii.filename <- ''
 -- Filename for spatial database not specified.
 pylithapp: configuration error(s)
```

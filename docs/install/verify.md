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
 -- timedependent.problem_defaults.name <- ''
 -- Missing required property 'name' in default options for problem.
 pylithapp: configuration error(s)
 ```

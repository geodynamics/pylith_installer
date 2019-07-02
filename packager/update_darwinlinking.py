#!/usr/bin/env python

"""Script to update links in dynamic libraries and modules on Darwin
to be relative to the bin directory. Run this script in the top-level
directory of the binary distribution.

Based on script used by Satish Balay to update linking for PETSc.
"""

import sys
import glob
import os
import fnmatch
import subprocess


BIN_DIR = "bin"
LIB_DIR = "lib"
PYEGG_ZIPS = ["netCDF4"]


class App(object):
    """Application for updating linking on Darwin.
    """

    def main(self):
        """Main application driver.
        """
        self._update_bin()
        self._update_pymodules()
        self._update_dylibs()
        return

    def _update_bin(self):
        """Update files in 'bin' directory.
        """
        for binfile in glob.glob(os.path.join(BIN_DIR, "*")):
            self._update_deplibs(binfile)
        return

    def _update_pymodules(self):
        """Update Python modules.
        """
        python_version = "%d.%d" % (sys.version_info.major, sys.version_info.minor)
        modules_dir = "lib/python%s/site-packages" % python_version
        for zfile in PYEGG_ZIPS:
            self._unzip(modules_dir, zfile)
        modules = self._find_files(modules_dir, "*.so")
        for module in modules:
            self._update_deplibs(module)
        for zfile in PYEGG_ZIPS:
            self._rezip(modules_dir, zfile)
        return

    def _unzip(self, modules_dir, egg_dir):
        """Unzip Python egg.
        """
        egg = self._get_egg(modules_dir, egg_dir)
        cmd = "unzip {}".format(egg)
        subprocess.check_call(cmd, shell=True, cwd=modules_dir)
        return

    def _rezip(self, modules_dir, egg_dir):
        """Rezip Python egg, deleting egg directory.
        """
        egg = self._get_egg(modules_dir, egg_dir)
        cmd = "zip -ru {} {}".format(egg, egg_dir)
        subprocess.check_call(cmd, shell=True, cwd=modules_dir)
        cmd = "rm -r {}".format(egg_dir)
        subprocess.check_call(cmd, shell=True, cwd=modules_dir)
        return

    def _get_egg(self, modules_dir, egg_dir):
        """Get name of egg file in modules directory.
        """
        egg = glob.glob(os.path.join(modules_dir, "{}*egg".format(egg_dir)))
        if len(egg) != 1:
            raise ValueError("Expected 1 egg, but found {} in directory '{}'.".format(
                egg, modules_dir))
        return os.path.split(egg[0])[-1]

    def _update_dylibs(self):
        """Update dynamic libraries.
        """
        dylibs = self._find_files(LIB_DIR, "*.dylib")
        for lib in dylibs:
            # Can't change stub files
            if lib.startswith("lib/libgcc_ext"):
                continue

            self._update_deplibs(lib)
        return

    def _find_files(self, local_dir, pattern):
        """Find files matching 'pattern' in directory 'local_dir'.
        """
        matches = []
        for root, dirnames, filenames in os.walk(local_dir):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))
        return matches

    def _update_deplibs(self, filename):
        """Update links in file 'filename'.
        """
        # Ignore symbolic links and directories
        if os.path.islink(filename) or os.path.isdir(filename):
            return

        print("Updating {}...".format(filename))

        process = subprocess.Popen(["otool", "-L", filename], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        deplibs = []
        lines = output.split("\t")
        for line in lines[1:]:
            deplibs.append(line.split()[0])
        for deplib_orig in deplibs:
            # Ignore system files
            if deplib_orig.startswith("/usr") or deplib_orig.startswith("/System"):
                continue

            deplib_name = os.path.split(deplib_orig)[-1]
            deplib_new = "@executable_path/../lib/{}".format(deplib_name)
            cmd = "install_name_tool -change {} {} {}".format(deplib_orig, deplib_new, filename)
            subprocess.check_call(cmd, shell=True)

        return


# ======================================================================
if __name__ == "__main__":
    App().main()


# End of file

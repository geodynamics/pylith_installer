#!/usr/bin/env python3
"""Application for managing the PyLith build environment.
"""

import sys
import os
import argparse
import subprocess
import configparser


class Package():
    """Base class for software package.
    """
    NAME = None
    CLONE_RECURSIVE = False

    def __init__(self, config):
        if not "base" in config:
            raise ValueError(f"Configure missing base settings.")
        self.base = config["base"]

        if not self.NAME in config:
            raise ValueError(f"Configure missing settings for '{self.NAME}'.")
        self.config = config[self.NAME]

        self.base["debug"] = self.base["debug"] == "True"
        self.base["build_threads"] = int(self.base["build_threads"])
        self.config["upstream"] = self.config["upstream"] if self.config["upstream"] != "False" else False

    @staticmethod
    def _display(lines):
        print("\n".join(lines))

    def _get_src_dir(self, top=False):
        return os.path.join(self.base["src_dir"], self.NAME) if not top else self.base["src_dir"]

    def _get_build_dir(self):
        build_arch = "debug" if self.base["debug"] else "opt"
        return os.path.join(self.base["build_dir"], build_arch, self.NAME)

    def _get_install_dir(self):
        build_arch = "debug" if self.base["debug"] else "opt"
        return os.path.join(self.base["install_dir"], build_arch)

    def _git_current_branch(self):
        """Get current git branch.
        """
        src_dir = self._get_src_dir()
        if not os.path.exists(src_dir):
            return None
        proc = subprocess.run(["git", "branch"], cwd=src_dir, capture_output=True)
        lines = proc.stdout.decode("utf-8").splitlines()
        for line in lines:
            if line.startswith("* "):
                branch = line[2:].strip()
                return branch
        return None

    def configure(self):
        lines = [f"# Configure '{self.NAME}''."]

        lines += ["# Generate the configure script using autoreconf."]
        lines += ["cd " + self._get_src_dir()]
        lines += ["autoreconf -if"]
        lines += [""]

        lines += ["# Run configure."]
        lines += ["cd " + self._get_build_dir()]
        configure_fullpath = os.path.join(self._get_src_dir(), "configure")
        lines += [f"{configure_fullpath} {self._configure_args()}"]
        lines += ["# After running configure, use --build to see the command for building."]
        self._display(lines)

    def build(self):
        branch = self._git_current_branch()
        lines = [f"# Build branch '{branch}' for '{self.NAME}'."]
        lines += ["cd " + self._get_build_dir()]
        lines += [f"make install -j{self.base['build_threads']}"]
        lines += ["# After building the software, use --test to see the command for testing."]
        self._display(lines)
    
    def test(self):
        lines = [f"# Test '{self.NAME}'."]
        lines += ["cd " + self._get_build_dir()]
        lines += [f"make check -j{self.base['build_threads']}"]
        self._display(lines)

    def git_clone(self):
        lines = [f"# Clone '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir(top=True)]
        cmd = "git clone "
        if self.CLONE_RECURSIVE:
            cmd += " --recursive"
        if self.config["branch"] != "main":
            cmd += f" --branch {self.config['branch']}"
        cmd += " " + self.config["repo_url"]
        lines += [cmd]
        lines += [""]
        lines += ["# When you clone a forked repository, you need to fix the cloning of the m4 submodules."]
        lines += ["git config submodule.m4.url https://github.com/geodynamics/autoconf_cig.git"]
        lines += ["# Repeat for any other m4 submodules, for example `templates/friction/m4`"]
        lines += ["git submodule update"]
        lines += [""]
        lines += ["# After running git clone, use --configure to see how to configure."]
        self._display(lines)
    
    def git_set_upstream(self):
        if not self.config["upstream"]:
            lines = [f"# No upstream repository for '{self.NAME}'."]
        else:
            lines = [f"# Set upstream repository for '{self.NAME}.'"]
            lines += ["cd " + self._get_src_dir()]
            lines += ["git remote -v # Show current remote repositories."]
            lines += [f"git remote add upstream {self.config['upstream']}"]
            lines += ["git remote -v # Verify new upstream"]
        self._display(lines)

    def git_sync_fork(self, branch="main"):
        if not self.config["upstream"]:
            lines = [f"# No upstream repository for '{self.NAME}'."]
        else:
            lines = [f"# Synchronize local branch {branch} for '{self.NAME}.'"]
            lines += ["# NOTE: You must have set the upstream repository. See --git-set-upstream."]
            lines += ["cd " + self._get_src_dir()]
            lines += ["git fetch upstream"]
            lines += [f"git checkout {branch}"]
            lines += [f"git merge upstream/{branch}"]
        self._display(lines)

    def git_fetch(self):
        lines = [f"# Update local clone for '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"git fetch -p"]
        self._display(lines)
        return

    def git_set_branch(self, branch):
        current_branch = self._git_current_branch()
        lines = [f"# Change from branch '{current_branch}' to branch '{branch}' for '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"git checkout {branch}"]
        self._display(lines)
        return

    def git_new_branch(self, branch):
        current_branch = self._git_current_branch()
        lines = [f"# Create new branch '{branch}' from branch '{current_branch}' for '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"git checkout -b {branch}"]
        self._display(lines)
        return

    def git_delete_branch(self, branch):
        lines = [f"# Delete local branch '{branch}' from '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"git branch -D {branch}"]
        self._display(lines)
        return

    def git_rebase(self, ref_branch):
        lines = [
                "DANGER: Rebasing can lead to irreversible changes to your repository!!!",
                "        Only rebase if you are sure you know what you are doing.",
                "",
                "TIP: You should always test your code _after_ rebasing and _before_ pushing to verify",
                "     your changes.",
                "",
                "After successfully rebasing, DO NOT run 'git pull' as git will suggest.",
                "Instead, run 'git push --force'",
                "",
                "If you encounter problems while rebasing, you can abort by running 'git rebase --abort'.",
                "This will return the repository to the state it was in before rebasing.",
                "",
                ]
        lines += [f"# Interactive rebase for '{self.NAME}'."]
        lines += [f"git rebase -i {ref_branch}"]
        self._display(lines)

    def git_replace_branch(self, branch):
        lines = [f"Delete and checkout branch '{branch}' for '{self.NAME}'."]
        lines += [f"git checkout main && git delete -D {branch} && git checkout {branch}"]
        self._display(lines)
        return

    def _configure_args(self):
        return

class Pythia(Package):
    """Pythia package.
    """
    NAME = "pythia"
    CLONE_RECURSIVE = True

    def _configure_args(self):
        args = [
            f"--prefix={self._get_install_dir()}",
            "--enable-testing",
            "CC=mpicc",
            "CXX=mpicxx",
        ]
        if self.base["debug"]:
            args += [
                "CFLAGS='-g -Wall'",
                "CXXFLAGS='-g -Wall'",
            ]
        else:
            args += [
                "CFLAGS='-g -O3 -DNDEBUG'",
                "CXXFLAGS='-g -O3 -DNDEBUG'",
            ]
        return " ".join(args)

class Spatialdata(Package):
    """Spatialdata package.
    """
    NAME = "spatialdata"
    CLONE_RECURSIVE = True

    def _configure_args(self):
        install_dir = self._get_install_dir()
        args = [
            f"--prefix={install_dir}",
            "--enable-swig",
            "--enable-testing",
            "CC=mpicc",
            "CXX=mpicxx",
            f"CPPFLAGS=\"-I{self.base['deps_dir']}/include -I{install_dir}/include\"",
            f"LDFLAGS=\"-L{self.base['deps_dir']}/lib -L{install_dir}/lib\"",
        ]
        if self.base["debug"]:
            args += [
                "CFLAGS='-g -O0 -Wall'",
                "CXXFLAGS='-g -O0 -Wall'",
            ]
        else:
            args += [
                "CFLAGS='-g -O3 -DNDEBUG'",
                "CXXFLAGS='-g -O3 -DNDEBUG'",
            ]
        return " ".join(args)


class Petsc(Package):
    """Petsc package.
    """
    NAME = "petsc"
    CLONE_RECURSIVE = False

    def __init__(self, config):
        super().__init__(config)
        self.petsc_arch = "arch-pylith-debug" if self.base["debug"] else "arch-pylith-opt"
        self.petsc_dir = os.path.join(self.base["src_dir"], "petsc")

    def configure(self):
        lines = [f"# Configure '{self.NAME}''."]

        lines += ["# Run configure."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"python3 ./configure {self._configure_args()}"]
        self._display(lines)

    def build(self):
        lines = [f"# Build '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"make -j{self.base['build_threads']} PETSC_DIR={self.petsc_dir} PETSC_ARCH={self.petsc_arch}"]
        self._display(lines)
    
    def test(self):
        lines = [f"# Test '{self.NAME}'."]
        lines += ["cd " + self._get_src_dir()]
        lines += [f"make check -j{self.base['build_threads']} PETSC_DIR={self.petsc_dir} PETSC_ARCH={self.petsc_arch}"]
        self._display(lines)
    
    def _configure_args(self):
        install_dir = self._get_install_dir()
        args = [
            "--with-c2html=0",
            "--with-lgrind=0",
            "--with-fc=0",
            "--with-x=0",
            "--with-clanguage=C",
            "--with-mpicompilers=1",
            "--with-shared-libraries=1",
            "--with-64-bit-points=1",
            "--with-large-file-io=1",
            "--with-hdf5=1",
            "--download-chaco=1",
            "--download-ml=1",
            "--download-f2cblaslapack=1",
        ]
        if self.base["debug"]:
                args += [
                "--with-debugging=1",
                "CFLAGS='-g -O0 -Wall'",
                ]
        else:
                args += [
                "--with-debugging=0",
                "CFLAGS='-g -O3 -DNDEBUG'",
                ]
        args += [
            f"CPPFLAGS=\"-I$HDF5_INCDIR -I{self.base['deps_dir']}/include\"",
            f"LDFLAGS=\"-L$HDF5_LIBDIR -L{self.base['deps_dir']}/lib\"",
            f"PETSC_DIR={self.petsc_dir}",
            f"PETSC_ARCH={self.petsc_arch}",
        ]
        return " ".join(args)


class PyLith(Package):
    """PyLith package.
    """
    NAME = "pylith"
    CLONE_RECURSIVE = True

    def _configure_args(self):
        install_dir = self._get_install_dir()
        args = [
            f"--prefix={install_dir}",
            "--enable-cubit",
            "--enable-hdf5",
            "--enable-swig",
            "--enable-testing",
            "CC=mpicc",
            "CXX=mpicxx",
            f"CPPFLAGS=\"-I$HDF5_INCDIR -I{self.base['deps_dir']}/include -I{install_dir}/include\"",
            f"LDFLAGS=\"-L$HDF5_LIBDIR -L{self.base['deps_dir']}/lib -L{install_dir}/lib\"",
        ]
        if self.base["debug"]:
            args += [
                "CFLAGS='-g -O0 -Wall'",
                "CXXFLAGS='-g -O0 -Wall'",
            ]
        else:
            args += [
                "CFLAGS='-g -O3 -DNDEBUG'",
                "CXXFLAGS='-g -O3 -DNDEBUG'",
            ]
        return " ".join(args)

def create_package(name, config):
    if name == "pythia":
        return Pythia(config)
    elif name == "spatialdata":
        return Spatialdata(config)
    elif name == "petsc":
        return Petsc(config)
    elif name == "pylith":
        return PyLith(config)
    else:
        raise ValueError(f"Unknown package {name}.")


class App():
    """Main application.
    """

    def __init__(self):
        """Constructor."""
        self.config = None

    def main(self):
        """Main entry point.
        """
        args = self._parse_command_line()
        self.initialize(args.config)

        if args.show_config:
            self.show_config()

        package = create_package(args.package, self.config)
        if args.git_clone:
            package.git_clone()
        if args.git_set_upstream:
            package.git_set_upstream()
        if args.git_sync_fork:
            package.git_sync_fork()
        if args.git_fetch:
            package.git_fetch()
        if args.git_set_branch:
            package.git_set_branch(args.git_set_branch)
        if args.git_new_branch:
            package.git_new_branch(args.git_new_branch)
        if args.git_delete_branch:
            package.git_delete_branch(args.git_delete_branch)
        if args.git_rebase:
            package.git_rebase(args.git_rebase)
        if args.git_replace_branch:
            package.git_replace_branch(args.git_replace_branch)

        if args.configure:
            package.configure()
        if args.build:
            package.build()
        if args.test:
            package.test()

    def initialize(self, filename, keep_case=True, verbose=False):
        """Set parameters from config file.

        Args:
            filenames (list)
                List of .cfg files to read.
            keep_case (bool)
                If True, maintain case in section headings, otherwise convert to lowercase.
            verbose (bool)
                If True, print out progress.

        Returns:
            Dictionary with configuration.
        """
        if not os.path.isfile(filename):
            raise IOError(f"Could not find configuration file '{filename}'.")
        if verbose:
            print(f"Fetching parameters from {filename}...")
        config = configparser.ConfigParser()
        config.read(filename)
        self.config = {s: dict(config.items(s)) for s in config.sections()}

    def show_config(self):
        """Write configuration to stdout.
        """
        parser = configparser.ConfigParser()
        parser.read_dict(self.config)
        parser.write(sys.stdout)

    def _parse_command_line(self):
        """Parse command line arguments.
        """
        DESCRIPTION = (
            "Application for managing the PyLith development environment. "
            "Once you become familiar with the build environment you will not need this utility."
        )
        PACKAGES = ["pythia", "spatialdata", "petsc", "pylith"]

        parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser.add_argument("--config", action="store", dest="config", required=True)
        parser.add_argument("--package", action="store", dest="package", choices=PACKAGES, required=True)

        parser.add_argument("--git-clone", action="store_true", dest="git_clone")
        parser.add_argument("--git-set-upstream", action="store_true", dest="git_set_upstream")
        parser.add_argument("--git-sync-fork", action="store_true", dest="git_sync_fork")
        parser.add_argument("--git-set-branch", action="store", dest="git_set_branch", metavar="BRANCH")
        parser.add_argument("--git-new-branch", action="store", dest="git_new_branch", metavar="BRANCH")
        parser.add_argument("--git-delete-branch", action="store", dest="git_delete_branch", metavar="BRANCH")
        parser.add_argument("--git-fetch", action="store_true", dest="git_fetch")
        parser.add_argument("--git-rebase", action="store", dest="git_rebase", metavar="REF_BRANCH")
        parser.add_argument("--git-replace-branch", action="store", dest="git_replace_branch", metavar="BRANCH")

        parser.add_argument("--configure", action="store_true", dest="configure")
        parser.add_argument("--build", action="store_true", dest="build")
        parser.add_argument("--test", action="store_true", dest="test")

        parser.add_argument("--show-config", action="store_true", dest="show_config")
        args = parser.parse_args()
        return args


if __name__ == "__main__":
    App().main()


# End of file

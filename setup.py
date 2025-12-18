#!/usr/bin/env python
"""
Setup script for rgbmatrix Python bindings.

This builds the C++ library and Cython extension for controlling
RGB LED matrices with Raspberry Pi GPIO.
"""

import os
import subprocess
import sys
from pathlib import Path

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class BuildExtWithLibrary(build_ext):
    """Custom build_ext that builds the C++ library first."""

    def run(self):
        # Build the C++ library before building the extension
        self.build_cpp_library()
        super().run()

    def build_cpp_library(self):
        """Build the rgbmatrix C++ library using make."""
        # Get the directory where setup.py is located
        setup_dir = Path(__file__).parent.absolute()
        lib_dir = setup_dir / "lib"

        self.announce("Building rgbmatrix C++ library...", level=3)

        try:
            subprocess.check_call(
                ["make", "-C", str(lib_dir)],
                cwd=str(setup_dir),
            )
        except subprocess.CalledProcessError as e:
            sys.exit(f"Failed to build C++ library: {e}")
        except FileNotFoundError:
            sys.exit("'make' command not found. Please install build-essential.")


def get_extension():
    """Create the Cython extension module."""
    # Use relative paths (relative to setup.py location)
    sources = [
        os.path.join("bindings", "python", "rgbmatrix", "core.pyx"),
        os.path.join("bindings", "python", "rgbmatrix", "shims", "pillow.c"),
    ]

    # Include directories (these can be absolute for compiler)
    setup_dir = Path(__file__).parent.absolute()
    include_dirs = [
        str(setup_dir / "include"),
        str(setup_dir / "bindings" / "python" / "rgbmatrix" / "shims"),
    ]

    # Library directories
    library_dirs = [
        str(setup_dir / "lib"),
    ]

    return Extension(
        name="rgbmatrix.core",
        sources=sources,
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        libraries=["rgbmatrix"],
        extra_compile_args=["-O3", "-Wall"],
        language="c++",
    )


# Check for Cython
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False


def get_extensions():
    """Get extension modules, using Cython if available."""
    ext = get_extension()

    if USE_CYTHON:
        # Include the rgbmatrix directory for .pxd files
        setup_dir = Path(__file__).parent.absolute()
        return cythonize(
            [ext],
            include_path=[str(setup_dir / "bindings" / "python" / "rgbmatrix")],
            compiler_directives={
                "language_level": "3",
                "boundscheck": False,
                "wraparound": False,
            },
        )
    else:
        # If Cython is not available, expect pre-generated .cpp file
        ext.sources[0] = ext.sources[0].replace(".pyx", ".cpp")
        return [ext]


setup(
    ext_modules=get_extensions(),
    cmdclass={"build_ext": BuildExtWithLibrary},
)

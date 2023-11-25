import os
from typing import Any
from distutils.core import setup
from Cython.Build import cythonize  # type: ignore
from distutils.extension import Extension
from distutils.command.build_ext import build_ext
from distutils.command.build import build
from ..models import FileData
from ..constant import BUILD_DIR
from .abstract_builder import AbstractBuilder


class RedefineBuild(build):
    """
    A subclass of `distutils.command.build` that redefines the base build directory during compilation.

    Overrides the `initialize_options` method to set the build directory to a custom path specified
    by the `BUILD_DIR` constant.
    """

    def initialize_options(self) -> None:
        """
        Initialize build task options by setting the build directory to the value specified in `BUILD_DIR`.
        """
        super().initialize_options()
        self.build_base = BUILD_DIR


class CythonBuilder(AbstractBuilder):
    """
    A builder class for compiling Cython extensions.

    Inherits from `AbstractBuilder`, and is used for compiling Cython modules with custom build
    location and additional compiler directives.
    """

    def redefine_inplace(self, abs_fullpath: str) -> Any:
        """
        Creates and returns a subclass of `build_ext` that modifies the path to place compiled
        extensions to match a given absolute path.

        :param abs_fullpath: The absolute path where the compiled extensions will be placed.
        :return: A subclass `BuildExtInplace` with an overridden `get_ext_fullpath` method.
        """

        class BuildExtInplace(build_ext):
            # -- Name generators -----------------------------------------------
            # (extension names, filenames, whatever)
            def get_ext_fullpath(self, ext_name: str) -> str:
                """Returns the path of the filename for a given extension.

                The file is located in `build_lib` or directly in the package
                (inplace option).
                """
                fullname = self.get_ext_fullname(ext_name)  # type: ignore
                modpath = fullname.split(".")
                filename = self.get_ext_filename(modpath[-1])  # type: ignore

                # returning
                #   package_dir/filename
                return os.path.join(abs_fullpath, filename)

        return BuildExtInplace

    def build(self, file: FileData) -> None:
        """
        Builds a Cython module from given file data.

        :param file: A `FileData` object containing information about the file to be compiled.
        """
        abs_fullpath = os.path.dirname(file.path)
        extension = [Extension(file.name, [str(file.path)])]
        setup(
            ext_modules=cythonize(
                extension,
                compiler_directives={
                    "c_string_type": "str",
                    "c_string_encoding": "utf8",
                    "language_level": 3,
                },
            ),
            cmdclass={
                "build": RedefineBuild,
                "build_ext": self.redefine_inplace(abs_fullpath),
            },
            script_args=["build_ext", "--inplace"],
        )

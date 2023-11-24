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
    def initialize_options(self) -> None:
        super().initialize_options()
        self.build_base = BUILD_DIR


class CythonBuilder(AbstractBuilder):
    def redefine_inplace(self, abs_fullpath: str) -> Any:
        # Define a subclass of build_ext to add the inplace
        class BuildExtInplace(build_ext):
            # -- Name generators -----------------------------------------------
            # (extension names, filenames, whatever)
            def get_ext_fullpath(self, ext_name: str) -> str:
                """Returns the path of the filename for a given extension.

                The file is located in `build_lib` or directly in the package
                (inplace option).
                """
                fullname = self.get_ext_fullname(ext_name)
                modpath = fullname.split(".")
                filename = self.get_ext_filename(modpath[-1])

                # returning
                #   package_dir/filename
                return os.path.join(abs_fullpath, filename)

        return BuildExtInplace

    def build(self, file: FileData) -> None:
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

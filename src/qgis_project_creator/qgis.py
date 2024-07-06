"""
Creation Date: 2024-07-06
Author: Florian Frosch
Purpose: Singleton instance of QgsApplication
Description:
    This defines a singleton instance of QgsApplication.
    Every other approach trying to manage the QgsApplication instance
    using `QgsApplication.exitQgis()` didn't work and crashed the Python kernel.
"""

import os
from dataclasses import dataclass
from pathlib import Path

from qgis.core import (
    QgsApplication,
    QgsCoordinateReferenceSystem,
    QgsProject,
    QgsProjectMetadata,
)


def _qgis() -> QgsApplication:
    # Setting the second argument to False disables the GUI.
    # https://qgis.org/pyqgis/master/core/QgsApplication.html
    instance = QgsApplication([], False)
    # Load providers
    instance.initQgis()
    return instance


# Singleton instance of QgsApplication
# Automatically instantiated when anything from this module is imported
QGIS: QgsApplication = _qgis()


class Project:
    """Create a QGIS project.

    All files will be written rlative to `self.settings.project_home`.

    `self.project` is the QgsProject instance, available for further customization by the user.
    """

    def __init__(self, metadata: "Metadata", settings: "Settings") -> None:
        self.metadata = metadata
        self.settings = settings

        self.project = QgsProject()

    def to_qgz(self, path: str | Path, overwrite: bool = False) -> None:
        """Write the project to a QGS/QGZ file.

        Parameters
        ----------
        path : str | Path
            Path relative to `self.settings.project_home`
        overwrite : bool, optional
            Whether to overwrite the file if it already exists, by default False
        """
        if Path(path).suffix != ".qgz" and Path(path).suffix != ".qgs":
            raise ValueError("File must have a .qgz or .qgs extension.")

        if os.path.isabs(path):
            raise ValueError("Path must be relative to `self.settings.project_home`.")

        if Path(path).is_dir():
            raise OSError("Path points to a directory. Specify a file name.")

        if Path(path).exists() and not overwrite:
            raise OSError("File already exists. Set `overwrite=True` to overwrite.")

        # Convert to absolute path
        # Format as string for compatibility with QgsProject.write()
        path = (Path(self.settings.project_home) / path).as_posix()

        metadata = QgsProjectMetadata()
        metadata.setAuthor(self.metadata.author)

        self.project.setCrs(QgsCoordinateReferenceSystem.fromEpsgId(self.settings.epsg))
        self.project.setMetadata(metadata)
        self.project.setPresetHomePath(str(self.settings.project_home))
        self.project.setTitle(self.metadata.title)

        self.project.write(path)


@dataclass
class Metadata:
    author: str = ""
    title: str = ""
    description: str = ""
    version: str = ""


@dataclass
class Settings:
    epsg: int
    project_home: str | Path

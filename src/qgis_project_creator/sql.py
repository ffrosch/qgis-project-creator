from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

from sqlalchemy.orm import mapped_column as sa_mapped_column

from .qgis import Widget

P = ParamSpec("P")
T = TypeVar("T")


def _add_widget(f: Callable[P, T]) -> Callable[Concatenate[Widget, P], T]:
    """Decorator to add the `widget` argument to `mapped_column`.

    This is remapped by the wrapper to the `info` keyword argument of the original `mapped_column`. The `info` argument is not parsed by SQLAlchemy and is meant to be used for the storage of arbitrary data.
    See: https://github.com/sqlalchemy/sqlalchemy/discussions/11511

    More about the the usage of ParamSpec:
    - https://stackoverflow.com/questions/71968447/python-typing-copy-kwargs-from-one-function-to-another
    - https://stackoverflow.com/questions/74714300/paramspec-for-a-pre-defined-function-without-using-generic-callablep
    """
    if f is not sa_mapped_column:
        raise RuntimeError("Exclusive decorator for `mapped_column`.")

    def wrapper(widget: Widget, *args: P.args, **kwargs: P.kwargs) -> T:
        kwargs["info"] = {"widget": widget}
        return f(*args, **kwargs)

    return wrapper


mapped_column = _add_widget(sa_mapped_column)

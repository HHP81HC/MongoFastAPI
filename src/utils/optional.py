"""optional.py"""

# Standard Library
from copy import deepcopy
from typing import Any
from typing import Type
from typing import Tuple
from typing import Optional

from pydantic import BaseModel
from pydantic import create_model
from pydantic.fields import FieldInfo


def partial_model(model: Type[BaseModel]):
    """Decorator to make all the fields in schema Optional

    """
    def make_field_optional(field: FieldInfo, default: Any = None) -> Tuple[Any, FieldInfo]:
        new = deepcopy(field)
        new.default = default
        new.annotation = Optional[field.annotation]  # type: ignore
        return new.annotation, new

    return create_model(
        f"Partial{model.__name__}",
        __base__=model,
        __module__=model.__module__,
        **{field_name: make_field_optional(field_info) for field_name, field_info in model.__fields__.items()},
    )

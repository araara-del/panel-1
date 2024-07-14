import datetime as dt
import json

from typing import TYPE_CHECKING, Any, Iterable

import param

from param.reactive import bind

from ..pane.markup import JSON
from ..util import classproperty
from .base import ModelUtils

if TYPE_CHECKING:
    try:
        from pydantic import BaseModel
    except ModuleNotFoundError:
        BaseModel = Any
else:
    BaseModel = Any

def default_serializer(obj):
    if isinstance(obj, (dt.datetime, dt.date)):
        return obj.isoformat()
    raise TypeError()


class PydanticUtils(ModelUtils):

    can_observe_field = False

    supports_constant_fields = False

    @classmethod
    def get_field_names(cls, model: BaseModel) -> Iterable[str]:
        return tuple(model.model_fields)

    @classmethod
    def observe_field(
        cls,
        model,
        field: str,
        handle_change,
    ):
        # We don't know if this is possible
        # Maybe solution can be found in
        # https://github.com/pydantic/pydantic/discussions/7127 or
        # https://psygnal.readthedocs.io/en/latest/API/model/
        pass

    @classproperty
    def parameter_map(cls):
        return {
            bool: param.Boolean,
            int: param.Integer,
            float: param.Number,
            str: param.String,
            list: param.List,
            tuple: param.Tuple,
            dict: param.Dict,
        }
    @classmethod
    def create_parameter(cls, model, field: str)->param.Parameter:
        field_type = model.__annotations__[field]
        ptype = cls.parameter_map.get(field_type, param.Parameter)
        return ptype()

    @classmethod
    def get_layout(cls, model, self, layout_params):
        def view_model(*args):
            if hasattr(model, 'model_dump'):
                return model.model_dump()
            else:
                return json.loads(model.json())

        return JSON(
            bind(view_model, *self.param.objects().values()),
            default=default_serializer,
            depth=2,
            **layout_params
        )

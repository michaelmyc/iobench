from enum import Enum

import tomli_w

from iobench.data.generator import DataGenerationConfig


class StrEnum(str, Enum):
    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value


class ConfigBaseClass:
    def _to_dict(self) -> dict:
        config_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, ConfigBaseClass):
                config_dict[k] = v._to_dict()
            elif isinstance(v, Enum):
                config_dict[k] = v.value
            elif (
                isinstance(v, list)
                and len(v) > 0
                and isinstance(v[0], DataGenerationConfig)
            ):
                config_dict[k] = [str(x) for x in v]
            else:
                config_dict[k] = v

        return config_dict

    def __str__(self) -> str:
        return tomli_w.dumps(self._to_dict())

    def __repr__(self) -> str:
        return str(self.__dict__)

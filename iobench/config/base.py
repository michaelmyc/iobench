from enum import Enum

import tomli_w


class ConfigBaseClass:
    def _to_dict(self) -> dict:
        config_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, ConfigBaseClass):
                config_dict[k] = v._to_dict()
            elif isinstance(v, Enum):
                config_dict[k] = v.value
            else:
                config_dict[k] = v

        return config_dict

    def __str__(self) -> str:
        return tomli_w.dumps(self._to_dict())

    def __repr__(self) -> str:
        return str(self.__dict__)

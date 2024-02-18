import re
from dataclasses import dataclass
from enum import Enum
from typing import Self


class BaseUnitPreference(Enum):
    Bits = 1
    Bytes = 2


class UnitPrefixPreference(Enum):
    Decimal = 1
    Binary = 2


class BaseUnit(float, Enum):
    b = 1 / 8
    B = 1


class UnitPrefix(float, Enum):
    pass


class DecimalUnitPrefix(UnitPrefix):
    K = 1000
    M = 1000**2
    G = 1000**3
    T = 1000**4
    P = 1000**5


class BinaryUnitPrefix(UnitPrefix):
    Ki = 1024
    Mi = 1024**2
    Gi = 1024**3
    Ti = 1024**4
    Pi = 1024**5


@dataclass
class Unit:
    prefix: UnitPrefix
    base: BaseUnit

    def to_bytes(self) -> float:
        return self.prefix.value * self.base.value

    @classmethod
    def get_best_unit(
        cls: Self,
        n_bytes: float,
        base_unit_preference: BaseUnitPreference,
        unit_prefix_preference: UnitPrefixPreference,
    ) -> Self:
        if base_unit_preference == BaseUnitPreference.Bits:
            base = BaseUnit.b
        elif base_unit_preference == BaseUnitPreference.Bytes:
            base = BaseUnit.B
        else:
            raise NotImplementedError()

        if unit_prefix_preference == UnitPrefixPreference.Decimal:
            PrefixClass = DecimalUnitPrefix
        elif unit_prefix_preference == UnitPrefixPreference.Binary:
            PrefixClass = BinaryUnitPrefix
        else:
            raise NotImplementedError()

        for prefix in sorted(PrefixClass, reverse=True):
            if n_bytes / prefix >= 1:
                return cls(prefix, base)
        return cls(sorted(PrefixClass)[0], base)


class SizeUnit(Unit):
    @staticmethod
    def from_string(s: str) -> Self:
        base = BaseUnit[s[-1]]
        try:
            prefix = DecimalUnitPrefix[s[:-1]]
        except:
            prefix = BinaryUnitPrefix[s[:-1]]
        return SizeUnit(prefix, base)

    def __repr__(self) -> str:
        return f"{self.prefix.name}{self.base.name}"

    def __str__(self) -> str:
        return repr(self)


class PerSecondSpeedUnit(Unit):
    @staticmethod
    def from_string(s: str) -> Self:
        base = BaseUnit(s[-3])
        try:
            prefix = DecimalUnitPrefix[s[:-3]]
        except:
            prefix = BinaryUnitPrefix[s[:-3]]
        return SizeUnit(prefix, base)

    def __repr__(self) -> str:
        if self.base == BaseUnit.B:
            return f"{self.prefix.name}{self.base.name}/s"
        elif self.base == BaseUnit.b:
            return f"{self.prefix.name}{self.base.name}ps"
        else:
            raise NotImplementedError()

    def __str__(self) -> str:
        return repr(self)


class ValueWithUnit:
    def __init__(self, amount: float, unit: Unit) -> None:
        self.amount = amount
        self.unit = unit

    def to_bytes(self) -> float:
        return self.amount * self.unit.to_bytes()

    @classmethod
    def to_unit(cls, new_unit: Unit) -> Self:
        new_amount = cls.to_bytes() / new_unit.to_bytes()
        return cls(new_amount, new_unit)

    @staticmethod
    def _parse_value(s: str) -> float:
        return float(re.findall("(\d+(?:\.\d+)?)", s)[0])

    @staticmethod
    def _parse_unit_str(s: str) -> str:
        return re.findall("[a-zA-Z]+", s)[-1]

    def __repr__(self) -> str:
        return f"{self.amount} {self.unit}"

    def __str__(self) -> str:
        return repr(self)


class Size(ValueWithUnit):
    amount: float
    unit: SizeUnit

    @staticmethod
    def from_bytes(n_bytes: float) -> Self:
        unit: SizeUnit = SizeUnit.get_best_unit(
            n_bytes, BaseUnitPreference.Bytes, UnitPrefixPreference.Binary
        )
        amount = n_bytes / unit.to_bytes()
        return Size(amount, unit)

    @staticmethod
    def from_string(s: str) -> Self:
        amount = Size._parse_value(s)
        unit = SizeUnit.from_string(Size._parse_unit_str(s))
        return Size(amount, unit)


class PerSecondSpeed(ValueWithUnit):
    amount: float
    unit: PerSecondSpeedUnit

    def to_bandwidth(self) -> Self:
        n_bytes = self.to_bytes()
        unit: PerSecondSpeedUnit = PerSecondSpeedUnit.get_best_unit(
            n_bytes, BaseUnitPreference.Bits, UnitPrefixPreference.Decimal
        )
        amount = n_bytes / unit.to_bytes()
        return PerSecondSpeed(amount, unit)

    @staticmethod
    def from_bytes(n_bytes: float) -> Self:
        unit: PerSecondSpeedUnit = PerSecondSpeedUnit.get_best_unit(
            n_bytes, BaseUnitPreference.Bytes, UnitPrefixPreference.Binary
        )
        amount = n_bytes / unit.to_bytes()
        return PerSecondSpeed(amount, unit)

    @staticmethod
    def from_string(s: str) -> Self:
        amount = Size._parse_value(s)
        unit = PerSecondSpeedUnit.from_string(Size._parse_unit_str(s))
        return PerSecondSpeed(amount, unit)

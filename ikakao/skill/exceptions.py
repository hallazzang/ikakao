__all__ = ("UnsupportedFieldWarning", "StructureError")


class FieldConstraintWarning(Warning):
    pass


class UnsupportedFieldWarning(Warning):
    pass


class StructureError(Exception):
    pass

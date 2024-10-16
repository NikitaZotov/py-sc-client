from __future__ import annotations

import warnings

from sc_client.constants.exceptions import InvalidTypeError
from sc_client.constants.sc_type import bitmasks


class ScType:
    def __init__(self, value: int = 0):
        if not isinstance(value, (ScType, int)):
            raise InvalidTypeError("You should to use int or ScType type for ScType initialization")
        if isinstance(value, ScType):
            value = value.value
        self.value = value

    def __repr__(self) -> str:
        return f"ScType({hex(self.value)})"

    def __hash__(self) -> int:
        return hash((self.value, self.__class__))

    def __rshift__(self, alias: str) -> tuple[ScType, str]:
        return self, alias

    def __eq__(self, other: ScType) -> bool:
        if isinstance(other, ScType):
            return self.value == other.value
        return NotImplemented

    def __bool__(self) -> bool:
        return self.value != 0

    def has_constancy(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_CONSTANCY_MASK) != 0

    def is_node(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE) != 0

    def is_connector(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_CONNECTOR) != 0

    def is_edge(self) -> bool:
        warnings.warn("ScType `is_edge` method is deprecated. Use `is_connector` method instead.", DeprecationWarning)
        return self.is_connector()

    def is_common_edge(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_COMMON_EDGE) != 0

    def is_arc(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_ARC) != 0

    def is_common_arc(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_COMMON_ARC) != 0

    def is_membership_arc(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_MEMBERSHIP_ARC) != 0

    def is_link(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_LINK) == bitmasks.SC_TYPE_NODE_LINK

    def is_const(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_CONST) != 0

    def is_var(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_VAR) != 0

    def is_pos(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_POS_ARC) == bitmasks.SC_TYPE_POS_ARC

    def is_neg(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NEG_ARC) == bitmasks.SC_TYPE_NEG_ARC

    def is_fuz(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_FUZ_ARC) == bitmasks.SC_TYPE_FUZ_ARC

    def is_perm(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_PERM_ARC) == bitmasks.SC_TYPE_PERM_ARC

    def is_temp(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_TEMP_ARC) == bitmasks.SC_TYPE_TEMP_ARC

    def is_actual(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_ACTUAL_ARC) == bitmasks.SC_TYPE_ACTUAL_ARC

    def is_inactual(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_INACTUAL_ARC) == bitmasks.SC_TYPE_INACTUAL_ARC

    def is_tuple(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_TUPLE) == bitmasks.SC_TYPE_NODE_TUPLE

    def is_structure(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_STRUCTURE) == bitmasks.SC_TYPE_NODE_STRUCTURE

    def is_struct(self) -> bool:
        warnings.warn("ScType `is_struct` method is deprecated. Use `is_structure` method instead.", DeprecationWarning)
        return self.is_structure()

    def is_role(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_ROLE) == bitmasks.SC_TYPE_NODE_ROLE

    def is_no_role(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_NO_ROLE) == bitmasks.SC_TYPE_NODE_NO_ROLE

    def is_norole(self) -> bool:
        warnings.warn("ScType `is_norole` method is deprecated. Use `is_no_role` method instead.", DeprecationWarning)
        return self.is_no_role()

    def is_class(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_CLASS) == bitmasks.SC_TYPE_NODE_CLASS

    def is_superclass(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_SUPERCLASS) == bitmasks.SC_TYPE_NODE_SUPERCLASS

    def is_material(self) -> bool:
        return (self.value & bitmasks.SC_TYPE_NODE_MATERIAL) == bitmasks.SC_TYPE_NODE_MATERIAL

    def is_valid(self) -> bool:
        return self.__bool__()

    def is_equal(self, other: ScType) -> bool:
        return self.__eq__(other)
    
    def _is_not_compatible_by_mask(self, new_type: ScType, mask):
        subtype = self.value & mask
        new_subtype = new_type.value & mask
        return subtype != bitmasks.SC_TYPE_UNKNOWN and subtype != new_subtype
    
    def _is_expendable_to(self, new_type: ScType): # it is equal to `sc_storage_is_type_expendable_to` in the sc-machine
        self_value = self.value
        new_value = new_type.value

        if self._is_not_compatible_by_mask(new_type, bitmasks.SC_TYPE_ELEMENT_MASK):
            return False
        if self._is_not_compatible_by_mask(new_type, bitmasks.SC_TYPE_CONSTANCY_MASK):
            return False

        if self.is_link():
            if not new_type.is_link():
                return False

            self_value = ScType(self_value & ~bitmasks.SC_TYPE_NODE_LINK)
            new_value = ScType(new_value & ~bitmasks.SC_TYPE_NODE_LINK)

            if self_value._is_not_compatible_by_mask(new_value, bitmasks.SC_TYPE_NODE_LINK_MASK):
                return False

        elif self.is_node():
            if not new_type.is_node():
                return False

            self_value = ScType(self_value & ~bitmasks.SC_TYPE_NODE)
            new_value = ScType(new_value & ~bitmasks.SC_TYPE_NODE)

            if self_value._is_not_compatible_by_mask(new_value, bitmasks.SC_TYPE_NODE_MASK):
                return False

        elif self.is_connector():
            if not new_type.is_connector():
                return False

            if self._is_not_compatible_by_mask(new_type, bitmasks.SC_TYPE_CONNECTOR_MASK):
                if self.is_common_edge():
                    if not new_type.is_common_edge():
                        return False
                elif self.is_arc():
                    if not new_type.is_arc():
                        return False

                    if self.is_common_arc():
                        if not new_type.is_common_arc():
                            return False
                    elif self.is_membership_arc():
                        if not new_type.is_membership_arc():
                            return False

            self_value = ScType(self_value & ~bitmasks.SC_TYPE_CONNECTOR_MASK)
            new_value = ScType(new_value & ~bitmasks.SC_TYPE_CONNECTOR_MASK)

            if self_value._is_not_compatible_by_mask(new_value, bitmasks.SC_TYPE_ACTUALITY_MASK):
                return False

            if self_value._is_not_compatible_by_mask(new_value, bitmasks.SC_TYPE_PERMANENCY_MASK):
                return False

            if self_value._is_not_compatible_by_mask(new_value, bitmasks.SC_TYPE_POSITIVITY_MASK):
                return False

        return True

    def merge(self, other: ScType) -> ScType:
        if not self._is_expendable_to(other):
            raise InvalidTypeError(f"Type `{self}` can not be expended to `{other}`.")
        return ScType(self.value | other.value)

    def change_const(self, is_const: bool) -> ScType:
        v = self.value & ~bitmasks.SC_TYPE_CONSTANCY_MASK
        return ScType(v | (bitmasks.SC_TYPE_CONST if is_const else bitmasks.SC_TYPE_VAR))

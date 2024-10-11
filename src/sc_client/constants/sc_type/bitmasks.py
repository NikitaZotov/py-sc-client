# sc-element types
SC_TYPE_UNKNOWN = 0
SC_TYPE_NODE = 0x1
SC_TYPE_CONNECTOR = 0x4000
SC_TYPE_COMMON_EDGE = SC_TYPE_CONNECTOR | 0x4
SC_TYPE_ARC = SC_TYPE_CONNECTOR | 0x8000
SC_TYPE_COMMON_ARC = SC_TYPE_ARC | 0x8
SC_TYPE_MEMBERSHIP_ARC = SC_TYPE_ARC | 0x10

# sc-element constancy
SC_TYPE_CONST = 0x20
SC_TYPE_VAR = 0x40

# sc-arc actuality
SC_TYPE_ACTUAL_ARC = SC_TYPE_MEMBERSHIP_ARC | 0x1000
SC_TYPE_INACTUAL_ARC = SC_TYPE_MEMBERSHIP_ARC | 0x2000

# sc-arc permanence
SC_TYPE_TEMP_ARC = SC_TYPE_MEMBERSHIP_ARC | 0x400
SC_TYPE_PERM_ARC = SC_TYPE_MEMBERSHIP_ARC | SC_TYPE_ACTUAL_ARC | 0x800

# sc-arc positivity
SC_TYPE_POS_ARC = SC_TYPE_MEMBERSHIP_ARC | 0x80
SC_TYPE_NEG_ARC = SC_TYPE_MEMBERSHIP_ARC | 0x100
SC_TYPE_FUZ_ARC = SC_TYPE_MEMBERSHIP_ARC | 0x200

# semantic sc-node types
SC_TYPE_NODE_LINK = SC_TYPE_NODE | 0x2
SC_TYPE_NODE_TUPLE = SC_TYPE_NODE | 0x80
SC_TYPE_NODE_STRUCTURE = SC_TYPE_NODE | 0x100
SC_TYPE_NODE_ROLE = SC_TYPE_NODE | 0x200
SC_TYPE_NODE_NO_ROLE = SC_TYPE_NODE | 0x400
SC_TYPE_NODE_CLASS = SC_TYPE_NODE | 0x800
SC_TYPE_NODE_SUPERCLASS = SC_TYPE_NODE | 0x1000
SC_TYPE_NODE_MATERIAL = SC_TYPE_NODE | 0x2000

# TYPE MASK
SC_TYPE_ELEMENT_MASK = SC_TYPE_NODE | SC_TYPE_CONNECTOR
SC_TYPE_CONNECTOR_MASK = SC_TYPE_COMMON_EDGE | SC_TYPE_COMMON_ARC | SC_TYPE_MEMBERSHIP_ARC
SC_TYPE_ARC_MASK = SC_TYPE_COMMON_ARC | SC_TYPE_MEMBERSHIP_ARC

SC_TYPE_CONSTANCY_MASK = SC_TYPE_CONST | SC_TYPE_VAR
SC_TYPE_ACTUALITY_MASK = SC_TYPE_ACTUAL_ARC | SC_TYPE_INACTUAL_ARC
SC_TYPE_PERMANENCY_MASK = SC_TYPE_PERM_ARC | SC_TYPE_TEMP_ARC
SC_TYPE_POSITIVITY_MASK = SC_TYPE_POS_ARC | SC_TYPE_NEG_ARC | SC_TYPE_FUZ_ARC

SC_TYPE_MEMBERSHIP_ARC_MASK = SC_TYPE_ACTUALITY_MASK | SC_TYPE_PERMANENCY_MASK | SC_TYPE_POSITIVITY_MASK
SC_TYPE_COMMON_ARC_MASK = SC_TYPE_COMMON_ARC
SC_TYPE_COMMON_EDGE_MASK = SC_TYPE_COMMON_EDGE

SC_TYPE_NODE_MASK = (
    SC_TYPE_NODE_LINK
    | SC_TYPE_NODE_TUPLE
    | SC_TYPE_NODE_STRUCTURE
    | SC_TYPE_NODE_ROLE
    | SC_TYPE_NODE_NO_ROLE
    | SC_TYPE_NODE_CLASS
    | SC_TYPE_NODE_SUPERCLASS
    | SC_TYPE_NODE_MATERIAL
)

SC_TYPE_NODE_LINK_MASK = SC_TYPE_NODE | SC_TYPE_NODE_LINK | SC_TYPE_NODE_CLASS

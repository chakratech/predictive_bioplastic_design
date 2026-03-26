"""
chemistry.py

Shared chemistry utilities for the bioplastic screening pipeline.
Provides SMILES parsing helpers and molecular property checks using RDKit.
"""

import re

from rdkit import Chem


def has_aromatic_atoms(smiles: str) -> bool:
    """Check whether a SMILES string contains any aromatic atoms.

    Parses the SMILES into an RDKit molecule object and queries each
    atom's aromaticity flag directly. This is more reliable than
    string pattern matching, which can miss aromatics hidden inside
    complex branch notation.

    Args:
        smiles: A SMILES string, e.g. '[*]OC(c1ccccc1)CCC(=O)[*]'

    Returns:
        True if any atom in the molecule is aromatic, False otherwise.
        Returns False if RDKit cannot parse the SMILES.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    return any(atom.GetIsAromatic() for atom in mol.GetAtoms())


def parse_smiles_field(val) -> list[str]:
    """Extract individual SMILES strings from a smiles field.

    Handles two storage formats:
      - Python list/tuple (from parquet): ('smi1', 'smi2')
      - Stringified array (from CSV):    "['smi1' 'smi2']"

    Args:
        val: Either a Python list/tuple of SMILES strings, or a string
             representation of one.

    Returns:
        A list of SMILES strings.
    """
    if isinstance(val, (list, tuple)):
        return list(val)
    return re.findall(r"'([^']+)'", str(val))


def parse_names_field(val) -> list[str]:
    """Extract individual monomer names from a names field.

    Handles two storage formats:
      - Python list/tuple (from parquet): ('pha', 'PS')
      - Stringified array (from CSV):    "['pha' 'PS']"

    Args:
        val: Either a Python list/tuple of name strings, or a string
             representation of one.

    Returns:
        A list of name strings.
    """
    if isinstance(val, (list, tuple)):
        return list(val)
    return re.findall(r"'([^']+)'", str(val))


def pha_monomers_have_aromatic(smiles_field, names_field) -> bool:
    """Check whether any PHA monomer in a candidate contains aromatic atoms.

    Examines only monomers named 'pha'. Conventional plastic monomers
    (e.g. 'PS', 'PET') are ignored — the filter targets the bio-based
    component only.

    Args:
        smiles_field: The smiles column value (list/tuple or stringified).
        names_field:  The names column value (list/tuple or stringified).

    Returns:
        True if any PHA monomer contains aromatic atoms.
    """
    monomers = parse_smiles_field(smiles_field)
    names = parse_names_field(names_field)

    for name, smi in zip(names, monomers):
        if name == "pha" and has_aromatic_atoms(smi):
            return True
    return False

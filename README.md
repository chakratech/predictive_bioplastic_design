# Predictive Bioplastic Design

**A polymer screening pipeline for identifying PHA-based bioplastic replacements for commodity and specialty plastics.**

Built on the multitask deep neural network framework from [Kuenneth et al. (2022)](https://doi.org/10.1038/s43246-022-00319-2), with planned extensions for additional target plastics, blend candidates, and visualization tools for industrial bioplastic design at [ChakraTech](https://github.com/chakratech).

> **Status:** Active development — building toward a custom screening pipeline for PHA-based materials.

---

## Background

Polyhydroxyalkanoates (PHAs) are bio-synthesized, biodegradable polymers with the potential to replace petroleum-based plastics. The original work by Kuenneth et al. developed multitask deep neural network property predictors trained on ~23,000 experimental data points to forecast 13 polymer properties (thermal, mechanical, gas permeability) across a search space of ~1.4 million PHA-based bioplastic candidates.

This fork extends that work with a focus on practical PHA screening for industrial applications.

## Goals (Planned Extensions)

- **Expand target plastics** — Add PLA and other commercially relevant polymers to the replacement target list (original covers PE, PP, PVC, PET, PS, Nylon 6, PEN)
- **Additional blend candidates** — Add starch as a copolymer/blend partner alongside the original 13 conventional polymers
- **Property visualization** — Build radar charts and comparison plots for predicted vs. target properties
- **Industrial focus** — Tailor screening criteria to real-world PHA production constraints

## Related Work

This project is part of a collaborative effort at ChakraTech. See also:
- [chakratech/bioplastic_design](https://github.com/chakratech/bioplastic_design) (Farah's fork — further along)

## Original Repository

Forked from [Ramprasad-Group/bioplastic_design](https://github.com/Ramprasad-Group/bioplastic_design).

**Citation:**
> Kuenneth, C., Lalonde, J., Marrone, B.L., Iverson, C.N., Ramprasad, R., & Pilania, G. (2022). Bioplastic design using multitask deep neural networks. *Communications Materials*, 3, 96. https://doi.org/10.1038/s43246-022-00319-2

## Install

```bash
git clone https://github.com/chakratech/predictive_bioplastic_design.git
cd predictive_bioplastic_design
poetry install
```

## Project Structure

```
predictive_bioplastic_design/
├── bioplastic_design/
│   ├── search_space.ipynb          # Create polymer search space
│   ├── screening.ipynb             # Screen for replacement candidates
│   ├── candidates.txt              # 70 bioplastic candidates (original 7 plastics)
│   └── predictions_01_11_2022.parquet  # ~1.4M candidates with predictions
├── README.md
└── pyproject.toml
```

## Roadmap

- [ ] Visualization: radar charts comparing predicted properties vs. target plastics
- [ ] Visualization: property distribution plots for the candidate search space
- [ ] Add PLA to target plastic list (Tg ~60°C, Tm ~150-180°C, E ~2000-3500 MPa)
- [ ] Add starch as a blend/copolymer candidate
- [ ] Add other common polymers as replacement targets (e.g., PBAT, PCL)
- [ ] Refine screening criteria for ChakraTech's production capabilities
- [ ] Integrate with polyBERT embeddings for enhanced polymer representation
- [ ] Build combined screening pipeline (Kuenneth predictors + polyBERT)

## How to Use

### Existing Notebooks

**[search_space.ipynb](bioplastic_design/search_space.ipynb)** — Creates the polymer search space by combining 540 PHAs with conventional polymers at varying compositions. Predictors are not included (available via [PolymerGenome](https://polymergenome.org)).

**[screening.ipynb](bioplastic_design/screening.ipynb)** — Screens the candidate space for polymers matching specific property targets using nearest-neighbor search.

### Data

Load the full prediction dataset:
```python
import pandas as pd
df = pd.read_parquet('bioplastic_design/predictions_01_11_2022.parquet')
```

## License

The original code and data are available for **academic non-commercial use only** (see original repository). Extensions in this fork follow the same terms unless otherwise noted.
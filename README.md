# Predictive Bioplastic Design

**A polymer screening pipeline for identifying PHA-based bioplastic replacements for commodity and specialty plastics.**

Built on the multitask deep neural network framework from [Kuenneth et al. (2022)](https://doi.org/10.1038/s43246-022-00319-2), with planned extensions for additional target plastics, blend candidates, and visualization tools for industrial bioplastic design at [ChakraTech](https://github.com/chakratech).

> **Status:** Active development — building toward a custom screening pipeline for PHA-based materials.

---

## Background

Polyhydroxyalkanoates (PHAs) are bio-synthesized, biodegradable polymers with the potential to replace petroleum-based plastics. The original work by Kuenneth et al. developed multitask deep neural network property predictors trained on ~23,000 experimental data points to forecast 13 polymer properties (thermal, mechanical, gas permeability) across a search space of ~1.4 million PHA-based bioplastic candidates.

This project builds on that framework with a focus on practical PHA screening for industrial applications.

### What's included and what's not

The original authors provided the code to construct the search space and screen candidates, along with pre-computed property predictions for all ~1.4 million candidates. However, the trained ML models and fingerprinting code used to generate those predictions are not included — the `predict()` function in `search_space.ipynb` is an empty placeholder. The models are proprietary and deployed via [PolymerGenome.org](https://polymergenome.org).

This means **screening.ipynb works fully** using the pre-computed predictions, but **search_space.ipynb cannot generate new predictions** without an external property predictor. Building or integrating our own prediction capability (via [polyBERT](https://huggingface.co/kuelumbus/polyBERT) or custom models) is a long-term goal of this project.

## Goals

- **Expand target plastics** — Add PLA and other commercially relevant polymers to the replacement target list (original covers PE, PP, PVC, PET, PS, Nylon 6, PEN)
- **Additional blend candidates** — Add starch as a copolymer/blend partner alongside the original 13 conventional polymers
- **Property visualization** — Build radar charts and comparison plots for predicted vs. target properties
- **Industrial focus** — Tailor screening criteria to real-world PHA production constraints
- **polyBERT integration** — Incorporate transformer-based polymer fingerprinting ([Kuenneth & Ramprasad, 2023](https://doi.org/10.1038/s41467-023-39868-6)) for enhanced polymer representation and faster screening

## Setup

> **Note:** The original `poetry install` may fail on Apple Silicon Macs due to pinned
> dependencies. Use the conda setup below instead.

```bash
git clone https://github.com/chakratech/predictive_bioplastic_design.git
cd predictive_bioplastic_design

conda create -n bioplastic_design python=3.9 -y
conda activate bioplastic_design

pip install -r requirements.txt
conda install -c conda-forge rdkit -y

python -m ipykernel install --user --name bioplastic_design --display-name "Python (bioplastic_design)"
```

RDKit is installed via conda separately because it has C++ dependencies that pip can't handle reliably.

## How to Use

### Screening for Replacement Candidates

**[screening.ipynb](bioplastic_design/screening.ipynb)** is the main notebook. It loads pre-computed property predictions for ~1.4 million bioplastic candidates and finds the closest matches to target commodity plastics using nearest-neighbor search on 7 key properties: glass transition temperature (Tg), melting temperature (Tm), Young's modulus (E), tensile strength at break (σb), elongation at break (εb), O₂ permeability, and CO₂ permeability.

```python
import pandas as pd
df = pd.read_parquet('bioplastic_design/predictions_01_11_2022.parquet')
```

### Understanding the Search Space

**[search_space.ipynb](bioplastic_design/search_space.ipynb)** shows how the candidate space is constructed: 540 PHA monomers (varying backbone length, side-chain length, and end group) are combined into copolymers at 11 compositions (0%, 10%, ..., 100%) with each other and with 13 conventional polymers. The `predict()` function in this notebook is a placeholder — see [What's included and what's not](#whats-included-and-whats-not) above.

## Roadmap

- [ ] Add PLA to target plastic list
- [ ] Add starch as a blend/copolymer candidate
- [ ] Radar charts comparing predicted properties vs. target plastics
- [ ] Property distribution plots for the candidate search space
- [ ] Add other biodegradable targets (PBAT, PCL)
- [ ] Refine screening criteria for ChakraTech's production capabilities
- [ ] Integrate polyBERT fingerprinting for expanded candidate screening
- [ ] Train custom property predictors on experimental data

## Related Work

- [Ramprasad-Group/bioplastic_design](https://github.com/Ramprasad-Group/bioplastic_design) — Original repository
- [chakratech/bioplastic_design](https://github.com/chakratech/bioplastic_design) (Farah's fork)
- [polyBERT](https://huggingface.co/kuelumbus/polyBERT) — Transformer-based polymer fingerprinting model

## Citations

> Kuenneth, C., Lalonde, J., Marrone, B.L., Iverson, C.N., Ramprasad, R., & Pilania, G. (2022). Bioplastic design using multitask deep neural networks. *Communications Materials*, 3, 96. https://doi.org/10.1038/s43246-022-00319-2

> Kuenneth, C. & Ramprasad, R. (2023). polyBERT: a chemical language model to enable fully machine-driven ultrafast polymer informatics. *Nature Communications*, 14, 4099. https://doi.org/10.1038/s41467-023-39868-6

## License

The original code and data are available for **academic non-commercial use only** (see [original repository](https://github.com/Ramprasad-Group/bioplastic_design)). Extensions in this project follow the same terms unless otherwise noted.
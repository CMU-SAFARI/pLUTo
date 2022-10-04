<p align="center">
  <img alt="pluto-logo" src="resources/pluto_logo_rounded_corners.png" width="300">
  <h3 align="center">Enabling Massively Parallel Computation in DRAM via Lookup Tables</h3>
</p>

<p align="center">
    <a href="https://github.com/CMU-SAFARI/pLUTo/blob/master/LICENSE">
        <img alt="GitHub" src="https://img.shields.io/badge/License-MIT-yellow.svg">
    </a>
    <a href="https://github.com/CMU-SAFARI/pLUTo/releases">
        <img alt="GitHub Release" src="https://img.shields.io/github/release/CMU-SAFARI/pLUTo">
    </a>
  <br>
    <a href="https://doi.org/10.1109/MICRO56248.2022.00067"><img src="https://img.shields.io/badge/DOI-10.1109/MICRO56248.2022.00067-blue" alt="MICRO DOI"></a>
    <a href="https://doi.org/10.48550/arXiv.2104.07699"><img src="https://img.shields.io/badge/DOI-10.48550/arXiv.2104.07699-blue" alt="arXiv DOI"></a>
    <a href="https://doi.org/10.5281/zenodo.6942058"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6942058.svg" alt="Zenodo DOI"></a>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#what-is-pluto">What is pLUTo?</a></li>
    <li><a href="#repository-structure">Repository Structure</a></li>
    <li><a href="#execution-instructions">Execution Instructions</a></li>
    <li><a href="#citation">Citation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## What is pLUTo?

**pLUTo is a Processing-using-Memory architecture that enables the execution of complex operations in-memory.**
To achieve this, the key idea of pLUTo is to replace complex operations with low-cost, massively parallel table lookups that produce the same result.

The _pLUTo LUT Query_ operation is at the core of pLUTo's functionality: this operation enables every element in an input memory row to be used to query a LUT that may contain up to as many entries as the number of rows in a DRAM subarray.


## Citation

Please cite our full MICRO 2022 paper if you find this repository useful.

> _João Dinis Ferreira, Gabriel Falcao, Juan Gómez-Luna, Mohammed Alser, Lois Orosa, Mohammad Sadrosadati, Jeremie S. Kim, Geraldo F. Oliveira, Taha Shahroodi, Anant Nori, and Onur Mutlu. ["pLUTo: Enabling Massively Parallel Computation in DRAM via Lookup Tables".](https://arxiv.org/abs/2104.07699) In Proceedings of the 55th Annual IEEE/ACM International Symposium on Microarchitecture (MICRO), 2022. https://doi.org/10.1109/MICRO56248.2022.00067._

You can also use the following BibTeX entry for this purpose:

```bibtex
@inproceedings{ferreira2022pluto,
  author = {Ferreira, João Dinis and Falcao, Gabriel and Gómez-Luna, Juan and Alser, Mohammed and Orosa, Lois and Sadrosadati, Mohammad and Kim, Jeremie S. and Oliveira, Geraldo F. and Shahroodi, Taha and Nori, Anant and Mutlu, Onur},
  title = {{pLUTo: Enabling Massively Parallel Computation in DRAM via Lookup Tables}},
  doi = {10.1109/MICRO56248.2022.00067},
  booktitle = {Proceedings of the 55th Annual IEEE/ACM International Symposium on Microarchitecture (MICRO)},
  year = {2022}
}
```

## Repository Structure

This repository contains the artifact evaluation materials associated with [pLUTo: Enabling Massively Parallel Computation In DRAM via Lookup Tables](pLUTo.pdf), published at MICRO 2022.

We provide source code and helper files to reproduce:

1. SPICE simulations (shown in Figure 6 in the paper)
2. The simulation of pLUTo's operation (shown in Figures 7-13 in the paper)

We provide in-depth instructions on how to reproduce each of the artifacts in the `README.md` files in the `pluto_sim` and `spice` directories.

The following is a high-level overview of the structure of this repository. We highlight select folders and files of note.

```
.
+-- LICENSE
+-- README.md
+-- pluto_sim/
|   +-- baselines                   -->             baseline results for the evaluated workloads
|   +-- pysim                       -->             output folder (empty when the repository is first cloned)
|   +-- pysim_reference             -->             reference results for the pLUTo-based execution of the evaluated workloads
|   +-- LUT_Loading_Times.xlsx      -->             used to produce the results shown in Figure 11 in the paper
|   +-- README.md                   --> START HERE: step-by-step instructions on how to reproduce our results
|   +-- requirements.txt            -->             Python requirements to be installed prior to execution
|   +-- sim_walkthrough.ipynb       -->             interactive Python Jupyter Notebook with step-by-step instructions on how to reproduce our results
|   +-- ...
+-- resources/
|   +-- ...                         -->             media rendered in this README
+-- spice/
|   +-- media/                      -->             media rendered in the README
|   +-- out/                        -->             output folder
|   +-- runs/                       -->             output folder
|   +-- README.md                   --> START HERE: step-by-step instructions on how to reproduce our results
|   +-- pluto-a.asc                 -->             cell design file
|   +-- pluto-b.asc                 -->             cell design file
|   +-- pluto-c.asc                 -->             cell design file
|   +-- reference.asc               -->             cell design file
|   +-- transistor_model.pm         -->             transistor model
```

## Execution Instructions

For step-by-step instructions on how to reproduce our results, please see [the README in the `spice` folder](spice/README.md) and [the README in the `pluto_sim` folder](pluto_sim/README.md).

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact

[João Dinis Ferreira - hello@joaof.eu](mailto:hello@joaof.eu?subject=A%20Question%20About%20pLUTo)

## Acknowledgements

We acknowledge support from SAFARI Research Group's industrial partners.

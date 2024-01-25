# Tracking pulsar phases using a Kalman filter


[![codecov](https://codecov.io/gh/tomkimpson/KalmanPhasePTA/graph/badge.svg?token=Y2TSEX32BI)](https://codecov.io/gh/tomkimpson/KalmanPhasePTA)


[![Build Status](https://github.com/tomkimpson/StateSpacePTA/actions/workflows/run_test.yml/badge.svg?branch=main)](https://github.com/tomkimpson/StateSpacePTA/actions/workflows/run_test.yml?query=branch%3Amain)


This repo is a research project aimed at tracking pulsar phases using a Kalman filter.

It is a phase-domain analogue of the work in https://github.com/tomkimpson/StateSpacePTA.



---


### Getting started

The structure is as follows:

* `data`: small (<100 Mb) data files  
* `docs`: paper manuscript and collected notes. 
* `notebooks`: collected jupyter notebooks for demos and exploration
* `src`: the actual code
* `test`: all unit tests

The relevant packages can be installed using [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) and the `env.yml` in the root directory.

The main script for running the complete pipeline is `src/main.py` which accepts a config `ini` file as an command line argument input, e.g. `python main.py config_file.ini`
The config files are generated by `src/configs/create_init_file.py`. A copy of the input `.ini` file is saved along with the `.json` result output by bilby.

We typically run via a slurm queue. The workflow from `src/` is as follows:

* `python configs/create_ini_file.py` 
* `python configs/create_slurm_job.py configs/example.ini` 
* `sbatch slurm.sh`



---
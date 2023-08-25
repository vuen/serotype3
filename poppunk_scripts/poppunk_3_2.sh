#!/bin/bash
#$ -S /bin/sh
#$ -N poppunk_3
#$ -q researchsmall.q
#$ -pe multithread 8
#$ -o popunk_3.o
#$ -e popunk_3.e
##$ -l walltime=72:00:00
. /etc/profile.d/modules.sh


#loading the needed modules

#module purge
#module load anaconda/5.3.1_python3
#python3 -m pip install poppunk
#conda activate poppunk_env 

#script for running poppunk

#Creating a database

poppunk --create-db --r-files input/phengs/hpc_projects/rvpbru/serotype_3_clades/assemblies/assembly_file.txt \
--output phengs/hpc_storage/home/vuyelwa.nkomo/project_results/poppunk_results --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --plot-fit 5 --length-range 1900000 2500000

# To fit to a Bayesian gaussian mixture model

poppunk --fit-model bgmm --distances 3_refine/3_refine.dists --output 3_refine --ref-db 3_refine --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5 

# To optimise the network score from a model already fitted by bgmm

poppunk --fit-model refine --distances 3_refine/3_refine.dists --output 3_refine --ref-db 3_refine --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5

# To fit to a Bayesian gaussian mixture model

poppunk --fit-model bgmm --distances 3_refine/3_refine.dists --output 3_refine --ref-db 3_refine --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5

# To optimise the network score from a model already fitted by bgmm

poppunk --fit-model refine --distances 3_refine/3_refine.dists --output 3_refine --ref-db 3_refine --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5

# To visulise the poppunk clustering results for the use of microreact

poppunk --generate-viz --ref-db 3_refine --output 3_refine --microreact

 


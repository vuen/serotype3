#!/bin/bash
#$ -S /bin/sh
#$ -N quast
#$ -q researchsmall.q
#$ -pe multithread 4
. /etc/profile.d/modules.sh
module purge
module load anaconda/5.3.1_python3
source activate quast/4.0

quast /phengs/hpc_storage/home/vuyelwa.nkomo/.conda/envs/quast/bin/quast -o /phengs/hpc_storage/home/vuyelwa.nkomo/project_results/quast_results1/ 
/phengs/hpc_projects/rvpbru/serotype_3_clades/assemblies/${1}*_contigs.fasta


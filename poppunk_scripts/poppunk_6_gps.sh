
#!/bin/bash
#$ -S /bin/sh
#$ -N poppunk_3
#$ -q researchsmall.q
#$ -pe multithread 8
#$ -o popunk_3.o
#$ -e popunk_3.e
##$ -l walltime=72:00:00
#. /etc/profile.d/modules.sh

#03.08.23
#Vuyelwa Nkomo
#v6 with  GPS assignment

#loading the needed modules

#module purge
#module load anaconda/5.3.1_python3
#python3 -m pip install poppunk
#conda activate poppunk_env

#script for running poppunk

#Creating a database
#no length range

#poppunk --create-db --r-files ~/serotype3_sequences/serotype_3_clades/assemblies/reference_list.txt \
#--output ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc --threads 8 \
#--overwrite --min-k 15 --max-k 29 --k-step 3 --plot-fit 5 --length-range 1900000 2500000 

# To fit to a Bayesian gaussian mixture model
#deleted the bgmm

#poppunk --fit-model bgmm --distances ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc/ppunk_results_with_qc.dists \
#--output ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc --ref-db ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc --threads 8 \
#--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5#!/usr/bin/env python


# To visulise the poppunk clustering results for the use of microreact

#poppunk --generate-viz --ref-db ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc \
#--output ~/vuyelwa.nkomo/project_results/ppunk_results --microreact

#poppunk_visualise --ref-db ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc \
#--output ~/vuyelwa.nkomo/project_results/ppunk_results_with_qc --microreact --threads 8

#gpsc assignment
#poppunk_assign --~/serotype3_sequences/serotype_3_clades/gps/db GPS_v6 --distances ~/serotype3_sequences/serotype_3_clades/gps/GPS_v6/GPS_v6.dists \
#--query </serotype3_sequences/serotype_3_clades/assemblies/reference_list.txt> --output <~/vuyelwa.nkomo/project_results/GPSC_assignment> \
#--external-clustering GPS_v6_external_clusters.csv

#gpsc
poppunk_assign --~/serotype3_sequences/serotype_3_clades/gps/db GPS_v6 --distances \
~/serotype3_sequences/serotype_3_clades/gps/GPS_v6/GPS_v6.dists \
--query <~/vuyelwa.nkomo/path_to_scripts/refine_new_reference_list.txt> \
--output <~/vuyelwa.nkomo/project_results/gpsc_assignment> \
--external-clustering GPS_v6_external_clusters.csv

# To visulise the poppunk clustering results for the use of microreact

#poppunk --generate-viz --ref-db ~/vuyelwa.nkomo/project_results/popunk_results_qc2 \
#--output ~/vuyelwa.nkomo/project_results/popunk_results_qc2 --microreact

poppunk_visualise --ref-db ~/vuyelwa.nkomo/project_results/ppunk_results_gps \
--output ~/vuyelwa.nkomo/project_results/ppunk_results_gps --microreact --threads 8

#visualise with gpsc assignment
poppunk_visualise --ref-db ~/serotype3_sequences/serotype_3_clades/gps/db \
--output ~/vuyelwa.nkomo/project_results/GPSC_assignment --microreact --threads 8


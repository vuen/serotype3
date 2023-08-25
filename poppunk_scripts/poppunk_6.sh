
#!/bin/bash
#$ -S /bin/sh
#$ -N poppunk_3
#$ -q researchsmall.q
#$ -pe multithread 8
#$ -o popunk_3.o
#$ -e popunk_3.e
##$ -l walltime=72:00:00
#. /etc/profile.d/modules.sh


#script for running poppunk

#Creating a database

poppunk --create-db --r-files ~/vuyelwa.nkomo/path_to_scripts/refine_new_reference_list.txt \
--output ~/vuyelwa.nkomo/project_results/ppunk_results_gps --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --plot-fit 5 --length-range 1900000 2500000

# To fit to a Bayesian gaussian mixture model
#deleted the bgmm

poppunk --fit-model bgmm --distances ~/vuyelwa.nkomo/project_results/ppunk_results_gps/ppunk_results_gps.dists \
--output ~/vuyelwa.nkomo/project_results/ppunk_results_gps --ref-db ~/vuyelwa.nkomo/project_results/ppunk_results_gps --threads 8 \
--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5


#asign query qc
#need query db
#poppunk --qc-db --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_qc2 \
#--length-range 1900000 2500000 --output ~/vuyelwa.nkomo/project_results/poppunk_results_qc2

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

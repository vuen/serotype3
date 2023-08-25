
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

#poppunk --create-db --r-files ~/vuyelwa.nkomo/path_to_scripts/refine_new_reference_list_no_MOLIS.txt \
#--output ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 --threads 8 \
#--overwrite --min-k 15 --max-k 29 --k-step 3 --plot-fit 5 --length-range 1900000 2500000

#need query db
#poppunk --qc-db --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 \
#--length-range 1900000 2500000 --max-zero-dist 1 --output ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2


# To fit to a Bayesian gaussian mixture model
#deleted the bgmm

#poppunk --fit-model bgmm --distances ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2/poppunk_results_gps_2.dists \
#--output ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 --threads 8 \
#--overwrite --min-k 15 --max-k 29 --k-step 3 --K 5


#asign query qc
#need query db
#poppunk --qc-db --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_qc2 \
#--length-range 1900000 2500000 --max-zero-dist 1 --output ~/vuyelwa.nkomo/project_results/poppunk_results_qc2

#gpsc
#poppunk_assign --db ~/serotype3_sequences/serotype_3_clades/gps/GPS_v6 --distances \
#~/serotype3_sequences/serotype_3_clades/gps/GPS_v6/GPS_v6.dists \
#--query ~/vuyelwa.nkomo/path_to_scripts/refine_new_reference_list_no_MOLIS.txt \
#--output ~/vuyelwa.nkomo/project_results/gpsc_assignment --external-clustering ~/serotype3_sequences/serotype_3_clades/gps/GPS_v6_external_clusters.csv --threads 8

# To visulise the poppunk clustering results for the use of microreact

rm ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2/poppunk_results_gps_2_core_NJ.nwk


#poppunk --generate-viz --ref-db ~/vuyelwa.nkomo/project_results/popunk_results_qc2 \
#--output ~/vuyelwa.nkomo/project_results/popunk_results_qc2 --microreact

poppunk_visualise --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 \
--output ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 --microreact --threads 8

poppunk_visualise --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 \
--output ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 --phandango --threads 8

poppunk_visualise --ref-db ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 \
--cytoscape --network-file ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2/poppunk_results_gps_2.refs_graph.gt \
--output ~/vuyelwa.nkomo/project_results/poppunk_results_gps_2 --phandango --threads 8


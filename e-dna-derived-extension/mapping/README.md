# A DwC DNA-derived data extension to MIxS mapping

## Project and Task Overview
This work is part of the eDNAqua-Plan project, a Horizon-funded initiative aimed at promoting synergies, harmonization, and interoperability between existing EU initiatives and resources linked to environmental DNA (eDNA) data from marine and freshwater ecosystems. The consortium's overarching goal is to provide a framework for maximizing the efficiency of future aquatic biodiversity monitoring activities by improving data generation, storage, analysis, and accessibility.

Specifically, this effort falls under Task 3.2: Standards for eDNA Data Repositories (Lead: BIOPOLIS-CIBIO; Contributors: SYKE, UNESCO, EMBL-EBI), which focuses on improving interoperability by modeling alignments between community (meta)data standards for eDNA across the entire aquatic biodiversity biomonitoring workflow.

## Mapping Effort
This folder contains the results of an extensive mapping exercise between the [DwC's DNA-derived data extension](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-04-17.xml) and [MIxS (Minimum Information about any (x) Sequence)](https://genomicsstandardsconsortium.github.io/mixs/) standards.

## Methodology
The mapping utilizes two complementary frameworks:

- Simple Standard for Sharing Ontology Mappings (SSSOM): Provides a standardized approach for representing and sharing ontology mappings
- Simple Knowledge Organization System (SKOS): Used to qualify and contextualize the mappings through semantic relationships

This approach ensures that the mappings are both machine-readable and semantically rich, facilitating automated processing and human interpretation.

## Folder Contents
This folder contains three mapping files in tab-separated value formats:
Content of this Folder
This folder contains three comprehensive mapping files in tab-separated value format:
- **e-dna-derived-extension_mappingSemantic.tsv** which contains semantic mappings between DwC DNA-derived data extension and MIxS terms.
- **e-dna-derived-extension_mappingSyntactic.tsv** which documents syntactic mappings and structural alignments. It features syntactic mapping predicate [ext_syntax_predicate_id] and accompanying syntactic comments [ext_syntax_comment].
- **e-dna-derived-extension_mappingSupport.tsv**, in preparation.


## Terms included in the mapping

- DNA-derived Extension Terms (99 terms):
samp_name, occurrenceID, project_name, experimental_factor, samp_taxon_id, neg_cont_type, pos_cont_type, env_broad_scale, env_local_scale, env_medium, subspecf_gen_lin, ploidy, num_replicons, extrachrom_elements, estimated_size, ref_biomaterial, source_mat_id, pathogenicity, biotic_relationship, specific_host, host_spec_range, host_disease_stat, trophic_level, propagation, encoded_traits, rel_to_oxygen, isol_growth_condt, samp_collec_device, samp_collec_method, samp_mat_process, size_frac, samp_size, samp_vol_we_dna_ext, source_uvig, virus_enrich_appr, nucl_acid_ext, nucl_acid_amp, lib_size, lib_reads_seqd, lib_layout, lib_vector, lib_screen, target_gene, target_subfragment, pcr_primers, mid, adapters, pcr_cond, seq_meth, seq_quality_check, chimera_check, tax_ident, assembly_qual, assembly_name, assembly_software, annot, number_contig, feat_pred, ref_db, sim_search_meth, tax_class, 16s_recover, 16s_recover_software, trnas, trna_ext_software, compl_score, compl_software, compl_appr, contam_score, contam_screen_input, contam_screen_param, decontam_software, sort_tech, single_cell_lysis_appr, single_cell_lysis_prot, wga_amp_appr, wga_amp_kit, bin_param, bin_software, reassembly_bin, mag_cov_software, vir_ident_software, pred_genome_type, pred_genome_struc, detec_type, otu_class_appr, otu_seq_comp_appr, otu_db, host_pred_appr, host_pred_est_acc, url, sop, pcr_primer_forward, pcr_primer_reverse, concentration, concentrationUnit, methodDeterminationConcentrationAndRatios, ratioOfAbsorbance260_230, ratioOfAbsorbance260_280
- MIxS's Terms (91 terms): MIxS Terms: MIXS:0001107, MIXS:0000092, MIXS:0000008, MIXS:0001320, MIXS:0001321, MIXS:0001322, MIXS:0000012, MIXS:0000013, MIXS:0000014, MIXS:0000020, MIXS:0000021, MIXS:0000022, MIXS:0000023, MIXS:0000024, MIXS:0000025, MIXS:0000026, MIXS:0000027, MIXS:0000028, MIXS:0000029, MIXS:0000030, MIXS:0000031, MIXS:0000032, MIXS:0000033, MIXS:0000034, MIXS:0000015, MIXS:0000003, MIXS:0000002, MIXS:0001225, MIXS:0000016, MIXS:0000017, MIXS:0000001, MIXS:0000111, MIXS:0000035, MIXS:0000036, MIXS:0000037, MIXS:0000038, MIXS:0000039, MIXS:0000040 ,MIXS:0000041, MIXS:0000042, MIXS:0000043, MIXS:0000044, MIXS:0000045, MIXS:0000046, MIXS:0000047, MIXS:0000048, MIXS:0000049, MIXS:0000050, MIXS:0000051, MIXS:0000052, MIXS:0000053, MIXS:0000056, MIXS:0000057, MIXS:0000058, MIXS:0000059, MIXS:0000060, MIXS:0000061, MIXS:0000062, MIXS:0000063, MIXS:0000064, MIXS:0000065, MIXS:0000066, MIXS:0000067, MIXS:0000068, MIXS:0000069, MIXS:0000070, MIXS:0000071, MIXS:0000072, MIXS:0000005, MIXS:0000073, MIXS:0000074, MIXS:0000075, MIXS:0000076, MIXS:0000054, MIXS:0000055, MIXS:0000006, MIXS:0000077, MIXS:0000078, MIXS:0000079, MIXS:0000080, MIXS:0000081, MIXS:0000082, MIXS:0000083, MIXS:0000084, MIXS:0000085, MIXS:0000086, MIXS:0000087, MIXS:0000088, MIXS:0000089, MIXS:0000091, MIXS:0000090, MIXS:0000046, MIXS:0000046.
- GGBN Terms (5 terms): Concentration (DNA), Unit of Concentration (DNA), Method used for Determination of Concentration and Ratios of Absorbance (DNA), Ratio of Absorbance 260/230 (DNA), Ratio of Absorbance 260/280 (DNA)

## Unmapped Terms
- Newly Introduced Terms (4 terms): The following terms were newly introduced in the DNA-derived data extension and currently lack mappings to existing standards (PCR Primer Name Forward, PCR Primer Name Reverse, PCR Primer Reference, DNA Sequence).
- MIQE-based Terms (19 terms): These terms are based on MIQE (Minimum Information for Publication of Quantitative Real-Time PCR Experiments, https://rdml.org/miqe.html) guidelines. Their provenance has been difficult to infer for mapping purposes (annealingTemp, annealingTempUnit, probeReporter, probeQuencher, ampliconSize, thresholdQuantificationCycle, baselineValue, quantificationCycle, automaticThresholdQuantificationCycle, automaticBaselineValue, contaminationAssessment, partitionVolume, partitionVolumeUnit, estimatedNumberOfCopies, amplificationReactionVolume, amplificationReactionVolumeUnit, pcr_analysis_software, experimentalVariance, pcr_primer_lod, pcr_primer_loq).

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

## Unmapped Terms

Unmapped terms are detailed here and included in the mapping file; however, they have no associated predicate identifier.

### Semantically Unmapped Terms

- Newly Introduced Terms (4 terms): The following terms were newly introduced in the DNA-derived data extension and currently lack mappings to existing standards (`pcr_primer_name_forward`, `pcr_primer_name_teverse`, `pcr_primer_reference`, `DNA_sequence`).

- MIQE-based Terms (20 terms): These terms are based on MIQE (Minimum Information for Publication of Quantitative Real-Time PCR Experiments, https://rdml.org/miqe.html) guidelines. Their provenance has been difficult to infer for mapping purposes (`annealingTemp`, `annealingTempUnit`, `probeReporter`, `probeQuencher`, `ampliconSize`, `thresholdQuantificationCycle`, `baselineValue`, `quantificationCycle`, `automaticThresholdQuantificationCycle`, `automaticBaselineValue`, `contaminationAssessment`, `partitionVolume`, `partitionVolumeUnit`, `estimatedNumberOfCopies`, `amplificationReactionVolume`, `amplificationReactionVolumeUnit`, `pcr_analysis_software`, `experimentalVariance`, `pcr_primer_lod`, `pcr_primer_loq`).


### Syntactically Unmapped Terms

### Syntactically Unmapped Terms

- All terms that remain semantically unmapped (i.e. the previously described Newly Introduced Terms [4] and MIQE-based Terms [20]).
- Additional terms were left syntactically unmapped due to misaligned or ambiguous specifications:
  `samp_collec_device`, `samp_collec_method`, `virus_enrich_appr`, `seq_quality_check`, `tax_ident`, `compl_appr`, `decontam_software`, `bin_param`, `bin_software`.
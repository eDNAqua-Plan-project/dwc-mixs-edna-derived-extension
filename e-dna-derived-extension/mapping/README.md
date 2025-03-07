# A DwC DNA derived data to MIxS mapping

The content of this folder is the result of an extensive mapping in the direction of [DwC DNA derived data](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-04-17.xml) to MIxS using Simple Standard for Sharing Ontology Mappings ([SSSOM](https://github.com/mapping-commons/SSSOM)) in combination with the Simple Knowledge Organization System ([SKOS](https://www.w3.org/TR/skos-reference/)) ontology to qualify the mapping.

## Content of this folder
This folder contains three mapping files in tab-separated value files:
* e-dna-derived-extension_mappingSemantic.tsv
   * includes relevant [SSSOM metadata elements](https://github.com/mapping-commons/SSSOM/blob/master/SSSOM.md#sssom-metadata-elements).
* e-dna-derived-extension_mappingSyntactic.tsv
   * includes relevant [SSSOM metadata elements](https://github.com/mapping-commons/SSSOM/blob/master/SSSOM.md#sssom-metadata-elements), however notes the syntactic mapping predicate [`syntax_predicate_id`] and accompanying comments[`syntax_comment`] instead of the semantic predicate.
* e-dna-derived-extension_mappingSupport.tsv
   * includes relevant [SSSOM metadata elements](https://github.com/mapping-commons/SSSOM/blob/master/SSSOM.md#sssom-metadata-elements), syntactic mapping predicates and accompanying comments, as well as additional metadata on the mapped terms (definitions [`subject_definition`, `object_definition`], syntax requirements [`subject_valueSyntax`, `object_valueSyntax`]).


## Terms included in the mapping

DwC terms included in this mapping
- Verbatim Coordinates


MIxS terms included in this mapping
- `z`

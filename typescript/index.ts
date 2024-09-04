// Code generated by jtd-codegen for TypeScript v0.2.1

export type Senzingapi = any;

export interface AddDataSource {
  DSRC_ID: number;
}

export interface AffectedEntity {
  /**
   * The ENTITY_ID is the Senzing-generated identifier for the discovered
   * entity. It may change when new information is added.
   */
  ENTITY_ID: number;
}

export interface CfgAttr {
  ADVANCED: string;
  ATTR_CLASS: string;
  ATTR_CODE: string;
  ATTR_ID: number;
  DEFAULT_VALUE: string;
  FELEM_CODE: string;
  FELEM_REQ: string;
  FTYPE_CODE: string;
  INTERNAL: string;
}

export interface CfgCfbom {
  CFCALL_ID: number;
  EXEC_ORDER: number;
  FELEM_ID: number;
  FTYPE_ID: number;
}

export interface CfgCfcall {
  CFCALL_ID: number;
  CFUNC_ID: number;
  EXEC_ORDER: number;
  FTYPE_ID: number;
}

export interface CfgCfrtn {
  CFRTN_ID: number;
  CFUNC_ID: number;
  CFUNC_RTNVAL: string;
  CLOSE_SCORE: number;
  EXEC_ORDER: number;
  FTYPE_ID: number;
  LIKELY_SCORE: number;
  PLAUSIBLE_SCORE: number;
  SAME_SCORE: number;
  UN_LIKELY_SCORE: number;
}

export interface CfgCfunc {
  ANON_SUPPORT: string;
  CFUNC_CODE: string;
  CFUNC_DESC: string;
  CFUNC_ID: number;
  CONNECT_STR: string;
  FUNC_LIB: string;
  FUNC_VER: string;
  JAVA_CLASS_NAME: string;
  LANGUAGE: string;
}

export interface CfgDfbom {
  DFCALL_ID: number;
  EXEC_ORDER: number;
  FELEM_ID: number;
  FTYPE_ID: number;
}

export interface CfgDfcall {
  DFCALL_ID: number;
  DFUNC_ID: number;
  EXEC_ORDER: number;
  FTYPE_ID: number;
}

export interface CfgDfunc {
  ANON_SUPPORT: string;
  CONNECT_STR: string;
  DFUNC_CODE: string;
  DFUNC_DESC: string;
  DFUNC_ID: number;
  FUNC_LIB: string;
  FUNC_VER: string;
  JAVA_CLASS_NAME: string;
  LANGUAGE: string;
}

export interface CfgDsrc {
  CONVERSATIONAL: string;
  DSRC_CODE: string;
  DSRC_DESC: string;
  DSRC_ID: number;
  DSRC_RELY: number;
  RETENTION_LEVEL: string;
}

export interface CfgDsrcInterest {
  DSRC_ID: number;
  INTEREST_FLAG: string;
  MAX_DEGREE: number;
}

export interface CfgEbom {
  ETYPE_ID: number;
  EXEC_ORDER: number;
  FTYPE_ID: number;
  UTYPE_CODE: string;
}

export interface CfgEclass {
  ECLASS_CODE: string;
  ECLASS_DESC: string;
  ECLASS_ID: number;
  RESOLVE: string;
}

export interface CfgEfbom {
  EFCALL_ID: number;
  EXEC_ORDER: number;
  FELEM_ID: number;
  FELEM_REQ: string;
  FTYPE_ID: number;
}

export interface CfgEfcall {
  EFCALL_ID: number;
  EFEAT_FTYPE_ID: number;
  EFUNC_ID: number;
  EXEC_ORDER: number;
  FELEM_ID: number;
  FTYPE_ID: number;
  IS_VIRTUAL: string;
}

export interface CfgEfunc {
  CONNECT_STR: string;
  EFUNC_CODE: string;
  EFUNC_DESC: string;
  EFUNC_ID: number;
  FUNC_LIB: string;
  FUNC_VER: string;
  JAVA_CLASS_NAME: string;
  LANGUAGE: string;
}

export interface CfgErfrag {
  ERFRAG_CODE: string;
  ERFRAG_DEPENDS: string;
  ERFRAG_DESC: string;
  ERFRAG_ID: number;
  ERFRAG_SOURCE: string;
}

export interface CfgErrule {
  DISQ_ERFRAG_CODE: string;
  ERRULE_CODE: string;
  ERRULE_DESC: string;
  ERRULE_ID: number;
  ERRULE_TIER: number;
  QUAL_ERFRAG_CODE: string;
  REF_SCORE: number;
  RELATE: string;
  RESOLVE: string;
  RTYPE_ID: number;
}

export interface CfgEtype {
  ECLASS_ID: number;
  ETYPE_CODE: string;
  ETYPE_DESC: string;
  ETYPE_ID: number;
}

export interface CfgFbom {
  DERIVED: string;
  DISPLAY_DELIM: string;
  DISPLAY_LEVEL: number;
  EXEC_ORDER: number;
  FELEM_ID: number;
  FTYPE_ID: number;
}

export interface CfgFbovr {
  ECLASS_ID: number;
  FTYPE_EXCL: string;
  FTYPE_FREQ: string;
  FTYPE_ID: number;
  FTYPE_STAB: string;
  UTYPE_CODE: string;
}

export interface CfgFclass {
  FCLASS_CODE: string;
  FCLASS_DESC: string;
  FCLASS_ID: number;
}

export interface CfgFelem {
  DATA_TYPE: string;
  FELEM_CODE: string;
  FELEM_DESC: string;
  FELEM_ID: number;
  TOKENIZE: string;
}

export interface CfgFtype {
  ANONYMIZE: string;
  DERIVATION: string;
  DERIVED: string;
  FCLASS_ID: number;
  FTYPE_CODE: string;
  FTYPE_DESC: string;
  FTYPE_EXCL: string;
  FTYPE_FREQ: string;
  FTYPE_ID: number;
  FTYPE_STAB: string;
  PERSIST_HISTORY: string;
  RTYPE_ID: number;
  SHOW_IN_MATCH_KEY: string;
  USED_FOR_CAND: string;
  VERSION: number;
}

export interface CfgGenericThreshold {
  BEHAVIOR: string;
  CANDIDATE_CAP: number;
  FTYPE_ID: number;
  GPLAN_ID: number;
  SCORING_CAP: number;
  SEND_TO_REDO: string;
}

export interface CfgGplan {
  GPLAN_CODE: string;
  GPLAN_DESC: string;
  GPLAN_ID: number;
}

export interface CfgLens {
  LENS_CODE: string;
  LENS_DESC: string;
  LENS_ID: number;
}

export type CfgLensrl = FixmeUnknown[];

export interface CfgRclass {
  IS_DISCLOSED: string;
  RCLASS_CODE: string;
  RCLASS_DESC: string;
  RCLASS_ID: number;
}

export interface CfgRtype {
  BREAK_RES: string;
  RCLASS_ID: number;
  REL_STRENGTH: number;
  RTYPE_CODE: string;
  RTYPE_DESC: string;
  RTYPE_ID: number;
}

export interface CfgSfcall {
  EXEC_ORDER: number;
  FELEM_ID: number;
  FTYPE_ID: number;
  SFCALL_ID: number;
  SFUNC_ID: number;
}

export interface CfgSfunc {
  CONNECT_STR: string;
  FUNC_LIB: string;
  FUNC_VER: string;
  JAVA_CLASS_NAME: string;
  LANGUAGE: string;
  SFUNC_CODE: string;
  SFUNC_DESC: string;
  SFUNC_ID: number;
}

export interface ConfigBaseVersion {
  BUILD_DATE: string;
  BUILD_NUMBER: string;
  BUILD_VERSION: string;
  COMPATIBILITY_VERSION: CompatibilityVersion;
  PRODUCT_NAME: string;
  VERSION: string;
}

export interface CompatibilityVersion {
  CONFIG_VERSION: string;
}

export interface Config {
  CONFIG_COMMENTS: string;
  CONFIG_ID: number;
  SYS_CREATE_DT: string;
}

export interface Configs {
  CONFIGS: Config[];
}

export interface DataSource {
  /**
   * The text representation of the datasource.
   */
  DSRC_CODE: string;

  /**
   * The unique identifier of the datasource.
   */
  DSRC_ID: number;
}

export interface Datastore {
  id: string;
  location: string;
  type: string;
}

export interface DatastoreInfo {
  dataStores: Datastore[];
}

export interface DatastorePerformance {
  insertTime: number;
  numRecordsInserted: number;
}

export interface Entity {
  RELATED_ENTITIES: RelatedEntity[];
  RESOLVED_ENTITY: ResolvedEntity;
}

export interface EntityPath {
  END_ENTITY_ID: number;
  ENTITIES: number[];
  START_ENTITY_ID: number;
}

export interface ExportConfig {
  G2_CONFIG: G2config;
}

export interface Feature {
  FELEM_CODE: string;
  FELEM_VALUE: string;
}

export interface FeatureDescriptionValue {
  CANDIDATE_CAP_REACHED: string;
  ENTITY_COUNT: number;
  FEAT_DESC: string;
  LIB_FEAT_ID: number;
  SCORING_CAP_REACHED: string;
  SUPPRESSED: string;
  USED_FOR_CAND: string;
  USED_FOR_SCORING: string;
}

export interface FeatureForAttribute {
  FEAT_DESC: string;
  FEAT_DESC_VALUES: FeatureDescriptionValue[];
  LIB_FEAT_ID: number;
  USAGE_TYPE: string;
}

export interface FeatureScoreForAttribute {
  CANDIDATE_FEAT: string;
  CANDIDATE_FEAT_ID: number;
  CANDIDATE_FEAT_USAGE_TYPE: string;
  FULL_SCORE: number;
  GENERATION_MATCH: number;
  GNR_FN: number;
  GNR_GN: number;
  GNR_ON: number;
  GNR_SN: number;
  INBOUND_FEAT: string;
  INBOUND_FEAT_ID: number;
  INBOUND_FEAT_USAGE_TYPE: string;
  SCORE_BEHAVIOR: string;
  SCORE_BUCKET: string;
}

export type FeatureScores = string;

export type FeatureScoresForAttribute = FeatureScoreForAttribute[];

export type FetchNext = FixmeUnknown;

export interface FinalState {
  NEED_REEVALUATION: number;
  VIRTUAL_ENTITIES: VirtualEntitySynopsis[];
}

export interface FixmeUnknown {
  FIXME_UNKNOWN: string;
}

export interface FocusRecord {
  DATA_SOURCE: string;
  RECORD_ID: string;
}

export type FocusRecords = FocusRecord[];

export interface G2config {
  CFG_ATTR: CfgAttr[];
  CFG_CFBOM: CfgCfbom[];
  CFG_CFCALL: CfgCfcall[];
  CFG_CFRTN: CfgCfrtn[];
  CFG_CFUNC: CfgCfunc[];
  CFG_DFBOM: CfgDfbom[];
  CFG_DFCALL: CfgDfcall[];
  CFG_DFUNC: CfgDfunc[];
  CFG_DSRC: CfgDsrc[];
  CFG_DSRC_INTEREST: CfgDsrcInterest[];
  CFG_EBOM: CfgEbom[];
  CFG_ECLASS: CfgEclass[];
  CFG_EFBOM: CfgEfbom[];
  CFG_EFCALL: CfgEfcall[];
  CFG_EFUNC: CfgEfunc[];
  CFG_ERFRAG: CfgErfrag[];
  CFG_ERRULE: CfgErrule[];
  CFG_ETYPE: CfgEtype[];
  CFG_FBOM: CfgFbom[];
  CFG_FBOVR: CfgFbovr[];
  CFG_FCLASS: CfgFclass[];
  CFG_FELEM: CfgFelem[];
  CFG_FTYPE: CfgFtype[];
  CFG_GENERIC_THRESHOLD: CfgGenericThreshold[];
  CFG_GPLAN: CfgGplan[];
  CFG_LENS: CfgLens[];
  CFG_LENSRL: CfgLensrl[];
  CFG_RCLASS: CfgRclass[];
  CFG_RTYPE: CfgRtype[];
  CFG_SFCALL: CfgSfcall[];
  CFG_SFUNC: CfgSfunc[];
  CONFIG_BASE_VERSION: ConfigBaseVersion;
  SYS_OOM: SysOom[];
}

export interface GetConfig {
  G2_CONFIG: G2config;
}

export interface GetDataSources {
  DATA_SOURCES: DataSource[];
}

export interface GetFeature {
  ELEMENTS: Feature[];
  FTYPE_CODE: string;
  LIB_FEAT_ID: number;
}

export interface How {
  HOW_RESULTS: HowResults;
}

export interface HowResults {
  FINAL_STATE: FinalState;
  RESOLUTION_STEPS: ResolutionSteps;
}

export interface Interesting {
  INTERESTING_ENTITIES: InterestingEntities;
}

export interface InterestingEntities {
  ENTITIES: InterestingEntity[];
  NOTICES: Notices;
}

export interface InterestingEntitySampleRecords {
  DATA_SOURCE: string;
  FLAGS: string[];
  RECORD_ID: string;
}

export interface InterestingEntity {
  DEGREES: number;

  /**
   * The ENTITY_ID is the Senzing-generated identifier for the discovered
   * entity. It may change when new information is added.
   */
  ENTITY_ID: number;
  FLAGS: string[];
  SAMPLE_RECORDS: InterestingEntitySampleRecords[];
}

export interface MatchInfoDisclosedRelationsRelAnchor {
  DOMAIN: string;
  FEAT_DESC: string;
  FEAT_ID: number;
  LINKED_FEAT_DESC: string;
  LINKED_FEAT_ID: number;
  LINKED_FEAT_TYPE: string;
  LINKED_FEAT_USAGE_TYPE: string;
}

export interface MatchInfoDisclosedRelationsRelLink {
  DOMAIN: string;
  FEAT_DESC: string;
  FEAT_ID: number;
  FEAT_USAGE_TYPE: string;
  LINKED_FEAT_DESC: string;
  LINKED_FEAT_ID: number;
  LINKED_FEAT_TYPE: string;
  LINKED_FEAT_USAGE_TYPE: string;
}

export interface MatchInfoDisclosedRelationsRelPointer {
  DOMAIN: string;
  FEAT_DESC: string;
  FEAT_ID: number;
  FEAT_USAGE_TYPE: string;
  LINKED_FEAT_DESC: string;
  LINKED_FEAT_ID: number;
  LINKED_FEAT_TYPE: string;
}

export interface MatchInfoDisclosedRelations {
  REL_ANCHOR: MatchInfoDisclosedRelationsRelAnchor[];
  REL_LINK: MatchInfoDisclosedRelationsRelLink[];
  REL_POINTER: MatchInfoDisclosedRelationsRelPointer[];
}

export interface MatchInfo {
  CANDIDATE_KEYS: MatchInfoCandidateKeys;
  DISCLOSED_RELATIONS: MatchInfoDisclosedRelations;
  ERRULE_CODE: string;
  FEATURE_SCORES: FeatureScores;
  MATCH_KEY: string;
  MATCH_LEVEL: number;
  MATCH_LEVEL_CODE: string;
  WHY_ERRULE_CODE: string;
  WHY_KEY: string;
}

export type MatchInfoCandidateKeys = string;

export interface MatchInfoForAttribute {
  FEAT_DESC: string;
  FEAT_ID: number;
}

export interface MemberRecord {
  INTERNAL_ID: number;
  RECORDS: Records;
}

export type MemberRecords = MemberRecord[];

export interface Network {
  ENTITIES: Entity[];
  ENTITY_PATHS: EntityPath[];
  MAX_ENTITY_LIMIT_REACHED: string;
}

export interface Notice {
  CODE: string;
  DESCRIPTION: string;
}

export type Notices = Notice[];

export interface Path {
  ENTITIES: Entity[];
  ENTITY_PATHS: EntityPath[];
}

export interface ProductLicense {
  billing: string;
  contract: string;
  customer: string;
  expireDate: string;
  issueDate: string;
  licenseLevel: string;
  licenseType: string;
  recordLimit: number;
}

export interface ProductVersion {
  BUILD_DATE: string;
  BUILD_NUMBER: string;
  BUILD_VERSION: string;
  COMPATIBILITY_VERSION: CompatibilityVersion;
  PRODUCT_NAME: string;
  SCHEMA_VERSION: SchemaVersion;
  VERSION: string;
}

export interface RecordFeatures {
  LIB_FEAT_ID: number;
  USAGE_TYPE: string;
}

export interface Record {
  ADDRESS_DATA: string[];
  ATTRIBUTE_DATA: string[];
  DATA_SOURCE: string;
  ENTITY_DATA: string[];
  ENTITY_DESC: string;
  ENTITY_KEY: string;
  ENTITY_TYPE: string;
  ERRULE_CODE: string;
  FEATURES: RecordFeatures[];
  IDENTIFIER_DATA: string[];
  INTERNAL_ID: number;
  JSON_DATA: string;
  LAST_SEEN_DT: string;
  MATCH_KEY: string;
  MATCH_LEVEL: number;
  MATCH_LEVEL_CODE: string;
  NAME_DATA: string[];
  OTHER_DATA: string[];
  PHONE_DATA: string[];
  RECORD_ID: string;
  RELATIONSHIP_DATA: string[];
}

export interface RecordSummaryElement {
  DATA_SOURCE: string;
  FIRST_SEEN_DT: string;
  LAST_SEEN_DT: string;
  RECORD_COUNT: number;
}

export type Records = Record[];

export type RedoRecord = FixmeUnknown;

export interface RelatedEntity {
  /**
   * The ENTITY_ID is the Senzing-generated identifier for the discovered
   * entity. It may change when new information is added.
   */
  ENTITY_ID: number;
  ENTITY_NAME: string;
  ERRULE_CODE: string;
  IS_AMBIGUOUS: number;
  IS_DISCLOSED: number;
  LAST_SEEN_DT: string;
  MATCH_KEY: string;
  MATCH_LEVEL: number;
  MATCH_LEVEL_CODE: string;
  RECORDS: Records;
  RECORD_SUMMARY: RecordSummaryElement[];
}

export interface ResolutionStep {
  INBOUND_VIRTUAL_ENTITY_ID: string;
  MATCH_INFO: MatchInfo;
  RESULT_VIRTUAL_ENTITY_ID: string;
  STEP: number;
  VIRTUAL_ENTITY_1: VirtualEntitySynopsis;
  VIRTUAL_ENTITY_2: VirtualEntitySynopsis;
}

export type ResolutionSteps = ResolutionStep[];

export interface ResolvedEntity {
  /**
   * The ENTITY_ID is the Senzing-generated identifier for the discovered
   * entity. It may change when new information is added.
   */
  ENTITY_ID: number;
  ENTITY_NAME: string;
  ERRULE_CODE: string;
  FEATURES: string;
  IS_AMBIGUOUS: number;
  IS_DISCLOSED: number;
  LAST_SEEN_DT: string;
  MATCH_KEY: string;
  MATCH_LEVEL: number;
  MATCH_LEVEL_CODE: string;
  RECORDS: Records;
  RECORD_SUMMARY: RecordSummaryElement[];
}

export interface ResolvedEntityAndMatchInfoEntity {
  RESOLVED_ENTITY: ResolvedEntity;
}

export interface ResolvedEntityAndMatchInfo {
  ENTITY: ResolvedEntityAndMatchInfoEntity;
  MATCH_INFO: MatchInfo;
}

export interface SysOom {
  FELEM_ID: number;
  FTYPE_ID: number;
  LENS_ID: number;
  LIB_FEAT_ID: number;
  LIB_FELEM_ID: number;
  NEXT_THRESH: number;
  OOM_LEVEL: string;
  OOM_TYPE: string;
  THRESH1_CNT: number;
  THRESH1_OOM: number;
}

export interface SchemaVersion {
  ENGINE_SCHEMA_VERSION: string;
  MAXIMUM_REQUIRED_SCHEMA_VERSION: string;
  MINIMUM_REQUIRED_SCHEMA_VERSION: string;
}

export interface Search {
  RESOLVED_ENTITIES: ResolvedEntityAndMatchInfo[];
  SEARCH_STATISTICS: SearchStatistics;
}

export interface SearchStatisticCandidateKeysFeatureTypes {
  FOUND: number;
  FTYPE_CODE: string;
  GENERIC: number;
  NOT_FOUND: number;
}

export interface SearchStatisticCandidateKeysSummary {
  FOUND: number;
  GENERIC: number;
  NOT_FOUND: number;
}

export interface SearchStatisticCandidateKeys {
  FEATURE_TYPES: SearchStatisticCandidateKeysFeatureTypes[];
  SUMMARY: SearchStatisticCandidateKeysSummary;
}

export interface SearchStatistic {
  CANDIDATE_KEYS: SearchStatisticCandidateKeys;
}

export type SearchStatistics = SearchStatistic[];

export type Stats = FixmeUnknown;

export type StreamExportJsonEntity = FixmeUnknown;

export type SzConfigAddDataSourceResponse = AddDataSource;

export type SzConfigExportConfigResponse = ExportConfig;

export type SzConfigGetDataSourcesResponse = GetDataSources;

export type SzConfigManagerGetConfigResponse = GetConfig;

export type SzConfigManagerGetConfigsResponse = Configs;

export type SzDiagnosticCheckDatastorePerformanceResponse = DatastorePerformance;

export type SzDiagnosticGetDatastoreInfoResponse = DatastoreInfo;

export type SzDiagnosticGetFeatureResponse = GetFeature;

export type SzEngineAddRecordResponse = WithInfo;

export type SzEngineDeleteRecordResponse = WithInfo;

export type SzEngineFetchNextResponse = FetchNext;

export type SzEngineFindInterestingEntitiesByEntityIdResponse = Interesting;

export type SzEngineFindInterestingEntitiesByRecordIdResponse = Interesting;

export type SzEngineFindNetworkByEntityIdResponse = Network;

export type SzEngineFindNetworkByRecordIdResponse = Network;

export type SzEngineFindPathByEntityIdResponse = Path;

export type SzEngineFindPathByRecordIdResponse = Path;

export type SzEngineGetEntityByEntityIdResponse = Entity;

export type SzEngineGetEntityByRecordIdResponse = Entity;

export type SzEngineGetRecordResponse = Record;

export type SzEngineGetRedoRecordResponse = RedoRecord;

export type SzEngineGetStatsResponse = Stats;

export type SzEngineGetVirtualEntityByRecordIdResponse = VirtualEntity;

export type SzEngineHowEntityByEntityIdResponse = How;

export type SzEngineProcessRedoRecordResponse = WithInfo;

export type SzEngineReevaluateEntityResponse = WithInfo;

export type SzEngineReevaluateRecordResponse = WithInfo;

export type SzEngineSearchByAttributesResponse = Search;

export type SzEngineStreamExportJsonEntityReportResponse = StreamExportJsonEntity;

export type SzEngineWhyEntitiesResponse = WhyEntities;

export type SzEngineWhyRecordInEntityResponse = WhyRecordInEntity;

export type SzEngineWhyRecordsResponse = WhyRecords;

export type SzProductGetLicenseResponse = ProductLicense;

export type SzProductGetVersionResponse = ProductVersion;

export interface VirtualEntity {
  RESOLVED_ENTITY: ResolvedEntity;
}

export interface VirtualEntitySynopsis {
  MEMBER_RECORDS: MemberRecords;
  VIRTUAL_ENTITY_ID: string;
}

export interface WhyEntities {
  ENTITIES: Entity[];
  WHY_RESULTS: WhyResults;
}

export type WhyRecordInEntity = FixmeUnknown;

export interface WhyRecords {
  ENTITIES: Entity[];
  WHY_RESULTS: WhyResults;
}

export interface WhyResult {
  /**
   * The ENTITY_ID is the Senzing-generated identifier for the discovered
   * entity. It may change when new information is added.
   */
  ENTITY_ID: number;
  ENTITY_ID_2: number;
  FOCUS_RECORDS: FocusRecords;
  FOCUS_RECORDS_2: FocusRecords;
  INTERNAL_ID: number;
  INTERNAL_ID_2: number;
  MATCH_INFO: MatchInfo;
}

export type WhyResults = WhyResult[];

export interface WithInfo {
  AFFECTED_ENTITIES: AffectedEntity[];
  DATA_SOURCE: string;
  INTERESTING_ENTITIES: InterestingEntities;
  RECORD_ID: string;
}

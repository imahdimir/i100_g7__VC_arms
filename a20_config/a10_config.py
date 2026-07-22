from pathlib import Path


class Directories:
    project_root: Path = Path('/sharedata/camm/c_projects/i100_g7__VC_arms')
    pitchbook_full_data = Path('/sharedata/camm/b000_PitchBook_Full_Data')

    b15_data_input = project_root / 'b15_data_input'
    d10_data_manual = project_root / 'd10_data_manual'
    f10_data_interim = project_root / 'f10_data_interim'
    g10_data_processed = project_root / 'g10_data_processed'
    g20_results_tables = project_root / 'g20_results_tables'
    g22_result_table_pics = project_root / 'g22_result_table_pics'
    g30_results_plots = project_root / 'g30_results_plots'
    g32_results_plot_with_tables = project_root / 'g32_results_plot_with_tables'


class FilePaths:
    dyr = Directories()

    # PitchBook Full Data Parquet Files
    pb_fund__parq = dyr.pitchbook_full_data / 'Fund.parquet'
    pb_investor__parq = dyr.pitchbook_full_data / 'Investor.parquet'
    pb_ent_aff_rel__parq = dyr.pitchbook_full_data / 'EntityAffiliateRelation.parquet'
    pb_deals__parq = dyr.pitchbook_full_data / 'Deal.parquet'
    pb_deal_inv_rel__parq = dyr.pitchbook_full_data / 'DealInvestorRelation.parquet'
    pb_companies__parq = dyr.pitchbook_full_data / 'Company.parquet'
    pb_limited_partners__parq = dyr.pitchbook_full_data / 'LimitedPartner.parquet'

    # manual data files
    dm_sp030_10__selected_funds__xl = dyr.d10_data_manual / 'dm_sp030_10__selected_funds.xlsx'

    # sp040
    dm_sp040_10__affiliated_entities_manual_list__xl = dyr.d10_data_manual / 'dm_sp040_10__affiliated_entities_manual_list.xlsx'
    dm_sp040_15__manual_hospitals_list__xl = dyr.d10_data_manual / 'dm_sp040_15__manual_hospitals_list.xlsx'

    # sp050
    di_sp050_05__hospitals_with_affiliated_vc_by_data_properties_only__xl = dyr.f10_data_interim / 'di_sp050_05__hospitals_with_affiliated_vc_by_data_properties_only.xlsx'
    di_sp050_10__VCs_with_affiliated_hospitals_by_data_properties_only__xl = dyr.f10_data_interim / 'di_sp050_10__VCs_with_affiliated_hosps_by_data_properties_only.xlsx'

    di_sp050_15__hospitals_with_affiliated_vc__manual_list_added_to_by_data_property__xl = dyr.f10_data_interim / 'di_sp050_15__hospitals_with_affiliated_vc__manual_list_added_to_by_data_property.xlsx'
    di_sp050_20__VCs_with_affiliated_hospitals_manual_list_added_to_by_data_property__xl = dyr.f10_data_interim / 'di_sp050_20__VCs_with_affiliated_hospitals_manual_list_added_to_by_data_property.xlsx'

    # sp060
    di_sp060_01__all_hospitals_and_VC_affiliations__preliminary__xl = dyr.f10_data_interim / 'di_sp060_01__all_hospitals_and_VC_affiliations__preliminary.xlsx'
    di_sp060_03__xl = dyr.f10_data_interim / 'di_sp060_03.xlsx'
    di_sp060_05__all_hospitals_and_VC_affiliations__xl = dyr.f10_data_interim / 'di_sp060_05__all_hospitals_and_VC_affiliations.xlsx'
    dp_sp060_10__all_hospitals_and_VC_affiliations__final__xl = dyr.g10_data_processed / 'dp_sp060_10__all_hospitals_and_VC_affiliations__final.xlsx'
    rt_sp060_15 = dyr.g20_results_tables / 'rt_sp060_15__unique_vc_hospital_and_pair_types_count.xlsx'
    sp060_20 = dyr.g20_results_tables / 'sp060_20.svg'

    # sp070
    di_sp070_05__vc_related_deal_ids__xl = dyr.f10_data_interim / 'di_sp070_05__vc_related_deal_ids.xlsx'
    di_sp070_10__vc_related_deals__n1__xl = dyr.f10_data_interim / 'di_sp070_10__vc_related_deals__n1.xlsx'
    dp_sp070_15__vc_related_deals__n2Final__xl = dyr.g10_data_processed / 'dp_sp070_15__vc_related_deals__n2Final.xlsx'
    rt_sp070_20__vc_deals_by_year__xl = dyr.g20_results_tables / 'rt_sp070_20__vc_deals_by_year.xlsx'
    dp_sp070_25__companies_in_vc_deals__xl = dyr.g10_data_processed / 'dp_sp070_25__companies_in_vc_deals.xlsx'

    # sp080
    rt_sp080_05_vc_affiliations_frequency__xl = dyr.g20_results_tables / 'rt_sp080_05_vc_affiliations_frequency.xlsx'
    rt_sp080_10_hospitals_affiliations_frequency__xl = dyr.g20_results_tables / 'rt_sp080_10_hospitals_affiliations_frequency.xlsx'

    # sp090.R
    rp_sp090_05__deals_count_by_year__fmt1__pdf = dyr.g30_results_plots / f'rp_sp090_05__deals_count_by_year__fmt1.pdf'
    rp_sp090_10__deals_count_by_year__fmt2__svg = dyr.g30_results_plots / f'rp_sp090_10__deals_count_by_year__fmt2.svg'

    rt_sp090_15__vc_related_deals_sum_stats__xl = dyr.g20_results_tables / f'rt_sp090_15__vc_related_deals_sum_stats.xlsx'

    rp_sp090_20__deals_amount_by_year__fmt1__pdf = dyr.g30_results_plots / f'rp_sp090_20__deals_amount_by_year__fmt1.pdf'
    rp_sp090_25__deals_amount_by_year__fmt2__svg = dyr.g30_results_plots / f'rp_sp090_25__deals_amount_by_year__fmt2.svg'

    rp_sp090_30__deals_mean_amount_by_year__fmt1__pdf = dyr.g30_results_plots / f'rp_sp090_30__deals_mean_amount_by_year__fmt1.pdf'
    rp_sp090_35__deals_mean_amount_by_year__fmt2__svg = dyr.g30_results_plots / f'rp_sp090_35__deals_mean_amount_by_year__fmt2.svg'

    rp_sp090_40__deals_median_by_year__fmt1__pdf = dyr.g30_results_plots / f'rp_sp090_40__deals_median_by_year__fmt1.pdf'
    rp_sp090_45__deals_median_by_year__fmt2__svg = dyr.g30_results_plots / f'rp_sp090_45__deals_median_by_year__fmt2.svg'

    rp_sp090_50__invested_industries__fmt1__pdf = dyr.g30_results_plots / f'rp_sp090_50__invested_industries__fmt1.pdf'
    rp_sp090_55__invested_industries__fmt2__svg = dyr.g30_results_plots / f'rp_sp090_55__invested_industries__fmt2.svg'

    # sp100
    sp100_20 = dyr.f10_data_interim / 'sp100_20.xlsx'
    sp100_25__t1 = dyr.g22_result_table_pics / 'sp100_10__t1.svg'
    sp100_30__t2 = dyr.g22_result_table_pics / 'sp100_30__t2.svg'
    sp100_32 = dyr.g32_results_plot_with_tables / 'sp100_32.svg'
    sp100_35 = dyr.g32_results_plot_with_tables / 'sp100_35.svg'
    sp100_40 = dyr.g32_results_plot_with_tables / 'sp100_40.svg'
    sp100_45_df11 = dyr.f10_data_interim / 'sp100_45.xlsx'
    sp100_50 = dyr.g32_results_plot_with_tables / 'sp100_50.svg'
    sp100_60 = dyr.g32_results_plot_with_tables / 'sp100_60.svg'
    sp100_65 = dyr.g32_results_plot_with_tables / 'sp100_65.svg'
    sp100_70 = dyr.g10_data_processed / 'sp100_70.xlsx'

    sp110_pb_ss = dyr.b15_data_input / 'pb_ss_investor_match.xlsx'
    sp100_stepstone_gps = dyr.b15_data_input / 'Stepstone_GPs.csv'


class Constants:
    sub = 'Subsidiary'
    par = 'Parent'
    sis = 'Sister'
    hospital = 'hospital'
    vc = 'vc'
    not_vc_nor_hospital = 'not_vc_nor_hospital'
    com = 'com'
    com_dot = 'Company.'
    inv_dot = 'Investor.'
    lp_dot = 'LimitedPartner.'


class Variables:
    """ Variables for Observations or columns in the data """
    const = Constants()

    # PitchBook data variables/columns
    fund_id = 'FundID'
    investor = 'Investor'
    fund_no = 'FundNo'
    investor_name = 'InvestorName'
    investor_fund_id = 'InvestorFundID'
    investor_fund_name = 'InvestorFundName'
    universe__pb = 'Universe'
    primary_industry_sec__pb = 'PrimaryIndustrySector'
    primary_industry_gp__pb = 'PrimaryIndustryGroup'
    industry = 'Industry'
    industry__pb = 'Industry'
    entity_id = 'EntityID'
    entity_id__pb = 'EntityID'
    affiliate_id = 'AffiliateID'
    affiliate_id__pb = 'AffiliateID'
    aff_type = 'AffiliateType'
    affiliate_type__pb = 'AffiliateType'
    comp_id = 'CompanyID'
    comp_id__pb = 'CompanyID'
    investor_id = 'InvestorID'
    deal_id = 'DealID'
    deal_status = 'DealStatus'
    native_currency = 'NativeCurrencyOfDeal'
    exit_scope = 'ExitScope'
    from_pitchbook = 'FromPitchBook'  # For the hospital VC affiliation data, indicates if the data came from PitchBook or manual entry if True it was available in PitchBook and if False it was manually entered
    pair_id = 'pair_id'  # For the hospital VC affiliation data, indicates unique pairs of Hospital and VC Firm
    affiliate_type = 'affiliate_type'
    entity_type = 'entity_type'
    not_valid_affiliation_type = 'not_valid_affiliation_type'  # For the hospital VC affiliation data, indicates if the affiliation type is not valid, e.g., having subsidiary and sister affiliation types at the same time one way is called subsidiary and the other sister, I removed these ones from valid data
    deal_date = 'DealDate'
    deal_size = 'DealSize'
    deal_year = 'deal_year'

    name_from_media = 'NameFromMedia'  # the hospital name from that media list
    pb_url = 'PBURL'
    pb_id = 'PBID'  # Pitchbook ID
    pb_type = 'PBEntityType'
    company_id = 'CompanyID'
    com_dot__company_id = const.com_dot + company_id
    matched_from_com = 'Matched_From_Com'

    inv_dot__investor_id = const.inv_dot + investor_id
    matched_from_inv = 'Matched_From_Inv'

    limited_partner_id = 'LimitedPartnerID'
    lp_dot__lp_id = const.lp_dot + limited_partner_id
    matched_from_lp = 'Matched_From_LP'

    hospital_id = 'HospitalID'
    aff_id = 'AffiliateID'

    parent_com_id = 'ParentCompanyID'

    pair_parent_count = 'pair_parent_count'
    pair_uniq_parent_count = 'pair_uniq_parent_count'
    both_sisters_have_same_parent = 'both_sisters_have_same_parent'
    aff_type_par = 'affiliate_type_par'
    child_vc_id = 'child_vc_id'
    parent_hospital_id = 'parent_hospital_id'
    sister_or_parsub = 'sister_or_parsub'
    parent_hospital_industry = 'parent_hospital_industry'
    child_vc_industry = 'child_vc_industry'
    parent_hospital_universe = 'parent_hospital_Universe'


dyr = Directories()
file = FilePaths()
fi = file
const = Constants()
c = const
var = Variables()
v = var


def normalize_instance_paths_from_class(cls_instance):
    """
    Convert class-level Path attributes into OS-agnostic string (POSIX) attributes
    on the given instance. Does not modify other instance-level attributes.

    Args:
        cls_instance: An instance of a class whose class has Path attributes.

    Returns:
        The same instance, with Path attributes copied as strings.
    """
    if isinstance(cls_instance, type):
        raise TypeError("Expected a class instance, not a class.")

    for attr, value in list(vars(cls_instance.__class__).items()):
        if attr.startswith("__"):
            continue  # skip magic attributes
        if isinstance(value, Path):
            setattr(cls_instance, attr, value.as_posix())

    return cls_instance


# for using in R
# Not using dyr because it changes the existing instance
dyr_str = normalize_instance_paths_from_class(Directories())
file_str = normalize_instance_paths_from_class(FilePaths())
const_str = normalize_instance_paths_from_class(Constants())
var_str = normalize_instance_paths_from_class(Variables())

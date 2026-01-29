from pathlib import Path


class Directories:
    project_root: Path = Path('/sharedata/camm/c_projects/i100_g7__VC_arms')
    pitchbook_full_data = Path('/sharedata/camm/b000_PitchBook_Full_Data')

    d10_data_manual = project_root / 'd10_data_manual'
    f10_data_interim = project_root / 'f10_data_interim'
    g10_data_processed = project_root / 'g10_data_processed'
    g20_results_tables = project_root / 'g20_results_tables'
    g30_results_plots = project_root / 'g30_results_plots'


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
    di_sp060_05__all_hospitals_and_VC_affiliations__xl = dyr.f10_data_interim / 'di_sp060_05__all_hospitals_and_VC_affiliations.xlsx'
    dp_sp060_10__all_hospitals_and_VC_affiliations__final__xl = dyr.g10_data_processed / 'dp_sp060_10__all_hospitals_and_VC_affiliations__final.xlsx'

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


class Constants:
    sub = 'Subsidiary'
    par = 'Parent'
    sis = 'Sister'
    hospital = 'hospital'
    vc = 'vc'

    # sp040
    com = 'com'
    com_dot = 'Company.'
    inv_dot = 'Investor.'
    lp_dot = 'LimitedPartner.'


class Variables:
    """ Variables for Observations or columns in the data """
    const = Constants()

    fund_id = 'FundID'
    investor = 'Investor'
    fund_no = 'FundNo'
    investor_name = 'InvestorName'
    investor_fund_id = 'InvestorFundID'
    investor_fund_name = 'InvestorFundName'

    industry = 'Industry'
    entity_id = 'EntityID'
    affiliate_id = 'AffiliateID'
    aff_type = 'AffiliateType'
    comp_id = 'CompanyID'
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

    # sp040
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


dyr = Directories()
file = FilePaths()
const = Constants()
var = Variables()


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

# # !/usr/bin/env python3
# """
# Script to display Jupyter kernel name and conda environment information
# """
#
# import sys
# import os
# import json
#
#
# def get_jupyter_kernel_name():
#     """Get the current Jupyter kernel name"""
#     try:
#         # Method 1: Check if running in IPython/Jupyter
#         from IPython import get_ipython
#         ipython = get_ipython()
#
#         if ipython is not None:
#             # Try to get connection file
#             connection_file = ipython.config.get('IPKernelApp', {}).get('connection_file', '')
#             if connection_file:
#                 print(f"Jupyter Connection File: {connection_file}")
#
#             # Get kernel info from connection file
#             if connection_file and os.path.exists(connection_file):
#                 with open(connection_file, 'r') as f:
#                     kernel_info = json.load(f)
#                     print(f"Kernel Info: {kernel_info.get('kernel_name', 'N/A')}")
#         else:
#             print("Not running in Jupyter/IPython environment")
#
#     except ImportError:
#         print("IPython not available - not running in Jupyter")
#     except Exception as e:
#         print(f"Could not determine Jupyter kernel: {e}")
#
#
# def get_conda_environment():
#     """Get conda environment name and path"""
#     print("\n--- Conda Environment Info ---")
#
#     # Method 1: CONDA_DEFAULT_ENV environment variable
#     conda_env = os.environ.get('CONDA_DEFAULT_ENV')
#     if conda_env:
#         print(f"Conda Environment Name: {conda_env}")
#     else:
#         print("CONDA_DEFAULT_ENV not set (may not be in conda environment)")
#
#     # Method 2: CONDA_PREFIX (conda environment path)
#     conda_prefix = os.environ.get('CONDA_PREFIX')
#     if conda_prefix:
#         print(f"Conda Environment Path: {conda_prefix}")
#     else:
#         print("CONDA_PREFIX not set")
#
#     # Method 3: Check sys.prefix (Python installation path)
#     print(f"Python Prefix (sys.prefix): {sys.prefix}")
#
#     # Check if we're in base environment
#     if conda_env == 'base':
#         print("Running in conda base environment")
#     elif conda_env:
#         print(f"Running in conda environment: {conda_env}")
#     else:
#         print("Not running in a conda environment (or conda not activated)")
#
#
# def get_python_executable():
#     """Get Python executable path"""
#     print("\n--- Python Executable Info ---")
#     print(f"Python Executable: {sys.executable}")
#     print(f"Python Version: {sys.version}")
#     print(f"Python Path: {sys.prefix}")
#
#
# def main():
#     print("=" * 60)
#     print("JUPYTER KERNEL AND CONDA ENVIRONMENT INFORMATION")
#     print("=" * 60)
#
#     get_jupyter_kernel_name()
#     get_conda_environment()
#     get_python_executable()
#
#     print("\n--- All Environment Variables (conda-related) ---")
#     for key, value in os.environ.items():
#         if 'CONDA' in key or 'JUPYTER' in key:
#             print(f"{key}: {value}")

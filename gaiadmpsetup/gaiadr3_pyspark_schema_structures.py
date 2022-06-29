from pyspark.sql.types import *

vari_time_series_statistics_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('num_selected_g_fov', ShortType(), True), # Total number of G FOV transits selected for variability analysis
    StructField('mean_obs_time_g_fov', DoubleType(), True), # Mean observation time for G FoV transits
    StructField('time_duration_g_fov', FloatType(), True), # Time duration of the time series for G FoV transits
    StructField('min_mag_g_fov', FloatType(), True), # Minimum G FoV magnitude
    StructField('max_mag_g_fov', FloatType(), True), # Maximum G FoV magnitude
    StructField('mean_mag_g_fov', FloatType(), True), # Mean G FoV magnitude
    StructField('median_mag_g_fov', FloatType(), True), # Median G FoV magnitude
    StructField('range_mag_g_fov', FloatType(), True), # Difference between the highest and lowest G FoV magnitudes
    StructField('trimmed_range_mag_g_fov', FloatType(), True), # Trimmed difference between the highest and lowest G FoV magnitudes
    StructField('std_dev_mag_g_fov', FloatType(), True), # Square root of the unweighted G FoV magnitude variance
    StructField('skewness_mag_g_fov', FloatType(), True), # Standardized unweighted G FoV magnitude skewness
    StructField('kurtosis_mag_g_fov', FloatType(), True), # Standardized unweighted G FoV magnitude kurtosis
    StructField('mad_mag_g_fov', FloatType(), True), # Median Absolute Deviation (MAD) for G FoV transits
    StructField('abbe_mag_g_fov', FloatType(), True), # Abbe value for G FoV transits
    StructField('iqr_mag_g_fov', FloatType(), True), # Interquartile range for G FoV transits
    StructField('stetson_mag_g_fov', FloatType(), True), # Stetson G FoV variability index
    StructField('std_dev_over_rms_err_mag_g_fov', FloatType(), True), # Signal-to-Noise G FoV estimate
    StructField('outlier_median_g_fov', FloatType(), True), # Greatest absolute deviation from the G FoV median normalized by the error
    StructField('num_selected_bp', ShortType(), True), # Total number of BP observations selected for variability analysis
    StructField('mean_obs_time_bp', DoubleType(), True), # Mean observation time for BP observations
    StructField('time_duration_bp', FloatType(), True), # Time duration of the BP time series
    StructField('min_mag_bp', FloatType(), True), # Minimum BP magnitude
    StructField('max_mag_bp', FloatType(), True), # Maximum BP magnitude
    StructField('mean_mag_bp', FloatType(), True), # Mean BP magnitude
    StructField('median_mag_bp', FloatType(), True), # Median BP magnitude
    StructField('range_mag_bp', FloatType(), True), # Difference between the highest and lowest BP magnitudes
    StructField('trimmed_range_mag_bp', FloatType(), True), # Trimmed difference between the highest and lowest BP magnitudes
    StructField('std_dev_mag_bp', FloatType(), True), # Square root of the unweighted BP magnitude variance
    StructField('skewness_mag_bp', FloatType(), True), # Standardized unweighted BP magnitude skewness
    StructField('kurtosis_mag_bp', FloatType(), True), # Standardized unweighted BP magnitude kurtosis
    StructField('mad_mag_bp', FloatType(), True), # Median Absolute Deviation (MAD) for BP observations
    StructField('abbe_mag_bp', FloatType(), True), # Abbe value for BP observations
    StructField('iqr_mag_bp', FloatType(), True), # Interquartile BP magnitude range
    StructField('stetson_mag_bp', FloatType(), True), # Stetson BP variability index
    StructField('std_dev_over_rms_err_mag_bp', FloatType(), True), # Signal-to-Noise BP estimate
    StructField('outlier_median_bp', FloatType(), True), # Greatest absolute deviation from the BP median normalized by the error
    StructField('num_selected_rp', ShortType(), True), # Total number of RP observations selected for variability analysis
    StructField('mean_obs_time_rp', DoubleType(), True), # Mean observation time for RP observations
    StructField('time_duration_rp', FloatType(), True), # Time duration of the RP time series
    StructField('min_mag_rp', FloatType(), True), # Minimum RP magnitude
    StructField('max_mag_rp', FloatType(), True), # Maximum RP magnitude
    StructField('mean_mag_rp', FloatType(), True), # Mean RP magnitude
    StructField('median_mag_rp', FloatType(), True), # Median RP magnitude
    StructField('range_mag_rp', FloatType(), True), # Difference between the highest and lowest RP magnitudes
    StructField('trimmed_range_mag_rp', FloatType(), True), # Trimmed difference between the highest and lowest RP magnitudes
    StructField('std_dev_mag_rp', FloatType(), True), # Square root of the unweighted RP magnitude variance
    StructField('skewness_mag_rp', FloatType(), True), # Standardized unweighted RP magnitude skewness
    StructField('kurtosis_mag_rp', FloatType(), True), # Standardized unweighted RP magnitude kurtosis
    StructField('mad_mag_rp', FloatType(), True), # Median Absolute Deviation (MAD) for RP observations
    StructField('abbe_mag_rp', FloatType(), True), # Abbe value for RP observations
    StructField('iqr_mag_rp', FloatType(), True), # Interquartile RP magnitude range
    StructField('stetson_mag_rp', FloatType(), True), # Stetson RP variability index
    StructField('std_dev_over_rms_err_mag_rp', FloatType(), True), # Signal-to-Noise RP estimate
    StructField('outlier_median_rp', FloatType(), True), # Greatest absolute deviation from the RP median normalized by the error
])
alerts_mixedin_sourceids_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('alert_source_id', LongType(), False), # Primary sourceId associated to the alert
    StructField('mixed_in_source_id', LongType(), False), # Additional sourceId, if any, associated to the alert
])
astrophysical_parameters_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source Identifier
    StructField('classprob_dsc_combmod_quasar', FloatType(), True), # Probability from DSC-Combmod of being a quasar (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_galaxy', FloatType(), True), # Probability from DSC-Combmod of being a galaxy (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_star', FloatType(), True), # Probability from DSC-Combmod of being a single star (but not a white dwarf) (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_whitedwarf', FloatType(), True), # Probability from DSC-Combmod of being a white dwarf (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_binarystar', FloatType(), True), # Probability from DSC-Combmod of being a binary star (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_specmod_quasar', FloatType(), True), # Probability from DSC-Specmod of being a quasar (data used: BP/RP spectrum)
    StructField('classprob_dsc_specmod_galaxy', FloatType(), True), # Probability from DSC-Specmod of being a galaxy (data used: BP/RP spectrum)
    StructField('classprob_dsc_specmod_star', FloatType(), True), # Probability from DSC-Specmod of being a single star (but not a white dwarf) (data used: BP/RP spectrum)
    StructField('classprob_dsc_specmod_whitedwarf', FloatType(), True), # Probability from DSC-Specmod of being a white dwarf (data used: BP/RP spectrum)
    StructField('classprob_dsc_specmod_binarystar', FloatType(), True), # Probability from DSC-Specmod of being a binary star (data used: BP/RP spectrum)
    StructField('classprob_dsc_allosmod_quasar', FloatType(), True), # Probability from DSC-Allosmod of being a quasar (data used: photometry, astrometry)
    StructField('classprob_dsc_allosmod_galaxy', FloatType(), True), # Probability from DSC-Allosmod of being a galaxy (data used: photometry, astrometry)
    StructField('classprob_dsc_allosmod_star', FloatType(), True), # Probability from DSC-Allosmod of being a star (data used: photometry, astrometry)
    StructField('teff_gspphot', FloatType(), True), # Effective temperature from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('teff_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('teff_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logg_gspphot', FloatType(), True), # Surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logg_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logg_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mh_gspphot', FloatType(), True), # Iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mh_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mh_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('distance_gspphot', FloatType(), True), # Distance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('distance_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of distance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('distance_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of distance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('azero_gspphot', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('azero_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('azero_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ag_gspphot', FloatType(), True), # Extinction in G band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ag_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ag_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('abp_gspphot', FloatType(), True), # Extinction in $G_{\rm BP}$ band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('abp_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{\rm BP}$ band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('abp_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{\rm BP}$ band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('arp_gspphot', FloatType(), True), # Extinction in $G_{\rm RP}$ band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('arp_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{\rm RP}$ band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('arp_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{\rm RP}$ band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ebpminrp_gspphot', FloatType(), True), # Reddening $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ebpminrp_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of reddening  $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ebpminrp_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of reddening  $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mg_gspphot', FloatType(), True), # Absolute magnitude $M_{\rm G}$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mg_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of absolute magnitude $M_{\rm G}$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mg_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of absolute magnitude $M_{\rm G}$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('radius_gspphot', FloatType(), True), # Radius from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('radius_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of radius from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('radius_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of radius from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logposterior_gspphot', FloatType(), True), # Goodness-of-fit score (mean log-posterior of MCMC) of GSP-Phot Aeneas MCMC best library
    StructField('mcmcaccept_gspphot', FloatType(), True), # MCMC acceptance rate of GSP-Phot Aeneas MCMC best library
    StructField('libname_gspphot', StringType(), True), # Name of library that achieves the highest mean log-posterior in MCMC samples and was used to derive GSP-Phot parameters in this table
    StructField('teff_gspspec', FloatType(), True), # Effective temperature from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations 
    StructField('teff_gspspec_lower', FloatType(), True), # 16th percentile of effective temperature from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('teff_gspspec_upper', FloatType(), True), # 84th percentile of effective temperature from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('logg_gspspec', FloatType(), True), # Logarithm of the stellar surface gravity from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('logg_gspspec_lower', FloatType(), True), # 16th percentile of the logarithm of the stellar surface gravity from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('logg_gspspec_upper', FloatType(), True), # 84th percentile of the logarithm of the stellar surface gravity from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('mh_gspspec', FloatType(), True), # Global metallicity [M/H] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('mh_gspspec_lower', FloatType(), True), # 16th percentile of global metallicity [M/H] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('mh_gspspec_upper', FloatType(), True), # 84th percentile of global metallicity [M/H] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('alphafe_gspspec', FloatType(), True), # Abundance of alpha-elements [alpha/Fe] with respect to iron from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('alphafe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of alpha-elements [alpha/Fe] with respect to iron from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('alphafe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of alpha-elements [alpha/Fe] with respect to iron from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('fem_gspspec', FloatType(), True), # Abundance of neutral iron [Fe/M] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt femGspspecNlines}
    StructField('fem_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of neutral iron [Fe/M] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('fem_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of neutral iron [Fe/M] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('fem_gspspec_nlines', IntegerType(), True), # Number of lines used for [Fe/M] abundance estimation
    StructField('fem_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Fe/M] abundance using N lines of the element, given in {\tt femGspspecNlines}
    StructField('sife_gspspec', FloatType(), True), # Abundance of Silicon [Si/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt sifeGspspecNlines}
    StructField('sife_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of silicon [Si/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations 
    StructField('sife_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of silicon [Si/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('sife_gspspec_nlines', IntegerType(), True), # Number of lines used for [Si/Fe] abundance estimation
    StructField('sife_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Si/Fe] abundance using N lines of the element, given in {\tt sifeGspspecNlines}
    StructField('cafe_gspspec', FloatType(), True), # Abundance of Calcium [Ca/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt cafeGspspecNlines}
    StructField('cafe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Calcium [Ca/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('cafe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Calcium [Ca/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('cafe_gspspec_nlines', IntegerType(), True), # Number of lines used for [Ca/Fe] abundance estimation
    StructField('cafe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Ca/Fe] abundance using N lines of the element, given in {\tt cafeGspspecNlines}
    StructField('tife_gspspec', FloatType(), True), # Abundance of Titanium [Ti/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt tifeGspspecNlines}  
    StructField('tife_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Titanium [Ti/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('tife_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Titanium [Ti/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('tife_gspspec_nlines', IntegerType(), True), # Number of lines used for [Ti/Fe] abundance estimation
    StructField('tife_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Ti/Fe] abundance using N lines of the element, given in {\tt tifeGspspecNlines}
    StructField('mgfe_gspspec', FloatType(), True), # Abundance of Magnesium [Mg/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt mgfeGspspecNlines}
    StructField('mgfe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Magnesium [Mg/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('mgfe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Magnesium [Mg/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations 
    StructField('mgfe_gspspec_nlines', IntegerType(), True), # Number of lines used for [Mg/Fe] abundance estimation
    StructField('mgfe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Mg/Fe] abundance using N lines of the element, given in {\tt mgfeGspspecNlines}
    StructField('ndfe_gspspec', FloatType(), True), # Abundance of neodymium [Nd/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt ndfeGspspecNlines}
    StructField('ndfe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of neodymium [Nd/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('ndfe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of neodymium [Nd/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('ndfe_gspspec_nlines', IntegerType(), True), # Number of lines used for [Nd/Fe] abundance estimation
    StructField('ndfe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Nd/Fe] abundance using N lines of the element, given in {\tt ndfeGspspecNlines}
    StructField('feiim_gspspec', FloatType(), True), # Abundance of ionised iron [FeII/M] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt feiimGspspecNlines}
    StructField('feiim_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of ionised iron [FeII/M] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('feiim_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of ionised iron [FeII/M] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('feiim_gspspec_nlines', IntegerType(), True), # Number of lines used for [FeII/M] abundance estimation
    StructField('feiim_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [FeII/M] abundance using N lines of the element, given in {\tt feiimGspspecNlines}
    StructField('sfe_gspspec', FloatType(), True), # Abundance of Sulphur [S/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt sfeGspspecNlines}
    StructField('sfe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Sulphur [S/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('sfe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Sulphur [S/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('sfe_gspspec_nlines', IntegerType(), True), # Number of lines used for [S/Fe] abundance estimation
    StructField('sfe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [S/Fe] abundance using N lines of the element, given in {\tt sfeGspspecNlines}
    StructField('zrfe_gspspec', FloatType(), True), # Abundance of Zirconium [Zr/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt zrfeGspspecNlines}
    StructField('zrfe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Zirconium [Zr/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('zrfe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Zirconium [Zr/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('zrfe_gspspec_nlines', IntegerType(), True), # Number of lines used for [Zr/Fe] abundance estimation
    StructField('zrfe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Zr/Fe] abundance using N lines of the element, given in {\tt zrfeGspspecNlines}
    StructField('nfe_gspspec', FloatType(), True), # Abundance of Nitrogen [N/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt nfeGspspecNlines}
    StructField('nfe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Nitrogen [N/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('nfe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Nitrogen [N/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('nfe_gspspec_nlines', IntegerType(), True), # Number of lines used for [N/Fe] abundance estimation
    StructField('nfe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [N/Fe] abundance using N lines of the element, given in {\tt nfeGspspecNlines}
    StructField('crfe_gspspec', FloatType(), True), # Abundance of Chromium [Cr/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt crfeGspspecNlines}
    StructField('crfe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Chromium [Cr/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('crfe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Chromium [Cr/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('crfe_gspspec_nlines', IntegerType(), True), # Number of lines used for [Cr/Fe] abundance estimation
    StructField('crfe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Cr/Fe] abundance using N lines of the element, given in {\tt crfeGspspecNlines}
    StructField('cefe_gspspec', FloatType(), True), # Abundance of Cerium [Ce/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt cefeGspspecNlines}
    StructField('cefe_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Cerium [Ce/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('cefe_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Cerium [Ce/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('cefe_gspspec_nlines', IntegerType(), True), # Number of lines used for [Ce/Fe] abundance estimation
    StructField('cefe_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Ce/Fe] abundance using N lines of the element, given in {\tt cefeGspspecNlines}
    StructField('nife_gspspec', FloatType(), True), # Abundance of Nickel [Ni/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations, applied to the individual N lines of the element, given in {\tt nifeGspspecNlines}
    StructField('nife_gspspec_lower', FloatType(), True), # 16th percentile of the abundance of Nickel [Ni/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('nife_gspspec_upper', FloatType(), True), # 84th percentile of the abundance of Nickel [Ni/Fe] from GSP-Spec MatisseGauguin using RVS spectra and Monte Carlo realisations
    StructField('nife_gspspec_nlines', IntegerType(), True), # Number of lines used for [Ni/Fe] abundance estimation
    StructField('nife_gspspec_linescatter', FloatType(), True), # Uncertainty estimation of [Ni/Fe] abundance using N lines of the element, given in {\tt nifeGspspecNlines}
    StructField('cn0ew_gspspec', FloatType(), True), # Equivalent witdh of cyanogen absorption line, derived from RVS spectra
    StructField('cn0ew_gspspec_uncertainty', FloatType(), True), # Uncertainty of equivalent witdh of cyanogen absorption line, derived from RVS spectra
    StructField('cn0_gspspec_centralline', FloatType(), True), # Central wavelength of cyanogen line, derived from RVS spectra using DIB algorithm
    StructField('cn0_gspspec_width', FloatType(), True), # Width of cyoanogen line, derived from RVS spectra using DIB algorithm
    StructField('dib_gspspec_lambda', FloatType(), True), # DIB central wavelength from GSP-Spec MatisseGauguin using RVS spectra 
    StructField('dib_gspspec_lambda_uncertainty', FloatType(), True), # Uncertainty on DIB central wavelength from GSP-Spec MatisseGauguin using RVS spectra
    StructField('dibew_gspspec', FloatType(), True), # Equivalent width of the DIB from GSP-Spec MatisseGauguin using RVS spectra
    StructField('dibew_gspspec_uncertainty', FloatType(), True), # Global uncertainty on DIB equivalent width value using DIB algorithm 
    StructField('dibewnoise_gspspec_uncertainty', FloatType(), True), # Uncertainty on DIB equivalent width value occuring from noise part 
    StructField('dibp0_gspspec', FloatType(), True), # Depth ($p_0$ parameter) of the DIB derived from a Gaussian model fit
    StructField('dibp2_gspspec', FloatType(), True), # Width ($p_2$ parameter) of the DIB derived from a Gaussian model fit
    StructField('dibp2_gspspec_uncertainty', FloatType(), True), # Uncertainty on the {\tt dibp2Gspspec} parameter 
    StructField('dibqf_gspspec', IntegerType(), True), # Quality flag of the DIB computation
    StructField('flags_gspspec', StringType(), True), # Catalogue flags for GSP-Spec MatisseGauguin 
    StructField('logchisq_gspspec', FloatType(), True), # Logarithm of the goodness-of-fit for the GSP-Spec MatisseGauguin parameters
    StructField('ew_espels_halpha', FloatType(), True), # Halpha pseudo-equivalent width from ESP-ELS
    StructField('ew_espels_halpha_uncertainty', FloatType(), True), # Uncertainty of the Halpha pseudo-equivalent width from ESP-ELS
    StructField('ew_espels_halpha_flag', StringType(), True), # Quality flag of the Halpha pseudo-equivalent width from ESP-ELS
    StructField('ew_espels_halpha_model', FloatType(), True), # Halpha pseudo-equivalent width from ESP-ELS measured on the synthetic spectrum
    StructField('classlabel_espels', StringType(), True), # Adopted ELS class label from ESP-ELS
    StructField('classlabel_espels_flag', StringType(), True), # Quality flag of the adopted ELS class label from ESP-ELS
    StructField('classprob_espels_wcstar', FloatType(), True), # Probability from ESP-ELS of being a Wolf-Rayet star of type WC
    StructField('classprob_espels_wnstar', FloatType(), True), # Probability from ESP-ELS of being a Wolf-Rayet star of type WN
    StructField('classprob_espels_bestar', FloatType(), True), # Probability from ESP-ELS of being a Be Star
    StructField('classprob_espels_ttauristar', FloatType(), True), # Probability from ESP-ELS of being a T Tauri Star
    StructField('classprob_espels_herbigstar', FloatType(), True), # Probability from ESP-ELS of being a Herbig Ae/Be Star
    StructField('classprob_espels_dmestar', FloatType(), True), # Probability from ESP-ELS of being an active M dwarf Star
    StructField('classprob_espels_pne', FloatType(), True), # Probability from ESP-ELS of being a planetary nebula
    StructField('azero_esphs', FloatType(), True), # Monochromatic interstellar extinction, A$_\mathrm{0}$, from ESP-HS
    StructField('azero_esphs_uncertainty', FloatType(), True), # Uncertainty at a 68% confidence level on A$_\mathrm{0}$ from ESP-HS
    StructField('ag_esphs', FloatType(), True), # Intersterstellar extinction in G band from ESP-HS
    StructField('ag_esphs_uncertainty', FloatType(), True), # Uncertainty on $A_{\rm G}$ from ESP-HS
    StructField('ebpminrp_esphs', FloatType(), True), # Reddening $E(G_{\rm BP} - G_{\rm RP})$ from ESP-HS
    StructField('ebpminrp_esphs_uncertainty', FloatType(), True), # Uncertainty on $E(G_{\rm BP} - G_{\rm RP})$ from ESP-HS
    StructField('teff_esphs', FloatType(), True), # Effective temperature from ESP-HS
    StructField('teff_esphs_uncertainty', FloatType(), True), # Uncertainty at a 68% confidence level on the effective temperature from ESP-HS
    StructField('logg_esphs', FloatType(), True), # Surface gravity from ESP-HS
    StructField('logg_esphs_uncertainty', FloatType(), True), # Uncertainty at a 68% confidence level on the surface gravity from ESP-HS
    StructField('vsini_esphs', FloatType(), True), # Projected rotational velocity from ESP-HS
    StructField('vsini_esphs_uncertainty', FloatType(), True), # Uncertainty on the projected rotational velocity from ESP-HS
    StructField('flags_esphs', StringType(), True), # Quality flag of the ESP-HS parametrisation
    StructField('spectraltype_esphs', StringType(), True), # Spectral type from ESP-ELS
    StructField('activityindex_espcs', FloatType(), True), # Chromospheric activity index from ESP-CS, measured on the calcium triplet using RVS spectra
    StructField('activityindex_espcs_uncertainty', FloatType(), True), # Uncertainty in the chromospheric activity index from ESP-CS
    StructField('activityindex_espcs_input', StringType(), True), # Source of input stellar parameters for the computation of the activity index by ESP-CS
    StructField('teff_espucd', FloatType(), True), # Effective temperature estimate from ESP-UCD based on the RP spectrum
    StructField('teff_espucd_uncertainty', FloatType(), True), # Uncertainty of the effective temperature estimate produced by ESP-UCD 
    StructField('flags_espucd', StringType(), True), # Quality flags of the ESP-UCD parameter estimates
    StructField('radius_flame', FloatType(), True), # Radius of the star from FLAME using {\tt teffGspphot} and {\tt lumFlame}
    StructField('radius_flame_lower', FloatType(), True), # Lower confidence level (16%) of {\tt radiusFlame}
    StructField('radius_flame_upper', FloatType(), True), # Upper confidence level (84%) of {\tt radiusFlame}
    StructField('lum_flame', FloatType(), True), # Luminosity of the star from FLAME using G band magnitude, extinction ({\tt agGspphot}),  parallax or distance, and a bolometric correction {\tt bcFlame}
    StructField('lum_flame_lower', FloatType(), True), # Lower confidence level (16%) of {\tt lumFlame}
    StructField('lum_flame_upper', FloatType(), True), # Upper confidence level (84%) of {\tt lumFlame}
    StructField('mass_flame', FloatType(), True), # Mass of the star from FLAME using stellar models, {\tt lumFlame}, and {\tt teffGspphot}
    StructField('mass_flame_lower', FloatType(), True), # Lower confidence level (16%) of {\tt massFlame}
    StructField('mass_flame_upper', FloatType(), True), # Upper confidence level (84%) of {\tt massFlame}
    StructField('age_flame', FloatType(), True), # Age of the star from FLAME using stellar models, see {\tt massFlame} for details
    StructField('age_flame_lower', FloatType(), True), # Lower confidence level (16%) of {\tt ageFlame}
    StructField('age_flame_upper', FloatType(), True), # Upper confidence level (84%) of {\tt ageFlame} 
    StructField('flags_flame', StringType(), True), # Flags indicating quality and processing information from FLAME
    StructField('evolstage_flame', IntegerType(), True), # Evolutionary stage of the star from FLAME using stellar models, see {\tt massFlame} for details
    StructField('gravredshift_flame', FloatType(), True), # Gravitational redshift from FLAME using {\tt radiusFlame} and {\tt loggGspphot}
    StructField('gravredshift_flame_lower', FloatType(), True), # Lower confidence level (16%) of {\tt gravredshiftFlame}
    StructField('gravredshift_flame_upper', FloatType(), True), # Upper confidence level (84%) of {\tt gravredshiftFlame}
    StructField('bc_flame', FloatType(), True), # Bolometric correction used to derive {\tt lumFlame}
    StructField('mh_msc', FloatType(), True), # Metallicity of the source treated as a binary system from MSC using BP/RP spectra and parallax
    StructField('mh_msc_upper', FloatType(), True), # Upper confidence level (84%) of the metallicity from MSC using BP/RP spectra and parallax
    StructField('mh_msc_lower', FloatType(), True), # Lower confidence level (16%) of the metallicity from MSC using BP/RP spectra and parallax
    StructField('azero_msc', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm of the source treated as a binary system from MSC using BP/RP spectra and parallax
    StructField('azero_msc_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from MSC using BP/RP spectra and parallax
    StructField('azero_msc_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from MSC using BP/RP spectra and parallax
    StructField('distance_msc', FloatType(), True), # Distance from MSC using BP/RP spectra and parallax
    StructField('distance_msc_upper', FloatType(), True), # Upper confidence level (84%) of distance from MSC using BP/RP spectra and parallax
    StructField('distance_msc_lower', FloatType(), True), # Lower confidence level (16%) of distance from MSC using BP/RP spectra and parallax
    StructField('teff_msc1', FloatType(), True), # Effective temperature of the primary from MSC using BP/RP spectra and parallax
    StructField('teff_msc1_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature of the primary from MSC using BP/RP spectra and parallax
    StructField('teff_msc1_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature of the primary from MSC using BP/RP spectra and parallax
    StructField('teff_msc2', FloatType(), True), # Effective temperature of the secondary from MSC using BP/RP spectra and parallax
    StructField('teff_msc2_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature of the secondary from MSC using BP/RP spectra and parallax
    StructField('teff_msc2_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature of the secondary from MSC using BP/RP spectra and parallax
    StructField('logg_msc1', FloatType(), True), # Surface gravity of the primary from MSC using BP/RP spectra and parallax
    StructField('logg_msc1_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity of the primary from MSC using BP/RP spectra and parallax
    StructField('logg_msc1_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity of the primary from MSC using BP/RP spectra and parallax
    StructField('logg_msc2', FloatType(), True), # Surface gravity of the secondary from MSC using BP/RP spectra and parallax
    StructField('logg_msc2_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity of the secondary from MSC using BP/RP spectra and parallax
    StructField('logg_msc2_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity of the secondary from MSC using BP/RP spectra and parallax
    StructField('ag_msc', FloatType(), True), # Extinction in G band of the source treated as a binary system from MSC using BP/RP spectra and parallax
    StructField('ag_msc_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from MSC using BP/RP spectra and parallax
    StructField('ag_msc_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from MSC using BP/RP spectra and parallax
    StructField('logposterior_msc', FloatType(), True), # Goodness-of-fit score (normalised log-posterior) of MSC MCMC
    StructField('mcmcaccept_msc', FloatType(), True), # Mean MCMC acceptance rate of MSC MCMC
    StructField('mcmcdrift_msc', FloatType(), True), # Mean drift of the MSC MCMC chain in units of parameter standard deviation
    StructField('flags_msc', StringType(), True), # Flag indicating quality information from MSC
    StructField('neuron_oa_id', LongType(), True), # Identifier of the OA SOM map neuron that represents the source
    StructField('neuron_oa_dist', FloatType(), True), # Distance between the source XP spectra and the OA neuron XP prototype that represents the source
    StructField('neuron_oa_dist_percentile_rank', IntegerType(), True), # Percentile rank according to the distance distribution of the OA neuron that represents the source
    StructField('flags_oa', StringType(), True), # Flags indicating quality and processing information from OA
])
astrophysical_parameters_supp_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source Identifier
    StructField('libname_best_gspphot', StringType(), True), # Name of library that achieves the highest mean log-posterior in MCMC samples from GSP-Phot Aeneas
    StructField('teff_gspphot_marcs', FloatType(), True), # Effective temperature from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('teff_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('teff_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('logg_gspphot_marcs', FloatType(), True), # Surface gravity from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('logg_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('logg_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('mh_gspphot_marcs', FloatType(), True), # Iron abundance from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('mh_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('mh_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('distance_gspphot_marcs', FloatType(), True), # Distance from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('distance_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of distance from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('distance_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of distance from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('azero_gspphot_marcs', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('azero_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('azero_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('ag_gspphot_marcs', FloatType(), True), # Extinction in G band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('ag_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('ag_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('abp_gspphot_marcs', FloatType(), True), # Extinction in $G_{BP}$ band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('abp_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('abp_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('arp_gspphot_marcs', FloatType(), True), # Extinction in $G_{RP}$ band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('arp_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('arp_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('ebpminrp_gspphot_marcs', FloatType(), True), # Reddening $E(BP-RP)$ from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('ebpminrp_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of reddening  $E(BP-RP)$ from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('ebpminrp_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of reddening  $E(BP-RP)$ from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('mg_gspphot_marcs', FloatType(), True), # Absolute magnitude $M_G$ from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('mg_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('mg_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('radius_gspphot_marcs', FloatType(), True), # Radius from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('radius_gspphot_marcs_lower', FloatType(), True), # Lower confidence level (16%) of radius from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('radius_gspphot_marcs_upper', FloatType(), True), # Upper confidence level (84%) of radius from GSP-Phot Aeneas for MARCS library using BP/RP spectra
    StructField('logposterior_gspphot_marcs', FloatType(), True), # Goodness-of-fit score (mean log-posterior of MCMC) of GSP-Phot Aeneas MCMC for MARCS library
    StructField('mcmcaccept_gspphot_marcs', FloatType(), True), # MCMC acceptance rate of GSP-Phot Aeneas MCMC for MARCS library
    StructField('teff_gspphot_phoenix', FloatType(), True), # Effective temperature from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('teff_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('teff_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('logg_gspphot_phoenix', FloatType(), True), # Surface gravity from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('logg_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('logg_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('mh_gspphot_phoenix', FloatType(), True), # Iron abundance from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('mh_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('mh_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('distance_gspphot_phoenix', FloatType(), True), # Distance from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('distance_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of distance from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('distance_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of distance from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('azero_gspphot_phoenix', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('azero_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('azero_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('ag_gspphot_phoenix', FloatType(), True), # Extinction in G band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('ag_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('ag_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('abp_gspphot_phoenix', FloatType(), True), # Extinction in $G_{BP}$ band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('abp_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('abp_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('arp_gspphot_phoenix', FloatType(), True), # Extinction in $G_{RP}$ band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('arp_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('arp_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('ebpminrp_gspphot_phoenix', FloatType(), True), # Reddening $E(BP-RP)$ from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('ebpminrp_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of reddening  $E(BP-RP)$ from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('ebpminrp_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of reddening  $E(BP-RP)$ from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('mg_gspphot_phoenix', FloatType(), True), # Absolute magnitude $M_G$ from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('mg_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('mg_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('radius_gspphot_phoenix', FloatType(), True), # Radius from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('radius_gspphot_phoenix_lower', FloatType(), True), # Lower confidence level (16%) of radius from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('radius_gspphot_phoenix_upper', FloatType(), True), # Upper confidence level (84%) of radius from GSP-Phot Aeneas for PHOENIX library using BP/RP spectra
    StructField('logposterior_gspphot_phoenix', FloatType(), True), # Goodness-of-fit score (mean log-posterior of MCMC) of GSP-Phot Aeneas MCMC for PHOENIX library
    StructField('mcmcaccept_gspphot_phoenix', FloatType(), True), # MCMC acceptance rate of GSP-Phot Aeneas MCMC for PHOENIX library
    StructField('teff_gspphot_ob', FloatType(), True), # Effective temperature from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('teff_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('teff_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('logg_gspphot_ob', FloatType(), True), # Surface gravity from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('logg_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('logg_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('mh_gspphot_ob', FloatType(), True), # Iron abundance from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('mh_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('mh_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('distance_gspphot_ob', FloatType(), True), # Distance from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('distance_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of distance from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('distance_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of distance from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('azero_gspphot_ob', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('azero_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('azero_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('ag_gspphot_ob', FloatType(), True), # Extinction in G band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('ag_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('ag_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('abp_gspphot_ob', FloatType(), True), # Extinction in $G_{BP}$ band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('abp_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('abp_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('arp_gspphot_ob', FloatType(), True), # Extinction in $G_{RP}$ band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('arp_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('arp_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('ebpminrp_gspphot_ob', FloatType(), True), # Reddening E(BP-RP) from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('ebpminrp_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of reddening  E(BP-RP) from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('ebpminrp_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of reddening  E(BP-RP) from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('mg_gspphot_ob', FloatType(), True), # Absolute magnitude $M_G$ from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('mg_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('mg_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('radius_gspphot_ob', FloatType(), True), # Radius from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('radius_gspphot_ob_lower', FloatType(), True), # Lower confidence level (16%) of radius from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('radius_gspphot_ob_upper', FloatType(), True), # Upper confidence level (84%) of radius from GSP-Phot Aeneas for OB library using BP/RP spectra
    StructField('logposterior_gspphot_ob', FloatType(), True), # Goodness-of-fit score (mean log-posterior of MCMC) of GSP-Phot Aeneas MCMC for OB library
    StructField('mcmcaccept_gspphot_ob', FloatType(), True), # MCMC acceptance rate of GSP-Phot Aeneas MCMC for OB library
    StructField('teff_gspphot_a', FloatType(), True), # Effective temperature from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('teff_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('teff_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('logg_gspphot_a', FloatType(), True), # Surface gravity from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('logg_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('logg_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('mh_gspphot_a', FloatType(), True), # Iron abundance from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('mh_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('mh_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('distance_gspphot_a', FloatType(), True), # Distance from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('distance_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of distance from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('distance_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of distance from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('azero_gspphot_a', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('azero_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('azero_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('ag_gspphot_a', FloatType(), True), # Extinction in G band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('ag_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('ag_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('abp_gspphot_a', FloatType(), True), # Extinction in $G_{BP}$ band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('abp_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('abp_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{BP}$ band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('arp_gspphot_a', FloatType(), True), # Extinction in $G_{RP}$ band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('arp_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('arp_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of extinction in $G_{RP}$ band from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('ebpminrp_gspphot_a', FloatType(), True), # Reddening $E(BP-RP)$ from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('ebpminrp_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of reddening  $E(BP-RP)$ from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('ebpminrp_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of reddening  $E(BP-RP)$ from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('mg_gspphot_a', FloatType(), True), # Absolute magnitude $M_G$ from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('mg_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('mg_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of absolute magnitude $M_G$ from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('radius_gspphot_a', FloatType(), True), # Radius from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('radius_gspphot_a_lower', FloatType(), True), # Lower confidence level (16%) of radius from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('radius_gspphot_a_upper', FloatType(), True), # Upper confidence level (84%) of radius from GSP-Phot Aeneas for A library using BP/RP spectra
    StructField('logposterior_gspphot_a', FloatType(), True), # Goodness-of-fit score (mean log-posterior of MCMC) of GSP-Phot Aeneas MCMC for A library
    StructField('mcmcaccept_gspphot_a', FloatType(), True), # MCMC acceptance rate of GSP-Phot Aeneas MCMC for A library
    StructField('teff_gspspec_ann', FloatType(), True), # Effective temperature from GSP-Spec ANN using RVS spectra and Monte Carlo realisations 
    StructField('teff_gspspec_ann_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('teff_gspspec_ann_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('logg_gspspec_ann', FloatType(), True), # Surface gravity from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('logg_gspspec_ann_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Spec ANN using RVS spectra and Monte Carlo realisations 
    StructField('logg_gspspec_ann_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Spec ANN using RVS spectra and Monte Carlo realisations 
    StructField('mh_gspspec_ann', FloatType(), True), # Global metallicity from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('mh_gspspec_ann_lower', FloatType(), True), # Lower confidence level (16%) of global metallicity from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('mh_gspspec_ann_upper', FloatType(), True), # Upper confidence level (84%) of global metallicity  from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('alphafe_gspspec_ann', FloatType(), True), # Abundance of alpha-elements with respect to iron from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('alphafe_gspspec_ann_lower', FloatType(), True), # Lower confidence level (16%) of alpha-elements with respect to iron from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('alphafe_gspspec_ann_upper', FloatType(), True), # Upper confidence level (84%) of alpha-elements with respect to iron from GSP-Spec ANN using RVS spectra and Monte Carlo realisations
    StructField('logchisq_gspspec_ann', FloatType(), True), # Logarithm of the goodness-of-fit for the GSP-Spec ANN parameters
    StructField('flags_gspspec_ann', StringType(), True), # Catalogue flags for GSP-Spec ANN
    StructField('radius_flame_spec', FloatType(), True), # Radius of the star from FLAME using {\tt teffGspspec} and {\tt lumFlameSpec}
    StructField('radius_flame_spec_lower', FloatType(), True), # Lower confidence level (16%) of {\tt radiusFlameSpec}
    StructField('radius_flame_spec_upper', FloatType(), True), # Upper confidence level (84%) of {\tt radiusFlameSpec}
    StructField('lum_flame_spec', FloatType(), True), # Luminosity of the star from FLAME using G band magnitude, extinction ({\tt agGspphot}),  parallax and a bolometric correction {\tt bcFlameSpec}
    StructField('lum_flame_spec_lower', FloatType(), True), # Lower confidence level (16%) of {\tt lumFlameSpec}
    StructField('lum_flame_spec_upper', FloatType(), True), # Upper confidence level (84%) of {\tt lumFlameSpec} 
    StructField('mass_flame_spec', FloatType(), True), # Mass of the star from FLAME using stellar models,  {\tt lumFlameSpec} and {\tt teffGspspec}
    StructField('mass_flame_spec_lower', FloatType(), True), # Lower confidence level (16%) of {\tt massFlameSpec}
    StructField('mass_flame_spec_upper', FloatType(), True), # Upper confidence level (84%) of {\tt massFlameSpec}
    StructField('age_flame_spec', FloatType(), True), # Age of the star from FLAME using stellar models, see {\tt massFlameSpec} for details
    StructField('age_flame_spec_lower', FloatType(), True), # Lower confidence level (16%) of {\tt ageFlameSpec}
    StructField('age_flame_spec_upper', FloatType(), True), # Upper confidence level (84%) of {\tt ageFlameSpec}
    StructField('flags_flame_spec', StringType(), True), # Flag indicating quality of parameters from FLAME using GSP-Spec parameters
    StructField('evolstage_flame_spec', IntegerType(), True), # Evolutionary stage of the star from FLAME using stellar models, see {\tt massFlameSpec} for details
    StructField('gravredshift_flame_spec', FloatType(), True), # Gravitational redshift from FLAME using GSP-Spec parameters
    StructField('gravredshift_flame_spec_lower', FloatType(), True), # Lower confidence interval of {\tt gravredshiftFlameSpec}
    StructField('gravredshift_flame_spec_upper', FloatType(), True), # Upper confidence interval of {\tt gravredshiftFlameSpec}
    StructField('bc_flame_spec', FloatType(), True), # Bolometric correction applied to derive {\tt lumFlameSpec} using GSP-Spec parameters
])
epoch_photometry_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('n_transits', ShortType(), True), # Number of Gaia transits
    StructField('transit_id', ArrayType(LongType()), True), # Transit unique identifier
    StructField('g_transit_time', ArrayType(DoubleType()), True), # Transit averaged G band observing time
    StructField('g_transit_flux', ArrayType(DoubleType()), True), # Transit averaged G band flux
    StructField('g_transit_flux_error', ArrayType(DoubleType()), True), # Transit averaged G band flux error
    StructField('g_transit_flux_over_error', ArrayType(FloatType()), True), # Transit averaged G band flux divided by its error
    StructField('g_transit_mag', ArrayType(DoubleType()), True), # Transit averaged G band Vega magnitude
    StructField('g_transit_n_obs', ArrayType(ByteType()), True), # Number of CCD observations contributing to transit averaged G band flux
    StructField('bp_obs_time', ArrayType(DoubleType()), True), # BP CCD transit observing time
    StructField('bp_flux', ArrayType(DoubleType()), True), # BP band flux
    StructField('bp_flux_error', ArrayType(DoubleType()), True), # BP band flux error
    StructField('bp_flux_over_error', ArrayType(FloatType()), True), # BP band flux divided by its error
    StructField('bp_mag', ArrayType(DoubleType()), True), # BP band Vega magnitude
    StructField('rp_obs_time', ArrayType(DoubleType()), True), # RP CCD transit observing time
    StructField('rp_flux', ArrayType(DoubleType()), True), # RP band flux
    StructField('rp_flux_error', ArrayType(DoubleType()), True), # RP band flux error
    StructField('rp_flux_over_error', ArrayType(FloatType()), True), # RP band flux divided by its error
    StructField('rp_mag', ArrayType(DoubleType()), True), # RP band Vega magnitude
    StructField('photometry_flag_noisy_data', ArrayType(BooleanType()), True), # G band flux scatter larger than expected by photometry processing (all CCDs considered)
    StructField('photometry_flag_sm_unavailable', ArrayType(BooleanType()), True), # SM transit unavailable by photometry processing
    StructField('photometry_flag_af1_unavailable', ArrayType(BooleanType()), True), # AF1 transit unavailable by photometry processing
    StructField('photometry_flag_af2_unavailable', ArrayType(BooleanType()), True), # AF2 transit unavailable by photometry processing
    StructField('photometry_flag_af3_unavailable', ArrayType(BooleanType()), True), # AF3 transit unavailable by photometry processing
    StructField('photometry_flag_af4_unavailable', ArrayType(BooleanType()), True), # AF4 transit unavailable by photometry processing
    StructField('photometry_flag_af5_unavailable', ArrayType(BooleanType()), True), # AF5 transit unavailable by photometry processing
    StructField('photometry_flag_af6_unavailable', ArrayType(BooleanType()), True), # AF6 transit unavailable by photometry processing
    StructField('photometry_flag_af7_unavailable', ArrayType(BooleanType()), True), # AF7 transit unavailable by photometry processing
    StructField('photometry_flag_af8_unavailable', ArrayType(BooleanType()), True), # AF8 transit unavailable by photometry processing
    StructField('photometry_flag_af9_unavailable', ArrayType(BooleanType()), True), # AF9 transit unavailable by photometry processing
    StructField('photometry_flag_bp_unavailable', ArrayType(BooleanType()), True), # BP transit unavailable by photometry processing
    StructField('photometry_flag_rp_unavailable', ArrayType(BooleanType()), True), # RP transit unavailable by photometry processing
    StructField('photometry_flag_sm_reject', ArrayType(BooleanType()), True), # SM transit rejected by photometry processing
    StructField('photometry_flag_af1_reject', ArrayType(BooleanType()), True), # AF1 transit rejected by photometry processing
    StructField('photometry_flag_af2_reject', ArrayType(BooleanType()), True), # AF2 transit rejected by photometry processing
    StructField('photometry_flag_af3_reject', ArrayType(BooleanType()), True), # AF3 transit rejected by photometry processing
    StructField('photometry_flag_af4_reject', ArrayType(BooleanType()), True), # AF4 transit rejected by photometry processing
    StructField('photometry_flag_af5_reject', ArrayType(BooleanType()), True), # AF5 transit rejected by photometry processing
    StructField('photometry_flag_af6_reject', ArrayType(BooleanType()), True), # AF6 transit rejected by photometry processing
    StructField('photometry_flag_af7_reject', ArrayType(BooleanType()), True), # AF7 transit rejected by photometry processing
    StructField('photometry_flag_af8_reject', ArrayType(BooleanType()), True), # AF8 transit rejected by photometry processing
    StructField('photometry_flag_af9_reject', ArrayType(BooleanType()), True), # AF9 transit rejected by photometry processing
    StructField('photometry_flag_bp_reject', ArrayType(BooleanType()), True), # BP transit rejected by photometry processing
    StructField('photometry_flag_rp_reject', ArrayType(BooleanType()), True), # RP transit rejected by photometry processing
    StructField('variability_flag_g_reject', ArrayType(BooleanType()), True), # Average G transit photometry rejected by variability processing
    StructField('variability_flag_bp_reject', ArrayType(BooleanType()), True), # BP transit photometry rejected by variability processing
    StructField('variability_flag_rp_reject', ArrayType(BooleanType()), True), # RP transit photometry rejected by variability processing
])
gaia_source_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('designation', StringType(), True), # Unique source designation (unique across all Data Releases)
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('random_index', LongType(), True), # Random index for use when selecting subsets
    StructField('ref_epoch', DoubleType(), True), # Reference epoch
    StructField('ra', DoubleType(), True), # Right ascension
    StructField('ra_error', FloatType(), True), # Standard error of right ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('dec_error', FloatType(), True), # Standard error of declination
    StructField('parallax', DoubleType(), True), # Parallax
    StructField('parallax_error', FloatType(), True), # Standard error of parallax
    StructField('parallax_over_error', FloatType(), True), # Parallax divided by its standard error
    StructField('pm', FloatType(), True), # Total proper motion
    StructField('pmra', DoubleType(), True), # Proper motion in right ascension direction
    StructField('pmra_error', FloatType(), True), # Standard error of proper motion in right ascension direction
    StructField('pmdec', DoubleType(), True), # Proper motion in declination direction
    StructField('pmdec_error', FloatType(), True), # Standard error of proper motion in declination direction
    StructField('ra_dec_corr', FloatType(), True), # Correlation between right ascension and declination
    StructField('ra_parallax_corr', FloatType(), True), # Correlation between right ascension and parallax		
    StructField('ra_pmra_corr', FloatType(), True), # Correlation between right ascension and proper motion in right ascension
    StructField('ra_pmdec_corr', FloatType(), True), # Correlation between right ascension and proper motion in declination
    StructField('dec_parallax_corr', FloatType(), True), # Correlation between declination and parallax
    StructField('dec_pmra_corr', FloatType(), True), # Correlation between declination and proper motion in right ascension
    StructField('dec_pmdec_corr', FloatType(), True), # Correlation between declination and proper motion in declination
    StructField('parallax_pmra_corr', FloatType(), True), # Correlation between parallax and proper motion in right ascension
    StructField('parallax_pmdec_corr', FloatType(), True), # Correlation between parallax and proper motion in declination
    StructField('pmra_pmdec_corr', FloatType(), True), # Correlation between proper motion in right ascension and proper motion in declination
    StructField('astrometric_n_obs_al', ShortType(), True), # Total number of observations in the along-scan (AL) direction
    StructField('astrometric_n_obs_ac', ShortType(), True), # Total number of observations in the across-scan (AC) direction
    StructField('astrometric_n_good_obs_al', ShortType(), True), # Number of good observations in the along-scan (AL) direction
    StructField('astrometric_n_bad_obs_al', ShortType(), True), # Number of bad observations in the along-scan (AL) direction
    StructField('astrometric_gof_al', FloatType(), True), # Goodness of fit statistic of model wrt along-scan observations
    StructField('astrometric_chi2_al', FloatType(), True), # AL chi-square value
    StructField('astrometric_excess_noise', FloatType(), True), # Excess noise of the source
    StructField('astrometric_excess_noise_sig', FloatType(), True), # Significance of excess noise
    StructField('astrometric_params_solved', ByteType(), True), # Which parameters have been solved for?
    StructField('astrometric_primary_flag', BooleanType(), True), # Primary or seconday
    StructField('nu_eff_used_in_astrometry', FloatType(), True), # Effective wavenumber of the source used in the astrometric solution
    StructField('pseudocolour', FloatType(), True), # Astrometrically estimated pseudocolour of the source
    StructField('pseudocolour_error', FloatType(), True), # Standard error of the pseudocolour of the source
    StructField('ra_pseudocolour_corr', FloatType(), True), # Correlation between right ascension and pseudocolour
    StructField('dec_pseudocolour_corr', FloatType(), True), # Correlation between declination and pseudocolour
    StructField('parallax_pseudocolour_corr', FloatType(), True), # Correlation between parallax and pseudocolour
    StructField('pmra_pseudocolour_corr', FloatType(), True), # Correlation between proper motion in right asension and pseudocolour
    StructField('pmdec_pseudocolour_corr', FloatType(), True), # Correlation between proper motion in declination and pseudocolour
    StructField('astrometric_matched_transits', ShortType(), True), # Matched FOV transits used in the AGIS solution
    StructField('visibility_periods_used', ShortType(), True), # Number of visibility periods used in Astrometric solution
    StructField('astrometric_sigma5d_max', FloatType(), True), # The longest semi-major axis of the 5-d error ellipsoid
    StructField('matched_transits', ShortType(), True), # The number of transits matched to this source
    StructField('new_matched_transits', ShortType(), True), # The number of transits newly incorporated into an existing source in the current cycle
    StructField('matched_transits_removed', ShortType(), True), # The number of transits removed from an existing source in the current cycle
    StructField('ipd_gof_harmonic_amplitude', FloatType(), True), # Amplitude of the IPD GoF versus position angle of scan
    StructField('ipd_gof_harmonic_phase', FloatType(), True), # Phase of the IPD GoF versus position angle of scan
    StructField('ipd_frac_multi_peak', ByteType(), True), # Percent of successful-IPD windows with more than one peak
    StructField('ipd_frac_odd_win', ByteType(), True), # Percent of transits with truncated windows or multiple gate
    StructField('ruwe', FloatType(), True), # Renormalised unit weight error
    StructField('scan_direction_strength_k1', FloatType(), True), # Degree of concentration of scan directions across the source
    StructField('scan_direction_strength_k2', FloatType(), True), # Degree of concentration of scan directions across the source
    StructField('scan_direction_strength_k3', FloatType(), True), # Degree of concentration of scan directions across the source
    StructField('scan_direction_strength_k4', FloatType(), True), # Degree of concentration of scan directions across the source
    StructField('scan_direction_mean_k1', FloatType(), True), # Mean position angle of scan directions across the source
    StructField('scan_direction_mean_k2', FloatType(), True), # Mean position angle of scan directions across the source
    StructField('scan_direction_mean_k3', FloatType(), True), # Mean position angle of scan directions across the source
    StructField('scan_direction_mean_k4', FloatType(), True), # Mean position angle of scan directions across the source
    StructField('duplicated_source', BooleanType(), True), # Source with multiple source identifiers
    StructField('phot_g_n_obs', ShortType(), True), # Number of observations contributing to G photometry
    StructField('phot_g_mean_flux', DoubleType(), True), # G-band mean flux
    StructField('phot_g_mean_flux_error', FloatType(), True), # Error on G-band mean flux
    StructField('phot_g_mean_flux_over_error', FloatType(), True), # G-band mean flux divided by its error
    StructField('phot_g_mean_mag', FloatType(), True), # G-band mean magnitude
    StructField('phot_bp_n_obs', ShortType(), True), # Number of observations contributing to BP photometry
    StructField('phot_bp_mean_flux', DoubleType(), True), # Integrated BP mean flux
    StructField('phot_bp_mean_flux_error', FloatType(), True), # Error on the integrated BP mean flux
    StructField('phot_bp_mean_flux_over_error', FloatType(), True), # Integrated BP mean flux divided by its error
    StructField('phot_bp_mean_mag', FloatType(), True), # Integrated BP mean magnitude
    StructField('phot_rp_n_obs', ShortType(), True), # Number of observations contributing to RP photometry
    StructField('phot_rp_mean_flux', DoubleType(), True), # Integrated RP mean flux
    StructField('phot_rp_mean_flux_error', FloatType(), True), # Error on the integrated RP mean flux
    StructField('phot_rp_mean_flux_over_error', FloatType(), True), # Integrated RP mean flux divided by its error
    StructField('phot_rp_mean_mag', FloatType(), True), # Integrated RP mean magnitude
    StructField('phot_bp_rp_excess_factor', FloatType(), True), # BP/RP excess factor
    StructField('phot_bp_n_contaminated_transits', ShortType(), True), # Number of BP contaminated transits
    StructField('phot_bp_n_blended_transits', ShortType(), True), # Number of BP blended transits
    StructField('phot_rp_n_contaminated_transits', ShortType(), True), # Number of RP contaminated transits
    StructField('phot_rp_n_blended_transits', ShortType(), True), # Number of RP blended transits
    StructField('phot_proc_mode', ByteType(), True), # Photometry processing mode
    StructField('bp_rp', FloatType(), True), # BP - RP colour
    StructField('bp_g', FloatType(), True), # BP - G colour
    StructField('g_rp', FloatType(), True), # G - RP colour
    StructField('radial_velocity', FloatType(), True), # Radial velocity 
    StructField('radial_velocity_error', FloatType(), True), # Radial velocity error 
    StructField('rv_method_used', ByteType(), True), # Method used to obtain the radial velocity
    StructField('rv_nb_transits', ShortType(), True), # Number of transits used to compute the radial velocity 
    StructField('rv_nb_deblended_transits', ShortType(), True), # Number of valid transits that have undergone deblending
    StructField('rv_visibility_periods_used', ShortType(), True), # Number of visibility periods used to estimate the radial velocity
    StructField('rv_expected_sig_to_noise', FloatType(), True), # Expected signal to noise ratio in the combination of the spectra used to obtain the radial velocity
    StructField('rv_renormalised_gof', FloatType(), True), # Radial velocity renormalised goodness of fit
    StructField('rv_chisq_pvalue', FloatType(), True), # P-value for constancy based on a chi-squared criterion
    StructField('rv_time_duration', FloatType(), True), # Time coverage of the radial velocity time series
    StructField('rv_amplitude_robust', FloatType(), True), # Total amplitude in the radial velocity time series after outlier removal
    StructField('rv_template_teff', FloatType(), True), # Teff of the template used to compute the radial velocity 
    StructField('rv_template_logg', FloatType(), True), # Logg of the template used to compute the radial velocity 
    StructField('rv_template_fe_h', FloatType(), True), # [Fe/H] of the template used to compute the radial velocityy
    StructField('rv_atm_param_origin', ShortType(), True), # Origin of the atmospheric parameters associated to the template
    StructField('vbroad', FloatType(), True), # Spectral line broadening parameter
    StructField('vbroad_error', FloatType(), True), # Uncertainty on the spectral line broadening
    StructField('vbroad_nb_transits', ShortType(), True), # Number of transits used to compute vbroad
    StructField('grvs_mag', FloatType(), True), # Integrated Grvs magnitude
    StructField('grvs_mag_error', FloatType(), True), # Grvs magnitude uncertainty
    StructField('grvs_mag_nb_transits', ShortType(), True), # Number of transits used to compute Grvs
    StructField('rvs_spec_sig_to_noise', FloatType(), True), # Signal to noise ratio in the mean RVS spectrum
    StructField('phot_variable_flag', StringType(), True), # Photometric variability flag
    StructField('l', DoubleType(), True), # Galactic longitude
    StructField('b', DoubleType(), True), # Galactic latitude
    StructField('ecl_lon', DoubleType(), True), # Ecliptic longitude
    StructField('ecl_lat', DoubleType(), True), # Ecliptic latitude
    StructField('in_qso_candidates', BooleanType(), True), # Flag indicating the availability of additional information in the QsoCandidates table
    StructField('in_galaxy_candidates', BooleanType(), True), # Flag indicating the availability of additional information in the GalaxyCandidates table
    StructField('non_single_star', ShortType(), True), # Flag indicating the availability of additional information in the various Non-Single Star tables
    StructField('has_xp_continuous', BooleanType(), True), # Flag indicating the availability of mean BP/RP spectrum in continuous representation for this source
    StructField('has_xp_sampled', BooleanType(), True), # Flag indicating the availability of mean BP/RP spectrum in sampled form for this source
    StructField('has_rvs', BooleanType(), True), # Flag indicating the availability of mean RVS spectrum for this source
    StructField('has_epoch_photometry', BooleanType(), True), # Flag indicating the availability of epoch photometry for this source
    StructField('has_epoch_rv', BooleanType(), True), # Flag indicating the availability of epoch radial velocity for this source
    StructField('has_mcmc_gspphot', BooleanType(), True), # Flag indicating the availability of GSP-Phot MCMC samples for this source
    StructField('has_mcmc_msc', BooleanType(), True), # Flag indicating the availability of MSC MCMC samples for this source
    StructField('in_andromeda_survey', BooleanType(), True), # Flag indicating that the source is present in the Gaia Andromeda Photometric Survey (GAPS)
    StructField('classprob_dsc_combmod_quasar', FloatType(), True), # Probability from DSC-Combmod of being a quasar (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_galaxy', FloatType(), True), # Probability from DSC-Combmod of being a galaxy (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_star', FloatType(), True), # Probability from DSC-Combmod of being a single star (but not a white dwarf) (data used: BP/RP spectrum, photometry, astrometry)
    StructField('teff_gspphot', FloatType(), True), # Effective temperature from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('teff_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of effective temperature from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('teff_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of effective temperature from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logg_gspphot', FloatType(), True), # Surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logg_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('logg_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mh_gspphot', FloatType(), True), # Iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mh_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('mh_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('distance_gspphot', FloatType(), True), # Distance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('distance_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of distance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('distance_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of distance from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('azero_gspphot', FloatType(), True), # Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('azero_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('azero_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ag_gspphot', FloatType(), True), # Extinction in G band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ag_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of extinction in G band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ag_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of extinction in G band from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ebpminrp_gspphot', FloatType(), True), # Reddening $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ebpminrp_gspphot_lower', FloatType(), True), # Lower confidence level (16%) of reddening  $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('ebpminrp_gspphot_upper', FloatType(), True), # Upper confidence level (84%) of reddening  $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best library using BP/RP spectra
    StructField('libname_gspphot', StringType(), True), # Name of library that achieves the highest mean log-posterior in MCMC samples and was used to derive GSP-Phot parameters in this table
])
galaxy_candidates_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('vari_best_class_name', StringType(), True), # Name of best class, see table VariClassifierClassDefinition for details of the class
    StructField('vari_best_class_score', FloatType(), True), # Score of the best class
    StructField('classprob_dsc_combmod_galaxy', FloatType(), True), # Probability from DSC-Combmod of being a galaxy (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_quasar', FloatType(), True), # Probability from DSC-Combmod of being a quasar (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classlabel_dsc', StringType(), True), # Class assigned by DSC based on the probability from its Combmod classifier
    StructField('classlabel_dsc_joint', StringType(), True), # Class assigned by DSC based on the probability from its Specmod and Allosmod classifiers
    StructField('classlabel_oa', StringType(), True), # Class assigned by OA the neuron that represents the source
    StructField('redshift_ugc', FloatType(), True), # Redshift from UGC
    StructField('redshift_ugc_lower', FloatType(), True), # Redshift prediction lower limit from UGC
    StructField('redshift_ugc_upper', FloatType(), True), # Redshift prediction upper limit from UGC
    StructField('n_transits', IntegerType(), True), # Number of transits used for the morphological analysis
    StructField('posangle_sersic', DoubleType(), True), # Fitted position angle of the source for the Sersic Profile
    StructField('posangle_sersic_error', DoubleType(), True), # Error on the fitted position angle of the source for the Sersic Profile
    StructField('intensity_sersic', DoubleType(), True), # Fitted intensity of the source for the Sersic Profile
    StructField('intensity_sersic_error', DoubleType(), True), # Error on the fitted intensity of the source at effective radius radiusSersic
    StructField('radius_sersic', DoubleType(), True), # Fitted effective radius of the source for the Sersic Profile
    StructField('radius_sersic_error', DoubleType(), True), # Error on the fitted effective radius of the source for the Sersic Profile
    StructField('ellipticity_sersic', DoubleType(), True), # Fitted ellipticity of source for the Sersic Profile
    StructField('ellipticity_sersic_error', DoubleType(), True), # Error on the fitted ellipticity of the source for the Sersic Profile
    StructField('n_sersic', FloatType(), True), # Fitted Sersic Index for Sersic Profile
    StructField('n_sersic_error', FloatType(), True), # Error on the fitted Sersic Index for Sersic Profile
    StructField('l2_sersic', DoubleType(), True), # L2 norm for the Sersic Profile
    StructField('morph_params_corr_vec_sersic', ArrayType(DoubleType()), True), # Vector form of the upper triangle of the correlation matrix for the fitted parameters for the Sersic Profile
    StructField('flags_sersic', ByteType(), True), # Flag indicative of processing or scientific quality for the morphological parameters fitting for the Sersic Profile
    StructField('posangle_de_vaucouleurs', DoubleType(), True), # Fitted position angle of the source for the de Vaucouleurs Profile
    StructField('posangle_de_vaucouleurs_error', DoubleType(), True), # Error on the fitted position angle of the source for the de Vaucouleurs Profile
    StructField('intensity_de_vaucouleurs', DoubleType(), True), # Fitted intensity of the source for the de Vaucouleurs Profile
    StructField('intensity_de_vaucouleurs_error', DoubleType(), True), # Error on the fitted intensity of the bulge for the de Vaucouleurs Profile
    StructField('radius_de_vaucouleurs', DoubleType(), True), # Fitted effective radius of the source for de Vaucouleurs Profile
    StructField('radius_de_vaucouleurs_error', DoubleType(), True), # Error on the fitted effective radius of the source for the de Vaucouleurs Profile
    StructField('ellipticity_de_vaucouleurs', DoubleType(), True), # Fitted ellipticity of source for the de Vaucouleurs Profile
    StructField('ellipticity_de_vaucouleurs_error', DoubleType(), True), # Error on the fitted ellipticity of the source for the de Vaucouleurs Profile
    StructField('l2_de_vaucouleurs', DoubleType(), True), # L2 norm for the de Vaucouleurs Profile
    StructField('morph_params_corr_vec_de_vaucouleurs', ArrayType(DoubleType()), True), # Vector form of the upper triangle of the correlation matrix for the fitted parameters for the de Vaucouleurs Profile
    StructField('flags_de_vaucouleurs', ByteType(), True), # Flag indicative of processing or scientific quality for the morphological parameters fitting for the de Vaucouleurs Profile
    StructField('source_selection_flags', IntegerType(), True), # Bit indicative of whether the input data from a given module met the source list eligibility criteria for the source of interest
])
galaxy_catalogue_name_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('catalogue_id', ByteType(), False), # The unique identifier for the catalogue(s) used to select the sources in the morphological analysis
])
mcmc_samples_gsp_phot_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('nsamples', ShortType(), True), # Number of samples in the chain from GSP-Phot
    StructField('teff', ArrayType(FloatType()), True), # MCMC samples for $T_{\rm eff}$ from GSP-Phot
    StructField('azero', ArrayType(FloatType()), True), # MCMC samples for extinction $A_0$ from GSP-Phot
    StructField('logg', ArrayType(FloatType()), True), # MCMC samples for $\log g$ from GSP-Phot
    StructField('mh', ArrayType(FloatType()), True), # MCMC samples for the metallicity from GSP-Phot
    StructField('ag', ArrayType(FloatType()), True), # MCMC samples for extinction in G band from GSP-Phot
    StructField('mg', ArrayType(FloatType()), True), # MCMC samples for $M_{\rm G}$ from GSP-Phot
    StructField('distancepc', ArrayType(FloatType()), True), # MCMC samples for distance from GSP-Phot
    StructField('abp', ArrayType(FloatType()), True), # MCMC samples for extinction in $G_{\rm BP}$ band from GSP-Phot
    StructField('arp', ArrayType(FloatType()), True), # MCMC samples for extinction in $G_{\rm RP}$ band from GSP-Phot
    StructField('ebpminrp', ArrayType(FloatType()), True), # MCMC samples for reddening $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot
    StructField('log_pos', ArrayType(FloatType()), True), # MCMC samples for the log-posterior from GSP-Phot
    StructField('log_lik', ArrayType(FloatType()), True), # MCMC samples for the log-likelihood from GSP-Phot
    StructField('radius', ArrayType(FloatType()), True), # MCMC samples for stellar radius from GSP-Phot
])
mcmc_samples_msc_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('nsamples', ShortType(), True), # Number of samples in the chain from MSC
    StructField('teff1', ArrayType(FloatType()), True), # MCMC samples for $T_{\rm eff, 1}$ of primary from MSC
    StructField('teff2', ArrayType(FloatType()), True), # MCMC samples for $T_{\rm eff, 2}$ of secondary from MSC
    StructField('logg1', ArrayType(FloatType()), True), # MCMC samples for $\log g_1$ of primary from MSC
    StructField('logg2', ArrayType(FloatType()), True), # MCMC samples for $\log g_2$ of secondary from MSC
    StructField('azero', ArrayType(FloatType()), True), # MCMC samples for extinction $A_0$ from MSC
    StructField('mh', ArrayType(FloatType()), True), # MCMC samples for the metallicity from MSC
    StructField('distancepc', ArrayType(FloatType()), True), # MCMC samples for distance from MSC
    StructField('log_pos', ArrayType(FloatType()), True), # MCMC samples for the log-posterior from MSC
    StructField('log_lik', ArrayType(FloatType()), True), # MCMC samples for the log-likelihood from MSC
])
nss_acceleration_astro_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source Identifier
    StructField('nss_solution_type', StringType(), True), # NSS model adopted
    StructField('ra', DoubleType(), True), # Right ascension
    StructField('ra_error', FloatType(), True), # Standard error of right ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('dec_error', FloatType(), True), # Standard error of declination
    StructField('parallax', DoubleType(), True), # Parallax
    StructField('parallax_error', FloatType(), True), # Standard error of parallax
    StructField('pmra', DoubleType(), True), # Proper motion in right ascension direction
    StructField('pmra_error', FloatType(), True), # Standard error of proper motion in right ascension direction
    StructField('pmdec', DoubleType(), True), # Proper motion in declination direction
    StructField('pmdec_error', FloatType(), True), # Standard error of proper motion in declination direction
    StructField('accel_ra', DoubleType(), True), # Acceleration in RA
    StructField('accel_ra_error', FloatType(), True), # Standard error of Acceleration in RA
    StructField('accel_dec', DoubleType(), True), # Acceleration in DEC
    StructField('accel_dec_error', FloatType(), True), # Standard error of Acceleration in DEC
    StructField('deriv_accel_ra', DoubleType(), True), # Time derivative of the accel. in RA
    StructField('deriv_accel_ra_error', FloatType(), True), # Standard error of Time derivative of the acceleration in RA
    StructField('deriv_accel_dec', DoubleType(), True), # Time derivative of the accel. in DEC
    StructField('deriv_accel_dec_error', FloatType(), True), # Standard error of Time derivative of the acceleration in DEC
    StructField('astrometric_n_obs_al', IntegerType(), True), # Total astrometric CCD observations in AL considered
    StructField('astrometric_n_good_obs_al', IntegerType(), True), # Total astrometric CCD observations in AL actually used
    StructField('bit_index', LongType(), True), # Boolean mask for the fields above in the corrVec matrix 
    StructField('corr_vec', ArrayType(FloatType()), True), # Vector form of the upper triangle of the correlation matrix
    StructField('obj_func', FloatType(), True), # Value of the objective function at the solution
    StructField('goodness_of_fit', FloatType(), True), # Goodness of fit in the Hipparcos sense
    StructField('significance', FloatType(), True), # The significance of the solution (i.e. how worth keeping a model is)
    StructField('flags', LongType(), True), # Quality flag for the achieved NSS solution
])
nss_non_linear_spectro_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source Identifier
    StructField('nss_solution_type', StringType(), True), # NSS model adopted
    StructField('mean_velocity', DoubleType(), True), # Mean velocity
    StructField('mean_velocity_error', FloatType(), True), # Standard error of Mean velocity
    StructField('first_deriv_velocity', DoubleType(), True), # First order derivative of the velocity
    StructField('first_deriv_velocity_error', FloatType(), True), # Standard error of First order derivative of the velocity
    StructField('second_deriv_velocity', DoubleType(), True), # Second order derivative of the velocity
    StructField('second_deriv_velocity_error', FloatType(), True), # Standard error of Second order derivative of the velocity
    StructField('rv_n_obs_primary', IntegerType(), True), # Total number of radial velocities considered for the primary
    StructField('rv_n_good_obs_primary', IntegerType(), True), # Total number of radial velocities actually used for the primary
    StructField('bit_index', LongType(), True), # Boolean mask for the fields above in the corrVec matrix 
    StructField('corr_vec', ArrayType(FloatType()), True), # Vector form of the upper triangle of the correlation matrix
    StructField('obj_func', FloatType(), True), # Value of the objective function at the solution
    StructField('goodness_of_fit', FloatType(), True), # Goodness of fit in the Hipparcos sense
    StructField('flags', LongType(), True), # Quality flag for the achieved NSS solution
])
nss_two_body_orbit_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source Identifier
    StructField('nss_solution_type', StringType(), False), # NSS model adopted
    StructField('ra', DoubleType(), True), # Right ascension
    StructField('ra_error', FloatType(), True), # Standard error of right ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('dec_error', FloatType(), True), # Standard error of declination
    StructField('parallax', DoubleType(), True), # Parallax
    StructField('parallax_error', FloatType(), True), # Standard error of parallax
    StructField('pmra', DoubleType(), True), # Proper motion in right ascension direction
    StructField('pmra_error', FloatType(), True), # Standard error of proper motion in right ascension direction
    StructField('pmdec', DoubleType(), True), # Proper motion in declination direction
    StructField('pmdec_error', FloatType(), True), # Standard error of proper motion in declination direction
    StructField('a_thiele_innes', DoubleType(), True), # Thiele-Innes element A
    StructField('a_thiele_innes_error', FloatType(), True), # Standard error of Thiele-Innes element A
    StructField('b_thiele_innes', DoubleType(), True), # Thiele-Innes element B
    StructField('b_thiele_innes_error', FloatType(), True), # Standard error of Thiele-Innes element B
    StructField('f_thiele_innes', DoubleType(), True), # Thiele-Innes element F
    StructField('f_thiele_innes_error', FloatType(), True), # Standard error of Thiele-Innes element F
    StructField('g_thiele_innes', DoubleType(), True), # Thiele-Innes element G
    StructField('g_thiele_innes_error', FloatType(), True), # Standard error of Thiele-Innes element G
    StructField('c_thiele_innes', DoubleType(), True), # C element of Thiele-Innes 
    StructField('c_thiele_innes_error', FloatType(), True), # Standard error of C element of Thiele-Innes 
    StructField('h_thiele_innes', DoubleType(), True), # H element of Thiele-Innes 
    StructField('h_thiele_innes_error', FloatType(), True), # Standard error of H element of Thiele-Innes 
    StructField('period', DoubleType(), True), # Orbital Period
    StructField('period_error', FloatType(), True), # Standard error of Orbital Period
    StructField('t_periastron', DoubleType(), True), # Periastron epoch
    StructField('t_periastron_error', FloatType(), True), # Standard error of Periastron epoch
    StructField('eccentricity', DoubleType(), True), # eccentricity
    StructField('eccentricity_error', FloatType(), True), # Standard error of eccentricity
    StructField('center_of_mass_velocity', DoubleType(), True), # The velocity of the center of mass
    StructField('center_of_mass_velocity_error', FloatType(), True), # Standard error of The velocity of the center of mass
    StructField('semi_amplitude_primary', DoubleType(), True), # Semi-amplitude of the center of mass
    StructField('semi_amplitude_primary_error', FloatType(), True), # Standard error of Semi-amplitude of the center of mass
    StructField('semi_amplitude_secondary', DoubleType(), True), # The semiamplitude of the radial velocity curve for second component
    StructField('semi_amplitude_secondary_error', FloatType(), True), # Standard error of The semiamplitude of the radial velocity curve for second component
    StructField('mass_ratio', DoubleType(), True), # Mass ratio
    StructField('mass_ratio_error', FloatType(), True), # Standard error of Mass ratio
    StructField('fill_factor_primary', DoubleType(), True), # Fill factor of primary
    StructField('fill_factor_primary_error', FloatType(), True), # Standard error of Fill factor of primary
    StructField('fill_factor_secondary', DoubleType(), True), # Fill factor of secondary
    StructField('fill_factor_secondary_error', FloatType(), True), # Standard error of Fill factor of secondary
    StructField('inclination', DoubleType(), True), # Orbital inclination
    StructField('inclination_error', FloatType(), True), # Standard error of Orbital inclination
    StructField('arg_periastron', DoubleType(), True), # Argument of periastron
    StructField('arg_periastron_error', FloatType(), True), # Standard error of Argument of periastron
    StructField('temperature_ratio', DoubleType(), True), # Ratio of the effective temperatures
    StructField('temperature_ratio_error', DoubleType(), True), # Standard error of the ratio of the effective temperatures
    StructField('temperature_ratio_definition', ByteType(), True), # Code defining which fitting scenario did apply to the effective temperature
    StructField('astrometric_n_obs_al', IntegerType(), True), # Total astrometric CCD observations in AL considered
    StructField('astrometric_n_good_obs_al', IntegerType(), True), # Total astrometric CCD observations in AL actually used
    StructField('rv_n_obs_primary', IntegerType(), True), # Total number of radial velocities considered for the primary
    StructField('rv_n_good_obs_primary', IntegerType(), True), # Total number of radial velocities actually used for the primary
    StructField('rv_n_obs_secondary', IntegerType(), True), # Total number of radial velocities considered for the secondary in the case of SB2
    StructField('rv_n_good_obs_secondary', IntegerType(), True), # Total number of radial velocities actually used for the secondary in the case of SB2
    StructField('phot_g_n_obs', IntegerType(), True), # Total number of G photometry measurements considered
    StructField('phot_g_n_good_obs', IntegerType(), True), # Total number of G photometry measurements actually used
    StructField('bit_index', LongType(), True), # boolean mask for the fields above in the corrVec matrix 
    StructField('corr_vec', ArrayType(FloatType()), True), # Vector form of the upper triangle of the correlation matrix (column-major ordered)
    StructField('obj_func', FloatType(), True), # value of the objective function at the solution
    StructField('goodness_of_fit', FloatType(), True), # goodness of fit in the Hipparcos sense
    StructField('efficiency', FloatType(), True), # Efficiency of the solution
    StructField('significance', FloatType(), True), # The significance of the solution (i.e. how worth keeping a model is)
    StructField('flags', LongType(), True), # Quality flag for the achieved NSS solution
    StructField('conf_spectro_period', FloatType(), True), # The probability of the period for not being due to (gaussian white) noise. Relevant for SB1, SB1C, SB2 and SB2C models. To be ignored otherwise.
    StructField('r_pole_sum', DoubleType(), True), # Sum of the polar radii of primary and secondary (in units of the semi-major axis)
    StructField('r_l1_point_sum', DoubleType(), True), # L1-pointing radii of primary and secondary (in units of the semi-major axis)
    StructField('r_spher_sum', DoubleType(), True), # Sum of the radii of sphere having the same volume as the primary and secondary (in units of the semi-major axis
    StructField('ecl_time_primary', DoubleType(), True), # Time of mid-eclipse of the primary by the secondary
    StructField('ecl_time_secondary', DoubleType(), True), # Time of mid-eclipse of the secondary by the primary
    StructField('ecl_dur_primary', DoubleType(), True), # Duration of primary eclipse assuming spherical components
    StructField('ecl_dur_secondary', DoubleType(), True), # Duration of secondary eclipse assuming spherical components
    StructField('g_luminosity_ratio', DoubleType(), True), # Ratio of the G-band luminosity of the secondary over the primary
    StructField('input_period_error', FloatType(), True), # Standard error of the period taken from VariEclipsingBinary.frequencyError
    StructField('g_rank', DoubleType(), True), # Rank of the G-band solution
    StructField('astrometric_jitter', DoubleType(), True), # Uncorrelated astrometric jitter term
])
nss_vim_fl_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source Identifier
    StructField('nss_solution_type', StringType(), True), # NSS model adopted
    StructField('ra', DoubleType(), True), # Right ascension
    StructField('ra_error', FloatType(), True), # Standard error of right ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('dec_error', FloatType(), True), # Standard error of declination
    StructField('parallax', DoubleType(), True), # Parallax
    StructField('parallax_error', FloatType(), True), # Standard error of parallax
    StructField('pmra', DoubleType(), True), # Proper motion in right ascension direction
    StructField('pmra_error', FloatType(), True), # Standard error of proper motion in right ascension direction
    StructField('pmdec', DoubleType(), True), # Proper motion in declination direction
    StructField('pmdec_error', FloatType(), True), # Standard error of proper motion in declination direction
    StructField('ref_flux_g', FloatType(), True), # Reference flux in the G band
    StructField('vim_d_ra', DoubleType(), True), # VIM coordinate in RA
    StructField('vim_d_ra_error', FloatType(), True), # Standard error of VIM coordinate in RA
    StructField('vim_d_dec', DoubleType(), True), # VIM coordinate in DEC
    StructField('vim_d_dec_error', FloatType(), True), # Standard error of VIM coordinate in DEC
    StructField('astrometric_n_obs_al', IntegerType(), True), # Total astrometric CCD observations in AL considered
    StructField('astrometric_n_good_obs_al', IntegerType(), True), # Total astrometric CCD observations in AL actually used
    StructField('bit_index', LongType(), True), # Boolean mask for the fields above in the corrVec matrix 
    StructField('corr_vec', ArrayType(FloatType()), True), # Vector form of the upper triangle of the correlation matrix
    StructField('obj_func', FloatType(), True), # Value of the objective function at the solution
    StructField('goodness_of_fit', FloatType(), True), # Goodness of fit in the Hipparcos sense
    StructField('efficiency', FloatType(), True), # Efficiency of the solution
    StructField('significance', FloatType(), True), # The significance of the solution (i.e. how worth keeping a model is)
    StructField('flags', LongType(), True), # Quality flag for the achieved NSS solution
])
oa_neuron_information_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('som_id', LongType(), False), # Self-Organized Map identifier
    StructField('neuron_id', LongType(), False), # Neuron identifier
    StructField('neuron_row_index', ShortType(), True), # Row index of the neuron in the Self-Organised Map lattice
    StructField('neuron_column_index', ShortType(), True), # Column index of the neuron in the Self-Organised Map lattice
    StructField('hits', IntegerType(), True), # Number of sources populating the neuron
    StructField('class_label', StringType(), True), # Astronomical class estimated for the neuron
    StructField('centroid_id', LongType(), True), # Identifier of the Gaia source that minimizes the classification distance to the neuron
    StructField('centroid_distance', FloatType(), True), # Squared Euclidean distance between the centroid XP spectrum and the neuron XP prototype
    StructField('template_distance', FloatType(), True), # Squared Euclidean distance between the reference XP template and the neuron XP prototype
    StructField('g_mag_mean', FloatType(), True), # Mean $G$ value for the sources that belong to the neuron
    StructField('g_mag_std_dev', FloatType(), True), # Standard deviation of $G$ values for the sources that belong to the neuron
    StructField('g_mag_min', FloatType(), True), # Minimum $G$ value for the sources that belong to the neuron
    StructField('g_mag_max', FloatType(), True), # Maximum $G$ value for the sources that belong to the neuron
    StructField('bp_mag_mean', FloatType(), True), # Mean $G_{\rm BP}$ value for the sources that belong to the neuron
    StructField('bp_mag_std_dev', FloatType(), True), # Standard deviation of $G_{\rm BP}$ values for the sources that belong to the neuron 
    StructField('bp_mag_min', FloatType(), True), # Minimum value of $G_{\rm BP}$ for the sources that belong to the neuron 
    StructField('bp_mag_max', FloatType(), True), # Maximum value of $G_{\rm BP}$ for the sources that belong to the neuron 
    StructField('rp_mag_mean', FloatType(), True), # Mean $G_{\rm RP}$ value for the sources that belong to the neuron neuron
    StructField('rp_mag_std_dev', FloatType(), True), # Standard deviation of $G_{\rm RP}$ values for the sources that belong to the neuron
    StructField('rp_mag_min', FloatType(), True), # Minimum value of $G_{\rm RP}$ for the sources that belong to the neuron  
    StructField('rp_mag_max', FloatType(), True), # Maximum value of $G_{\rm RP}$ for the sources that belong to the neuron
    StructField('pm_ra_mean', FloatType(), True), # Mean value of the proper motion in right ascension for the sources that belong to the neuron
    StructField('pm_ra_std_dev', FloatType(), True), # Standard deviation of the proper motion in right ascension for the sources that belong to the neuron
    StructField('pm_ra_min', FloatType(), True), # Minimum value of the proper motion in right ascension for the sources that belong to the neuron
    StructField('pm_ra_max', FloatType(), True), # Maximum value of the proper motion in right ascension for the sources that belong to the neuron
    StructField('pm_dec_mean', FloatType(), True), # Mean value of the proper motion in declination for the sources that belong to the neuron
    StructField('pm_dec_std_dev', FloatType(), True), # Standard deviation of the proper motion in declination for the sources that belong to the neuron
    StructField('pm_dec_min', FloatType(), True), # Minimum value of the proper motion in declination for the sources that belong to the neuron
    StructField('pm_dec_max', FloatType(), True), # Maximum value of the proper motion in declination for the sources that belong to the neuron
    StructField('parallax_mean', FloatType(), True), # Mean parallax value for the sources that belong to the neuron
    StructField('parallax_std_dev', FloatType(), True), # Standard deviation of the parallax values for the sources that belong to the neuron
    StructField('parallax_min', FloatType(), True), # Minimum parallax value for the sources that belong to the neuron 
    StructField('parallax_max', FloatType(), True), # Maximum parallax value for the sources that belong to the neuron
    StructField('gal_latitude_mean', FloatType(), True), # Mean galactic latitude for the sources that belong to the neuron
    StructField('gal_latitude_std_dev', FloatType(), True), # Standard deviation of the galactic latitude values for the sources that belong to the neuron 
    StructField('gal_latitude_min', FloatType(), True), # Minimum galactic latitude for the sources that belong to the neuron
    StructField('gal_latitude_max', FloatType(), True), # Maximum galactic latitude for the sources that belong to the neuron
    StructField('intra_neuron_distance_mean', FloatType(), True), # Mean value of the squared Euclidean distance between each of the XP sources in the neuron and the neuron prototype
    StructField('intra_neuron_distance_std_dev', FloatType(), True), # Standard deviation of the squared Euclidean distance between each of the XP sources in the neuron and the neuron prototype
    StructField('intra_neuron_distance_min', FloatType(), True), # Minimum squared Euclidean distance between each of the XP sources in the neuron and the neuron prototype
    StructField('intra_neuron_distance_max', FloatType(), True), # Maximum squared Euclidean distance between each of the XP sources in the neuron and the neuron prototype
    StructField('inter_neuron_distance_mean', FloatType(), True), # Mean value of the squared Euclidean distance between the neuron XP prototype and the XP prototypes of its immediate neighbours
    StructField('inter_neuron_distance_std_dev', FloatType(), True), # Standard deviation of the squared Euclidean distance between the neuron XP prototype and the XP prototypes of its immediate neighbours
    StructField('inter_neuron_distance_min', FloatType(), True), # Minimum value of the squared Euclidean distance between the neuron XP prototype and the XP prototypes of its immediate neighbours
    StructField('inter_neuron_distance_max', FloatType(), True), # Maximum value of the squared Euclidean distance between the neuron XP prototype and the XP prototypes of its immediate neighbours
    StructField('template_name', StringType(), True), # Name of the template used to describe the neuron
    StructField('distance_percentile25', FloatType(), True), # 25th percentile value for the intra-neuron distance distribution
    StructField('distance_percentile50', FloatType(), True), # 50th percentile value for the intra-neuron distance distribution 
    StructField('distance_percentile68', FloatType(), True), # 68th percentile value for the intra-neuron distance distribution
    StructField('distance_percentile75', FloatType(), True), # 75th percentile value for the intra-neuron distance distribution
    StructField('distance_percentile95', FloatType(), True), # 95th percentile value for the intra-neuron distance distribution
    StructField('distance_fwhm', FloatType(), True), # Full Width at Half Maximum value for the intra-neuron distance distribution
    StructField('distance_skew', FloatType(), True), # Skewness value for the intra-neuron distance distribution 
    StructField('distance_kurtosis', FloatType(), True), # Kurtosis value for the intra-neuron distance distribution
    StructField('distance_i_q_r', FloatType(), True), # Inter-Quartile Range value for the intra-neuron distance distribution
    StructField('distance_fwhm_norm', FloatType(), True), # Normalized FWHM value for the intra-neuron distance distribution
    StructField('quality_category', ShortType(), True), # Quality category assigned to the neuron, where 0 corresponds to the most homogeneous neurons and 6 to the most heterogeneous ones
    StructField('bp_transits_mean', FloatType(), True), # Mean value of the number of  BP transits for the sources that belong to the neuron
    StructField('bp_transits_std_dev', FloatType(), True), # Standard deviation of the number of BP transits for the sources that belong to the neuron
    StructField('bp_transits_min', FloatType(), True), # Minimum value of the number of BP transits for the sources that belong to the neuron
    StructField('bp_transits_max', FloatType(), True), # Maximum value of the number of BP transits for the sources that belong to the neuron
    StructField('rp_transits_mean', FloatType(), True), # Mean value of the number of  RP transits for the sources that belong to the neuron
    StructField('rp_transits_std_dev', FloatType(), True), # Standard deviation of the number of RP transits for the sources that belong to the neuron
    StructField('rp_transits_min', FloatType(), True), # Minimum value of the number of RP transits for the sources that belong to the neuron
    StructField('rp_transits_max', FloatType(), True), # Maximum value of the number of RP transits for the sources that belong to the neuron
    StructField('ruwe_mean', FloatType(), True), # Mean value of the renormalised unit weight error for the sources that belong to the neuron
    StructField('ruwe_std_dev', FloatType(), True), # Standard deviation of the renormalised unit weight error for the sources that belong to the neuron
    StructField('ruwe_min', FloatType(), True), # Minimum value of the renormalised unit weight error for the sources that belong to the neuron
    StructField('ruwe_max', FloatType(), True), # Maximum value of the renormalised unit weight error for the sources that belong to the neuron
    StructField('bprp_mean_flux_excess_mean', FloatType(), True), # Mean value of the BP/RP flux excess for the sources that belong to the neuron
    StructField('bprp_mean_flux_excess_std_dev', FloatType(), True), # Standard deviation of the BP/RP flux excess for the sources that belong to the neuron
    StructField('bprp_mean_flux_excess_min', FloatType(), True), # Minimum value of the BP/RP flux excess for the sources that belong to the neuron
    StructField('bprp_mean_flux_excess_max', FloatType(), True), # Maximum value of the BP/RP flux excess for the sources that belong to the neuron
    StructField('bprp_colour_mean', FloatType(), True), # Mean value of the $G_{\rm BP}-G_{\rm RP}$ colour for the sources that belong to the neuron
    StructField('bprp_colour_std_dev', FloatType(), True), # Standard deviation of the $G_{\rm BP}-G_{\rm RP}$ colour for the sources that belong to the neuron
    StructField('bprp_colour_min', FloatType(), True), # Minimum value of the $G_{\rm BP}-G_{\rm RP}$ colour for the sources that belong to the neuron
    StructField('bprp_colour_max', FloatType(), True), # Maximum value of the $G_{\rm BP}-G_{\rm RP}$ colour for the sources that belong to the neuron
])
oa_neuron_xp_spectra_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('neuron_id', LongType(), False), # Neuron identifier
    StructField('neuron_row_index', ShortType(), True), # Row index of the neuron in the Self-Organised Map lattice
    StructField('neuron_column_index', ShortType(), True), # Column index of the neuron in the Self-Organised Map lattice
    StructField('xp_spectrum_prototype_flux', FloatType(), True), # Normalised flux at wavelength {\tt xpSpectrumPrototypeWavelength} for the preprocessed XP spectrum that best represents the neuron (prototype) 
    StructField('xp_spectrum_prototype_wavelength', FloatType(), True), # Wavelength associated with the XP spectrum flux values 
    StructField('xp_spectrum_template_flux', FloatType(), True), # Normalised flux at wavelength {\tt xpSpectrumPrototypeWavelength} for the preprocessed XP spectrum corresponding to the neuron template  
])
qso_candidates_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('astrometric_selection_flag', BooleanType(), True), # Flag indicating if the source is part of the astrometric selection
    StructField('gaia_crf_source', BooleanType(), True), # Flag indicative of whether the source was used define the Gaia-CRF3
    StructField('vari_best_class_name', StringType(), True), # Name of best class, see table VariClassifierClassDefinition for details of the class
    StructField('vari_best_class_score', FloatType(), True), # Score of the best class
    StructField('fractional_variability_g', FloatType(), True), # Fractional variability in the G band
    StructField('structure_function_index', FloatType(), True), # Index of the first-order structure function in the G band
    StructField('structure_function_index_scatter', DoubleType(), True), # Standard deviation of the index of the structure function
    StructField('qso_variability', FloatType(), True), # Quasar variability metric in the G band
    StructField('non_qso_variability', FloatType(), True), # Non-quasar variability metric in the G band
    StructField('vari_agn_membership_score', DoubleType(), True), # Membership score (0=lowest,1=highest) of source to be of AGN type
    StructField('classprob_dsc_combmod_quasar', FloatType(), True), # Probability from DSC-Combmod of being a quasar (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classprob_dsc_combmod_galaxy', FloatType(), True), # Probability from DSC-Combmod of being a galaxy (data used: BP/RP spectrum, photometry, astrometry)
    StructField('classlabel_dsc', StringType(), True), # Class assigned by DSC based on the probability from its Combmod classifier
    StructField('classlabel_dsc_joint', StringType(), True), # Class assigned by DSC based on the probability from its Specmod and Allosmod classifiers
    StructField('classlabel_oa', StringType(), True), # Class assigned by OA the neuron that represents the source
    StructField('redshift_qsoc', FloatType(), True), # Redshift from QSOC
    StructField('redshift_qsoc_lower', FloatType(), True), # Redshift lower confidence level from QSOC
    StructField('redshift_qsoc_upper', FloatType(), True), # Redshift upper confidence level from QSOC
    StructField('ccfratio_qsoc', FloatType(), True), # Value of the cross-correlation function used to derive the redshift from QSOC, relative to the maximum value
    StructField('zscore_qsoc', FloatType(), True), # Redshift zscore from QSOC
    StructField('flags_qsoc', LongType(), True), # Processing flags for the analysis based on BP/RP Spectra from QSOC
    StructField('n_transits', IntegerType(), True), # Number of transits used for the morphological analysis
    StructField('intensity_quasar', DoubleType(), True), # Fitted intensity of the quasar at its center
    StructField('intensity_quasar_error', DoubleType(), True), # Error on the fitted intensity of the quasar at its center
    StructField('intensity_hostgalaxy', DoubleType(), True), # Fitted intensity of the host galaxy at the effective radius
    StructField('intensity_hostgalaxy_error', DoubleType(), True), # Error on the fitted intensity of the host galaxy at effective radius
    StructField('radius_hostgalaxy', DoubleType(), True), # Fitted effective radius of the host galaxy
    StructField('radius_hostgalaxy_error', DoubleType(), True), # Error on the fitted effective radius of the host galaxy
    StructField('sersic_index', FloatType(), True), # Fitted sersic Index
    StructField('sersic_index_error', FloatType(), True), # Error on the fitted sersic Index
    StructField('ellipticity_hostgalaxy', DoubleType(), True), # Fitted ellipticity of the host galaxy
    StructField('ellipticity_hostgalaxy_error', DoubleType(), True), # Error on the fitted ellipticity of the host galaxy
    StructField('posangle_hostgalaxy', DoubleType(), True), # Fitted position angle of the host galaxy
    StructField('posangle_hostgalaxy_error', DoubleType(), True), # Error on the fitted position angle of the host galaxy
    StructField('host_galaxy_detected', BooleanType(), True), # Flag indicating whether a host galaxy has been detected
    StructField('l2_norm', DoubleType(), True), # L2 norm for the fitted Sersic profile
    StructField('morph_params_corr_vec', ArrayType(DoubleType()), True), # Vector form of the upper triangle of the correlation matrix for the fitted morphological parameters
    StructField('host_galaxy_flag', ByteType(), True), # Flag indicative of processing or scientific quality for the morphological parameters fitting
    StructField('source_selection_flags', IntegerType(), True), # Bit indicative of whether the input data from a given module met the source list eligibility criteria for the source of interest
])
qso_catalogue_name_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('catalogue_id', ByteType(), False), # The unique identifier for the catalogue(s) used to select the sources in the morphological analysis
])
rvs_mean_spectrum_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('ra', DoubleType(), True), # Right Ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('flux', ArrayType(FloatType()), True), # array of fluxes
    StructField('flux_error', ArrayType(FloatType()), True), # array of uncertainties in flux
    StructField('combined_transits', ShortType(), True), # number of combined transits
    StructField('combined_ccds', ShortType(), True), # number of combined CCD spectra
    StructField('deblended_ccds', ShortType(), True), # number of deblended CCD spectra 
])
science_alerts_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('transit_id', LongType(), False), # Alerting transit identifier
    StructField('name', StringType(), True), # Name of alert
    StructField('solution_id', LongType(), True), # Solution Identifier
])
sso_observation_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Source identifier
    StructField('denomination', StringType(), True), # standard MPC denomination of the asteroid
    StructField('transit_id', LongType(), True), # Transit Identifier
    StructField('observation_id', LongType(), True), # Observation Identifier
    StructField('number_mp', LongType(), True), # Minor Planet number
    StructField('epoch', DoubleType(), False), # Gaia-centric epoch TCB(Gaia)
    StructField('epoch_err', DoubleType(), True), # Error in Gaiacentric epoch
    StructField('epoch_utc', DoubleType(), True), # Gaia-centric TCB epoch converted to UTC
    StructField('ra', DoubleType(), True), # Right ascension of the source
    StructField('dec', DoubleType(), True), # Declination of the source
    StructField('ra_error_systematic', DoubleType(), True), # Standard error of right ascension - systematic
    StructField('dec_error_systematic', DoubleType(), True), # Standard error of declination - systematic
    StructField('ra_dec_correlation_systematic', DoubleType(), True), # Correlation of ra and dec errors - systematic
    StructField('ra_error_random', DoubleType(), True), # Standard error of right ascension - random
    StructField('dec_error_random', DoubleType(), True), # Standard error of declination - random
    StructField('ra_dec_correlation_random', DoubleType(), True), # Correlation of ra and dec errors - random
    StructField('g_mag', DoubleType(), True), # Calibrated G mag
    StructField('g_flux', DoubleType(), True), # Average calibrated G flux for the transit
    StructField('g_flux_error', DoubleType(), True), # Error on the G flux
    StructField('x_gaia', DoubleType(), True), # Barycentric x position of Gaia
    StructField('y_gaia', DoubleType(), True), # Barycentric y position of Gaia
    StructField('z_gaia', DoubleType(), True), # Barycentric z position of Gaia
    StructField('vx_gaia', DoubleType(), True), # Barycentric x velocity of Gaia
    StructField('vy_gaia', DoubleType(), True), # Barycentric y velocity of Gaia
    StructField('vz_gaia', DoubleType(), True), # Barycentric z velocity of Gaia
    StructField('x_gaia_geocentric', DoubleType(), True), # Geocentric x position of Gaia
    StructField('y_gaia_geocentric', DoubleType(), True), # Geocentric y position of Gaia
    StructField('z_gaia_geocentric', DoubleType(), True), # Geocentric z position of Gaia
    StructField('vx_gaia_geocentric', DoubleType(), True), # Geocentric x velocity of Gaia
    StructField('vy_gaia_geocentric', DoubleType(), True), # Geocentric y velocity of Gaia
    StructField('vz_gaia_geocentric', DoubleType(), True), # Geocentric z velocity of Gaia
    StructField('position_angle_scan', DoubleType(), True), # Position angle of the scanning direction 
    StructField('astrometric_outcome_ccd', ArrayType(IntegerType()), True), # Result of processing the CCDs
    StructField('astrometric_outcome_transit', IntegerType(), True), # Result of processing the transit
])
sso_reflectance_spectrum_schema = StructType([
    StructField('source_id', LongType(), False), # Source identifier
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('number_mp', LongType(), True), # Minor Planet number
    StructField('denomination', StringType(), True), # standard MPC denomination of the asteroid
    StructField('nb_samples', ShortType(), True), # Nb samples in spectrum
    StructField('num_of_spectra', IntegerType(), True), # number of epoch spectra used to compute the average
    StructField('reflectance_spectrum', FloatType(), True), # Reflectance spectrum
    StructField('reflectance_spectrum_err', FloatType(), True), # Error in reflectance spectrum
    StructField('wavelength', FloatType(), True), # Internally-calibrated wavelength of reflectance spectrum
    StructField('reflectance_spectrum_flag', ByteType(), True), # Reflectance spectrum value flag
])
sso_source_schema = StructType([
    StructField('solution_id', LongType(), False), # Solution Identifier
    StructField('source_id', LongType(), False), # Source identifier
    StructField('num_of_obs', IntegerType(), True), # number of observations
    StructField('number_mp', LongType(), True), # Minor Planet number
    StructField('denomination', StringType(), True), # standard MPC denomination of the asteroid
    StructField('num_of_spectra', IntegerType(), True), # Number of epoch spectra used to compute the average
])
total_galactic_extinction_map_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('healpix_id', LongType(), False), # HEALPix identification
    StructField('healpix_level', ByteType(), True), # HEALPix level used 
    StructField('a0', FloatType(), True), # Mean $A_0$ extinction parameter
    StructField('a0_uncertainty', FloatType(), True), # Uncertainty for the mean $A_0$
    StructField('a0_min', FloatType(), True), # Minimum $A_0$ value used for the HEALPix of interest
    StructField('a0_max', FloatType(), True), # Maximum $A_0$ value used for the HEALPix of interest
    StructField('num_tracers_used', IntegerType(), True), # Number of tracers used
    StructField('optimum_hpx_flag', BooleanType(), True), # Flag to indicate whether a given HEALPix level is the optimum (True) or not (False)
    StructField('status', ShortType(), True), # Exit status for TGE
])
total_galactic_extinction_map_opt_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('healpix_id', LongType(), False), # HEALPix identification
    StructField('a0', FloatType(), True), # Median A$_0$ extinction parameter
    StructField('a0_uncertainty', FloatType(), True), # Uncertainty for the mean A$_0$
    StructField('num_tracers_used', IntegerType(), True), # Number of tracers used
    StructField('status', ShortType(), True), # Exit status for TGE
    StructField('optimum_hpx_level', ByteType(), True), # Number indicating which HEALPix level was chosen to populate this HEALPix
])
vari_agn_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('fractional_variability_g', FloatType(), True), # Fractional variability in the G band
    StructField('structure_function_index', FloatType(), True), # Index of the first-order structure function in the G band
    StructField('structure_function_index_scatter', FloatType(), True), # Standard deviation of the index of the structure function
    StructField('qso_variability', FloatType(), True), # Quasar variability metric in the G band
    StructField('non_qso_variability', FloatType(), True), # Non-quasar variability metric in the G band
])
vari_classifier_class_definition_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('classifier_name', StringType(), False), # Name of the classifier that is detailed in this entry
    StructField('class_name', StringType(), False), # Name of the published class from this classifier
    StructField('class_description', StringType(), True), # Description of the published class from this classifier
])
vari_classifier_definition_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('classifier_name', StringType(), False), # Name of the classifier that is detailed in this entry
    StructField('classifier_description', StringType(), True), # Description of this classifier
])
vari_classifier_result_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('classifier_name', StringType(), False), # Classifier name used to produce this result, use for lookup in \texttt{VariClassifierDefinition} table
    StructField('best_class_name', StringType(), True), # Name of best class, see table \texttt{VariClassifierClassDefinition} for details of the class
    StructField('best_class_score', FloatType(), True), # Score of the best class
])
vari_compact_companion_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('period', DoubleType(), True), # Orbital period
    StructField('period_error', FloatType(), True), # Orbital period error
    StructField('t0_g', DoubleType(), True), # G-band reference time
    StructField('t0_g_error', FloatType(), True), # G-band reference time error
    StructField('t0_bp', DoubleType(), True), # BP-band reference time
    StructField('t0_bp_error', FloatType(), True), # BP-band reference time error
    StructField('t0_rp', DoubleType(), True), # RP-band reference time
    StructField('t0_rp_error', FloatType(), True), # RP-band reference time error
    StructField('harmonic_model_params_g', ArrayType(FloatType()), True), # G-band harmonics
    StructField('harmonic_model_params_g_error', ArrayType(FloatType()), True), # G-band harmonics errors
    StructField('harmonic_model_params_bp', ArrayType(FloatType()), True), # BP-band harmonics
    StructField('harmonic_model_params_bp_error', ArrayType(FloatType()), True), # BP-band harmonics errors
    StructField('harmonic_model_params_rp', ArrayType(FloatType()), True), # RP-band harmonics
    StructField('harmonic_model_params_rp_error', ArrayType(FloatType()), True), # RP-band harmonics errors
    StructField('model_mean_g', FloatType(), True), # Harmonics model mean G-band magnitude
    StructField('model_mean_g_error', FloatType(), True), # Harmonics model mean G-band magnitude error
    StructField('model_mean_bp', FloatType(), True), # Harmonics model mean BP-band magnitude
    StructField('model_mean_bp_error', FloatType(), True), # Harmonics model mean BP-band magnitude error
    StructField('model_mean_rp', FloatType(), True), # Harmonics model mean RP-band magnitude
    StructField('model_mean_rp_error', FloatType(), True), # Harmonics model mean RP-band magnitude error
    StructField('mod_min_mass_ratio', FloatType(), True), # Modified minimum mass ratio
    StructField('mod_min_mass_ratio_one_sigma', FloatType(), True), # 15.9 percentile modified minimum mass ratio
    StructField('mod_min_mass_ratio_three_sigma', FloatType(), True), # 0.135 percentile modified minimum mass ratio
    StructField('alpha', FloatType(), True), # alpha ellipsoidal coefficient
])
vari_eclipsing_binary_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('global_ranking', FloatType(), True), # Number between 0 (worst) and 1 (best)
    StructField('reference_time', DoubleType(), True), # Reference time used for the geometric model fit
    StructField('frequency', DoubleType(), True), # Frequency of geometric model of the eclipsing binary light curve
    StructField('frequency_error', FloatType(), True), # Uncertainty of \texttt{frequency}
    StructField('geom_model_reference_level', FloatType(), True), # Magnitude reference level of geometric model
    StructField('geom_model_reference_level_error', FloatType(), True), # Uncertainty of \texttt{geomModelReferenceLevel}
    StructField('geom_model_gaussian1_phase', FloatType(), True), # Phase of the Gaussian 1 component
    StructField('geom_model_gaussian1_phase_error', FloatType(), True), # Uncertainty of \texttt{geomModelGaussian1Phase}
    StructField('geom_model_gaussian1_sigma', FloatType(), True), # Standard deviation [phase] of Gaussian 1 component
    StructField('geom_model_gaussian1_sigma_error', FloatType(), True), # Uncertainty of \texttt{geomModelGaussian1Sigma}
    StructField('geom_model_gaussian1_depth', FloatType(), True), # Magnitude depth of Gaussian 1 component
    StructField('geom_model_gaussian1_depth_error', FloatType(), True), # Uncertainty of \texttt{geomModelGaussian1Depth}
    StructField('geom_model_gaussian2_phase', FloatType(), True), # Phase of Gaussian 2 component
    StructField('geom_model_gaussian2_phase_error', FloatType(), True), # Uncertainty of \texttt{geomModelGaussian2Phase}
    StructField('geom_model_gaussian2_sigma', FloatType(), True), # Standard deviation [phase] of Gaussian 2 component
    StructField('geom_model_gaussian2_sigma_error', FloatType(), True), # Uncertainty of \texttt{geomModelGaussian2Sigma}
    StructField('geom_model_gaussian2_depth', FloatType(), True), # Magnitude depth of Gaussian2 component
    StructField('geom_model_gaussian2_depth_error', FloatType(), True), # Uncertainty of \texttt{geomModelGaussian2Depth}
    StructField('geom_model_cosine_half_period_amplitude', FloatType(), True), # Amplitude of the cosine component with half the period of the geometric model
    StructField('geom_model_cosine_half_period_amplitude_error', FloatType(), True), # Uncertainty of \texttt{geomModelCosineHalfPeriodAmplitude}
    StructField('geom_model_cosine_half_period_phase', FloatType(), True), # Reference phase of the cosine component with half the period of the geometric model
    StructField('geom_model_cosine_half_period_phase_error', FloatType(), True), # Uncertainty of \texttt{geomModelCosineHalfPeriodPhase}
    StructField('model_type', StringType(), True), # Type of geometrical model of the light curve
    StructField('num_model_parameters', ByteType(), True), # Number of free parameters of the geometric model
    StructField('reduced_chi2', FloatType(), True), # Reduced Chi2 of the geometrical model fit
    StructField('derived_primary_ecl_phase', FloatType(), True), # Primary eclipse: phase at geometrically deepest point 
    StructField('derived_primary_ecl_phase_error', FloatType(), True), # Primary eclipse: uncertainty of \texttt{derivedPrimaryEclPhase}
    StructField('derived_primary_ecl_duration', FloatType(), True), # Primary eclipse: duration [phase fraction]
    StructField('derived_primary_ecl_duration_error', FloatType(), True), # Primary eclipse: uncertainty of \texttt{derivedPrimaryEclDuration}
    StructField('derived_primary_ecl_depth', FloatType(), True), # Primary eclipse: depth
    StructField('derived_primary_ecl_depth_error', FloatType(), True), # Primary eclipse: uncertainty of \texttt{derivedPrimaryEclDepth}
    StructField('derived_secondary_ecl_phase', FloatType(), True), # Secondary eclipse: phase at geometrically second deepest point 
    StructField('derived_secondary_ecl_phase_error', FloatType(), True), # Secondary eclipse: uncertainty of \texttt{derivedSecondaryEclPhase}
    StructField('derived_secondary_ecl_duration', FloatType(), True), # Secondary eclipse: duration [phase fraction]
    StructField('derived_secondary_ecl_duration_error', FloatType(), True), # Secondary eclipse: uncertainty of \texttt{derivedSecondaryEclDuration}
    StructField('derived_secondary_ecl_depth', FloatType(), True), # Secondary eclipse: depth
    StructField('derived_secondary_ecl_depth_error', FloatType(), True), # Secondary eclipse: uncertainty of \texttt{derivedSecondaryEclDepth}
])
vari_epoch_radial_velocity_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('transit_id', LongType(), True), # Transit unique identifier
    StructField('rv_obs_time', DoubleType(), True), # Observing time of the transit
    StructField('radial_velocity', DoubleType(), True), # Barycentric radial velocity
    StructField('radial_velocity_error', DoubleType(), True), # Barycentric radial velocity error
    StructField('rejected_by_variability', BooleanType(), True), # Rejected by DPAC variability processing (or variability analysis)
    StructField('solution_id', LongType(), True), # Solution Identifier
])
vari_long_period_variable_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('frequency', DoubleType(), True), # Frequency of the LPV
    StructField('frequency_error', FloatType(), True), # Error on the frequency
    StructField('amplitude', FloatType(), True), # Amplitude of the LPV variability
    StructField('median_delta_wl_rp', FloatType(), True), # Median of the pseudo-wavelength separations between the two highest peaks in RP spectra 
    StructField('is_cstar', BooleanType(), True), # Flag to mark C-stars
])
vari_microlensing_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('paczynski0_g0', FloatType(), True), # G-band magnitude baseline (level 0)
    StructField('paczynski0_g0_error', FloatType(), True), # Error of G-band magnitude baseline (level 0)
    StructField('paczynski0_bp0', FloatType(), True), # BP-band magnitude baseline (level 0)
    StructField('paczynski0_bp0_error', FloatType(), True), # Error of BP-band magnitude baseline (level 0)
    StructField('paczynski0_rp0', FloatType(), True), # RP-band magnitude baseline (level 0)
    StructField('paczynski0_rp0_error', FloatType(), True), # Error of RP-band magnitude baseline (level 0)
    StructField('paczynski0_u0', DoubleType(), True), # Impact parameter (level 0)
    StructField('paczynski0_u0_error', DoubleType(), True), # Error of the impact parameter (level 0)
    StructField('paczynski0_te', FloatType(), True), # Event timescale (level 0)
    StructField('paczynski0_te_error', FloatType(), True), # Error of event timescale (level 0)
    StructField('paczynski0_tmax', DoubleType(), True), # Time of maximum amplification (level 0)
    StructField('paczynski0_tmax_error', DoubleType(), True), # Error of time of maximum amplification (level 0)
    StructField('paczynski0_chi2', FloatType(), True), # Chi square of level 0 Paczynski fit
    StructField('paczynski0_chi2_dof', FloatType(), True), # Reduced chi square of level 0 Paczynski fit
    StructField('paczynski1_g0', FloatType(), True), # G-band magnitude baseline (level 1)
    StructField('paczynski1_g0_error', FloatType(), True), # Error of G-band magnitude baseline (level 1)
    StructField('paczynski1_bp0', FloatType(), True), # BP-band magnitude baseline (level 1)
    StructField('paczynski1_bp0_error', FloatType(), True), # Error of BP-band magnitude baseline (level 1)
    StructField('paczynski1_rp0', FloatType(), True), # RP-band magnitude baseline (level 1)
    StructField('paczynski1_rp0_error', FloatType(), True), # Error of RP-band magnitude baseline (level 1)
    StructField('paczynski1_u0', DoubleType(), True), # Impact parameter (level 1)
    StructField('paczynski1_u0_error', DoubleType(), True), # Error of the impact parameter (level 1)
    StructField('paczynski1_te', FloatType(), True), # Event timescale (level 1)
    StructField('paczynski1_te_error', FloatType(), True), # Error of event timescale (level 1)
    StructField('paczynski1_tmax', DoubleType(), True), # Time of maximum amplification (level 1)
    StructField('paczynski1_tmax_error', DoubleType(), True), # Error of time of maximum amplification (level 1)
    StructField('paczynski1_fs_g', FloatType(), True), # Blending factor in G-band (level 1)
    StructField('paczynski1_fs_g_error', FloatType(), True), # Error of blending factor in G-band (level 1)
    StructField('paczynski1_fs_bp', FloatType(), True), # Blending factor in BP-band (level 1)
    StructField('paczynski1_fs_bp_error', FloatType(), True), # Error of blending factor in BP-band (level 1)
    StructField('paczynski1_fs_rp', FloatType(), True), # Blending factor in RP-band (level 1)
    StructField('paczynski1_fs_rp_error', FloatType(), True), # Error of blending factor in RP-band (level 1)
    StructField('paczynski1_chi2', FloatType(), True), # Chi square of level 1 Paczynski fit
    StructField('paczynski1_chi2_dof', FloatType(), True), # Reduced chi square of level 1 Paczynski fit
])
vari_ms_oscillator_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('frequency1', DoubleType(), True), # Best frequency
    StructField('fap_g_freq1', FloatType(), True), # False alarm probability corresponding to the best frequency
    StructField('amplitude_g_freq1', FloatType(), True), # Half peak-to-peak amplitude in the G band of the best frequency
    StructField('phase_g_freq1', FloatType(), True), # Phase of the oscillation in the G band corresponding to best frequency
    StructField('num_harmonics', ByteType(), True), # Number of significant harmonics of the best frequency
    StructField('amplitude_g_freq1_harm2', FloatType(), True), # Half peak-to-peak amplitude in the G band of the second harmonic of the best frequency
    StructField('phase_g_freq1_harm2', FloatType(), True), # Phase of the oscillation in the G band corresponding to the second harmonic of the best frequency
    StructField('amplitude_g_freq1_harm3', FloatType(), True), # Half peak-to-peak amplitude in the G band of the third harmonic of the best frequency
    StructField('phase_g_freq1_harm3', FloatType(), True), # Phase of the oscillation in the G band corresponding to the third harmonic of the best frequency
])
vari_planetary_transit_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('transit_reference_time', DoubleType(), True), # Mid-transit reference time
    StructField('transit_period', DoubleType(), True), # Most probable transit period
    StructField('transit_depth', FloatType(), True), # Transit depth
    StructField('transit_duration', FloatType(), True), # Transit duration
    StructField('num_in_transit', ByteType(), True), # Number of in-transit observations
])
vari_rad_vel_statistics_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('num_selected_rv', ShortType(), True), # Total number of radial velocity transits selected for variability analysis
    StructField('mean_obs_time_rv', DoubleType(), True), # Mean observation time for radial velocity transits
    StructField('time_duration_rv', FloatType(), True), # Time duration of the time series for radial velocity transits
    StructField('min_rv', FloatType(), True), # Minimum radial velocity
    StructField('max_rv', FloatType(), True), # Maximum radial velocity
    StructField('mean_rv', FloatType(), True), # Mean radial velocity
    StructField('median_rv', FloatType(), True), # Median radial velocity
    StructField('range_rv', FloatType(), True), # Difference between the highest and lowest radial velocity transits
    StructField('std_dev_rv', FloatType(), True), # Square root of the unweighted radial velocity variance
    StructField('skewness_rv', FloatType(), True), # Standardized unweighted radial velocity skewness
    StructField('kurtosis_rv', FloatType(), True), # Standardized unweighted radial velocity kurtosis
    StructField('mad_rv', FloatType(), True), # Median Absolute Deviation (MAD) for radial velocity transits
    StructField('abbe_rv', FloatType(), True), # Abbe value for radial velocity transits
    StructField('iqr_rv', FloatType(), True), # Interquartile range for radial velocity transits
])
vari_short_timescale_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Unique source identifier
    StructField('amplitude_estimate', FloatType(), True), # Amplitude estimate of all per-CCD G-band photometry (95th quantile - 5th quantile)
    StructField('number_of_fov_transits', ShortType(), True), # Number of FoV transits with more than 7 CCD measurements after time series cleaning
    StructField('mean_of_fov_abbe_values', FloatType(), True), # Mean of per-FoV Abbe values derived from per-CCD G-band photometry
    StructField('variogram_num_points', ByteType(), True), # Number of selected timescale(s) derived from the variogram
    StructField('variogram_char_timescales', ArrayType(FloatType()), True), # Characteristic timescale(s) of variability
    StructField('variogram_values', ArrayType(DoubleType()), True), # Variogram values associated with the {\tt variogramCharTimescales}
    StructField('frequency', DoubleType(), True), # Frequency search result for either G CCD, G FoV, BP or RP photometry
])
xp_continuous_mean_spectrum_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('bp_basis_function_id', ShortType(), True), # Identifier defining the set of basis functions for the BP spectrum representation
    StructField('bp_degrees_of_freedom', ShortType(), True), # Degrees of freedom for the BP spectrum representation
    StructField('bp_n_parameters', ByteType(), True), # Number of parameters for the BP spectrum representation
    StructField('bp_n_measurements', ShortType(), True), # Number of measurements used for the BP spectrum generation
    StructField('bp_n_rejected_measurements', ShortType(), True), # Number of rejected measurements in the BP spectrum generation
    StructField('bp_standard_deviation', FloatType(), True), # Standard deviation for the BP spectrum representation
    StructField('bp_chi_squared', FloatType(), True), # Chi squared for the BP spectrum representation
    StructField('bp_coefficients', ArrayType(DoubleType()), True), # Basis function coefficients for the BP spectrum representation
    StructField('bp_coefficient_errors', ArrayType(FloatType()), True), # Basis function coefficient errors for the BP spectrum representation
    StructField('bp_coefficient_correlations', ArrayType(FloatType()), True), # Correlation matrix for BP coefficients
    StructField('bp_n_relevant_bases', ShortType(), True), # Number of bases that are relevant for the representation of this mean BP spectrum
    StructField('bp_relative_shrinking', FloatType(), True), # Measure of the relative shrinking of the coefficient vector when truncation is applied for the mean BP spectrum
    StructField('rp_basis_function_id', ShortType(), True), # Identifier defining the set of basis functions for the BP spectrum representation
    StructField('rp_degrees_of_freedom', ShortType(), True), # Degrees of freedom for the RP spectrum representation
    StructField('rp_n_parameters', ByteType(), True), # Number of parameters for the RP spectrum representation
    StructField('rp_n_measurements', ShortType(), True), # Number of measurements used for the RP spectrum generation
    StructField('rp_n_rejected_measurements', ShortType(), True), # Number of rejected measurements in the RP spectrum generation
    StructField('rp_standard_deviation', FloatType(), True), # Standard deviation for the RP spectrum representation
    StructField('rp_chi_squared', FloatType(), True), # Chi squared for the RP spectrum representation
    StructField('rp_coefficients', ArrayType(DoubleType()), True), # Basis function coefficients for the RP spectrum representation
    StructField('rp_coefficient_errors', ArrayType(FloatType()), True), # Basis function coefficient errors for the RP spectrum representation
    StructField('rp_coefficient_correlations', ArrayType(FloatType()), True), # Correlation matrix for RP coefficients
    StructField('rp_n_relevant_bases', ShortType(), True), # Number of bases that are relevant for the representation of this mean RP spectrum
    StructField('rp_relative_shrinking', FloatType(), True), # Measure of the relative shrinking of the coefficient vector when truncation is applied for the mean RP spectrum
])
xp_merge_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('wavelength', FloatType(), False), # Wavelength
    StructField('bp_weight', FloatType(), True), # BP flux weight
    StructField('rp_weight', FloatType(), True), # RP flux weight
])
xp_sampled_mean_spectrum_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('ra', DoubleType(), True), # Right Ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('flux', ArrayType(FloatType()), True), # mean BP + RP combined spectrum flux
    StructField('flux_error', ArrayType(FloatType()), True), # mean BP + RP combined spectrum flux error
])
xp_sampling_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('band', StringType(), True), # BP or RP photometric band
    StructField('wavelength', FloatType(), False), # Wavelength
    StructField('basis_function', ShortType(), True), # basis function index
    StructField('sampling_coefficient', DoubleType(), True), # sampling matrix coefficient
])
xp_summary_schema = StructType([
    StructField('source_id', LongType(), False), # Unique source identifier (unique within a particular Data Release)
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('bp_n_relevant_bases', ShortType(), True), # Number of bases that are relevant for the representation of this mean BP spectrum
    StructField('bp_relative_shrinking', FloatType(), True), # Measure of the relative shrinking of the coefficient vector when truncation is applied for the mean BP spectrum
    StructField('bp_n_measurements', ShortType(), True), # Number of measurements used for the BP spectrum generation
    StructField('bp_n_rejected_measurements', ShortType(), True), # Number of rejected measurements in the BP spectrum generation
    StructField('bp_standard_deviation', FloatType(), True), # Standard deviation for the BP spectrum representation
    StructField('bp_chi_squared', FloatType(), True), # Chi squared for the BP spectrum representation
    StructField('bp_n_transits', ShortType(), True), # Number of transits contributing to the mean in BP
    StructField('bp_n_contaminated_transits', ShortType(), True), # Number of contaminated transits in BP
    StructField('bp_n_blended_transits', ShortType(), True), # Number of blended transits in BP
    StructField('rp_n_relevant_bases', ShortType(), True), # Number of bases that are relevant for the representation of this mean RP spectrum
    StructField('rp_relative_shrinking', FloatType(), True), # Measure of the relative shrinking of the coefficient vector when truncation is applied for the mean RP spectrum
    StructField('rp_n_measurements', ShortType(), True), # Number of measurements used for the RP spectrum generation
    StructField('rp_n_rejected_measurements', ShortType(), True), # Number of rejected measurements in the RP spectrum generation
    StructField('rp_standard_deviation', FloatType(), True), # Standard deviation for the RP spectrum representation
    StructField('rp_chi_squared', FloatType(), True), # Chi squared for the RP spectrum representation
    StructField('rp_n_transits', ShortType(), True), # Number of transits contributing to the mean in RP
    StructField('rp_n_contaminated_transits', ShortType(), True), # Number of contaminated transits in RP
    StructField('rp_n_blended_transits', ShortType(), True), # Number of blended transits in RP
])
commanded_scan_law_schema = StructType([
    StructField('jd_time', DoubleType(), True), # Time [Julian Date in TCB at Gaia - 2455197.5]
    StructField('bjd_fov1', DoubleType(), True), # Time [Julian Date in TCB at barycentre for FOV1 - 2455197.5]
    StructField('bjd_fov2', DoubleType(), True), # Time [Julian Date in TCB at barycentre for FOV2 - 2455197.5]
    StructField('obmt_time', LongType(), False), # Time at Gaia (OBMT)
    StructField('ra_fov1', FloatType(), True), # Right Ascension of FOV1 centre
    StructField('dec_fov1', FloatType(), True), # Declination of FOV1 centre
    StructField('heal_pix_fov1', IntegerType(), True), # FOV1 HEALPix level 12
    StructField('scan_angle_fov1', FloatType(), True), # Scan position angle of FOV1
    StructField('ra_fov2', FloatType(), True), # Right ascension of FOV2 centre
    StructField('dec_fov2', FloatType(), True), # Declination of FOV2 centre
    StructField('heal_pix_fov2', IntegerType(), True), # FOV2 HEALPix level 12
    StructField('scan_angle_fov2', FloatType(), True), # Scan position angle of FOV2
    StructField('solution_id', LongType(), True), # Solution Identifier
])
agn_cross_id_schema = StructType([
    StructField('source_name_in_catalogue', StringType(), True), # Identifier in the external catalogue
    StructField('source_id', LongType(), False), # Gaia source identifier
    StructField('catalogue_name', StringType(), True), # Name of the external catalogue
])
frame_rotator_source_schema = StructType([
    StructField('source_id', LongType(), False), # Gaia source identifier
    StructField('considered_for_reference_frame_orientation', BooleanType(), True), # Considered for the reference frame orientation
    StructField('used_for_reference_frame_orientation', BooleanType(), True), # Used for the reference frame orientation
    StructField('considered_for_reference_frame_spin', BooleanType(), True), # Considered for the reference frame spin
    StructField('used_for_reference_frame_spin', BooleanType(), True), # Used for the reference frame spin
])
gaia_crf3_xm_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Gaia source identifier
    StructField('icrf3sx', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in ICRF3 S/X
    StructField('icrf3k', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in ICRF3 K
    StructField('icrf3xka', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in ICRF3 X/Ka
    StructField('icrf_name', StringType(), True), # The ICRF name of the source
    StructField('iers_name', StringType(), True), # The IERS name of the source
    StructField('ocars', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in OCARS
    StructField('ocars_name', StringType(), True), # The name for this source in OCARS
    StructField('aw15', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in allWISE
    StructField('aw15_name', StringType(), True), # The name for this source in allWISE
    StructField('r90', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in the catalogue R90
    StructField('r90_name', StringType(), True), # The name for this source in R90
    StructField('m65', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in Milliquas v6.5
    StructField('m65_name', StringType(), True), # The name for this source in Milliquas v6.5
    StructField('c75', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in the catalogue C75
    StructField('c75_name', StringType(), True), # The name for this source in C75
    StructField('dr14q', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in the catalogue SDSS DR14Q
    StructField('dr14q_name', StringType(), True), # The name for this source in SDSS DR14Q
    StructField('lqac5', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in LQAC-5
    StructField('lqac5_name', StringType(), True), # The name for this source in LQAC-5
    StructField('lamost5', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in the LAMOST QSO catalogue
    StructField('lamost5_name', StringType(), True), # The name for this source in the LAMOST QSO catalogue
    StructField('lqrf', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in LQRF
    StructField('lqrf_name', StringType(), True), # The name for this source in LQRF
    StructField('cat2qz', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in 2QZ
    StructField('cat2qz_name', StringType(), True), # The name for this source in 2QZ
    StructField('bzcat5', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in Roma-BZCAT, v5
    StructField('bzcat5_name', StringType(), True), # The name for this source in Roma-BZCAT, v5
    StructField('cat2whspj', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in 2WHSPJ
    StructField('cat2whspj_name', StringType(), True), # The name for this source in 2WHSPJ
    StructField('alma19', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in the ALMA calibrator catalogue
    StructField('alma19_name', StringType(), True), # The name for this source in the ALMA calibrator catalogue
    StructField('guw', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in Gaia-unWISE
    StructField('guw_name', StringType(), True), # The name for this source in Gaia-unWISE
    StructField('b19', BooleanType(), True), # The flag describing if the Gaia-CRF3 source was found in the Gaia DR2 quasar and galaxy classification catalogue
    StructField('b19_name', StringType(), True), # The name for this source in the Gaia DR2 quasar and galaxy classification catalogue
])
gaia_source_simulation_schema = StructType([
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('source_id', LongType(), False), # Long Identifier
    StructField('ra', DoubleType(), True), # Right Ascension
    StructField('ra_error', FloatType(), True), # Right Ascension error
    StructField('dec', DoubleType(), True), # Declination
    StructField('dec_error', FloatType(), True), # Declination error
    StructField('parallax', FloatType(), True), # Parallax
    StructField('parallax_error', FloatType(), True), # Parallax error
    StructField('pmra', FloatType(), True), # Proper motion in RA
    StructField('pmra_error', FloatType(), True), # Error in RA proper motion
    StructField('pmdec', FloatType(), True), # Proper motion in dec
    StructField('pmdec_error', FloatType(), True), # Error in dec. proper motion
    StructField('n_obs_al', IntegerType(), True), # Number of AL observations
    StructField('n_outliers_al', IntegerType(), True), # Number of outliers AL observations
    StructField('phot_g_mean_flux', FloatType(), True), # Mean G flux
    StructField('phot_g_mean_flux_error', FloatType(), True), # Mean G flux error
    StructField('phot_g_mean_mag', FloatType(), True), # Mean G magnitude
    StructField('phot_bp_mean_flux', FloatType(), True), # Mean BP flux
    StructField('phot_bp_mean_flux_error', FloatType(), True), # Mean BP flux error
    StructField('phot_bp_mean_mag', FloatType(), True), # Mean BP magnitude
    StructField('phot_rp_mean_flux', FloatType(), True), # Mean RP flux
    StructField('phot_rp_mean_flux_error', FloatType(), True), # Mean RP flux error
    StructField('phot_rp_mean_mag', FloatType(), True), # Mean RP magnitude
    StructField('phot_rvs_mean_flux', FloatType(), True), # Mean RVS flux
    StructField('phot_rvs_mean_flux_error', FloatType(), True), # Mean RVS flux error
    StructField('phot_rvs_mean_mag', FloatType(), True), # Mean RVS magnitude
    StructField('radial_velocity', FloatType(), True), # Radial velocity
    StructField('radial_velocity_error', FloatType(), True), # Radial velocity error
    StructField('teff', FloatType(), True), # Effective temperature
    StructField('teff_error', FloatType(), True), # Effective temperature error
    StructField('vsini', FloatType(), True), # v sin i
    StructField('vsini_error', FloatType(), True), # v sin i error
    StructField('a0', FloatType(), True), # Extinction at 550 nm
    StructField('a0_error', FloatType(), True), # Extinction at 550 nm error
    StructField('feh', FloatType(), True), # Iron abundance
    StructField('feh_error', FloatType(), True), # Iron abundance error
    StructField('logg', FloatType(), True), # Surface gravity
    StructField('logg_error', FloatType(), True), # Surface gravity Error
])
gaia_universe_model_schema = StructType([
    StructField('source_extended_id', StringType(), True), # Extended source identifier
    StructField('source_id', LongType(), False), # Long Identifier
    StructField('solution_id', LongType(), True), # Solution Identifier
    StructField('ra', DoubleType(), True), # Right Ascension
    StructField('dec', DoubleType(), True), # Declination
    StructField('barycentric_distance', FloatType(), True), # Barycentric distance to the simulated source
    StructField('pmra', FloatType(), True), # Proper motion along right ascension 
    StructField('pmdec', FloatType(), True), # Proper motion along declination
    StructField('radial_velocity', FloatType(), True), # Radial Velocity 
    StructField('mag_g', FloatType(), True), # Mean Apparent G magnitude
    StructField('mag_bp', FloatType(), True), # Mean Apparent BP magnitude
    StructField('mag_rp', FloatType(), True), # Mean Apparent RP magnitude
    StructField('mag_rvs', FloatType(), True), # Mean Apparent RVS magnitude
    StructField('v_i', FloatType(), True), # (V-I) colour
    StructField('mean_absolute_v', FloatType(), True), # Mean Absolute V magnitude
    StructField('ag', FloatType(), True), # Absorption in G
    StructField('av', FloatType(), True), # Absorption in V
    StructField('teff', FloatType(), True), # Effective temperature
    StructField('spectral_type', StringType(), True), # spectral class + luminosity class
    StructField('logg', FloatType(), True), # Surface gravity
    StructField('feh', FloatType(), True), # Metallicity
    StructField('alphafe', FloatType(), True), # Alpha elements
    StructField('mbol', FloatType(), True), # Absolute bolometric magnitude
    StructField('age', FloatType(), True), # Age
    StructField('mass', FloatType(), True), # Mass
    StructField('radius', FloatType(), True), # Radius
    StructField('vsini', FloatType(), True), # Rotational velocity
    StructField('population', IntegerType(), True), # Population
    StructField('has_photocenter_motion', BooleanType(), True), # Boolean describing if the photocenter has or not motion
    StructField('nc', IntegerType(), True), # Number of components
    StructField('nt', IntegerType(), True), # Total number of object
    StructField('semimajor_axis', FloatType(), True), # Semi major axis 
    StructField('eccentricity', FloatType(), True), # Eccentricity
    StructField('inclination', FloatType(), True), # Inclination
    StructField('longitude_ascending_node', FloatType(), True), # Longitude of ascending node
    StructField('orbit_period', FloatType(), True), # Period of the orbit
    StructField('periastron_date', FloatType(), True), # Date of periastron
    StructField('periastron_argument', FloatType(), True), # Periastron argument
    StructField('variability_type', StringType(), True), # Variability type
    StructField('variability_amplitude', FloatType(), True), # Amplitude of variability
    StructField('variability_period', FloatType(), True), # Period of variability
    StructField('variability_phase', FloatType(), True), # Phase of variability
    StructField('r_env_r_star', FloatType(), True), # Envelope characterisic for Be stars
])

# base folder for all release products
release_folder = 'GDR3'

# dictionary of all tables: key is table name, value = tuple(tuple of schema(s), subfolder containing parquet files)
table_dict = {
    #'vari_time_series_statistics',
    #'alerts_mixedin_sourceids',
    'astrophysical_parameters' : 
        ((astrophysical_parameters_schema), release_folder + '/GDR3_ASTROPHYSICAL_PARAMETERS'),
    'astrophysical_parameters_supp' : 
        ((astrophysical_parameters_supp_schema), release_folder + '/GDR3_ASTROPHYSICAL_PARAMETERS_SUPP'),
    'epoch_photometry' : 
        ((epoch_photometry_schema), release_folder + '/GDR3_EPOCH_PHOTOMETRY'),
    'gaia_source' : 
        ((gaia_source_schema), release_folder + '/GDR3_GAIA_SOURCE'),
    #'galaxy_candidates',
    #'galaxy_catalogue_name',
    'mcmc_samples_gsp_phot' : 
        ((mcmc_samples_gsp_phot_schema), release_folder + '/GDR3_MCMC_SAMPLES_GSP_PHOT'),
    'mcmc_samples_msc' : 
        ((mcmc_samples_msc_schema), release_folder + '/GDR3_MCMC_SAMPLES_MSC'),
    #'nss_acceleration_astro',
    #'nss_non_linear_spectro',
    #'nss_two_body_orbit',
    #'nss_vim_fl',
    'oa_neuron_information' : 
        ((oa_neuron_information_schema), release_folder + '/GDR3_OA_NEURON_INFORMATION'),
    'oa_neuron_xp_spectra' : 
        ((oa_neuron_xp_spectra_schema), release_folder + '/GDR3_OA_NEURON_XP_SPECTRA'),
    #'qso_candidates',
    #'qso_catalogue_name',
    'rvs_mean_spectrum' : 
        ((rvs_mean_spectrum_schema), release_folder + '/GDR3_RVS_MEAN_SPECTRUM'),
    #'science_alerts',
    #'sso_observation',
    #'sso_reflectance_spectrum',
    #'sso_source',
    'total_galactic_extinction_map' : 
        ((total_galactic_extinction_map_schema), release_folder + '/GDR3_TOTAL_GALACTIC_EXTINCTION_MAP'),
    'total_galactic_extinction_map_opt' : 
        ((total_galactic_extinction_map_opt_schema), release_folder + '/GDR3_TOTAL_GALACTIC_EXTINCTION_MAP_OPT'),
    #'vari_agn',
    #'vari_classifier_class_definition',
    #'vari_classifier_definition',
    #'vari_classifier_result',
    #'vari_compact_companion',
    #'vari_eclipsing_binary',
    #'vari_epoch_radial_velocity',
    #'vari_long_period_variable',
    #'vari_microlensing',
    #'vari_ms_oscillator',
    #'vari_planetary_transit',
    #'vari_rad_vel_statistics',
    #'vari_short_timescale',
    'xp_continuous_mean_spectrum' : 
        ([xp_continuous_mean_spectrum_schema], release_folder + '/GDR3_XP_CONTINUOUS_MEAN_SPECTRUM'),
    'xp_sampled_mean_spectrum' : 
        ([xp_sampled_mean_spectrum_schema], release_folder + '/GDR3_XP_SAMPLED_MEAN_SPECTRUM'),
    'xp_summary' : 
        ([xp_summary_schema], release_folder + '/GDR3_XP_SUMMARY'),
    #'commanded_scan_law',
    #'agn_cross_id',
    #'frame_rotator_source',
    #'gaia_crf3_xm',
    #'gaia_source_simulation' : 
    #    ([gaia_source_simulation_schema], release_folder + '/GDR3_GAIA_SOURCE_SIMULATION'),
    #'gaia_universe_model' : 
    #    ([gaia_universe_model_schema], release_folder + '/GDR3_UNIVERSE_MODEL'),
}
# ... small tables commented out: TODO decide later what to include.



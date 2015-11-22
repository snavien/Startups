NAME_IDX = 0
MARKET_IDX = 1
FUNDING_IDX = 2
STATUS_IDX = 3
COUNTRY_IDX = 4
BAYAREA_IDX = 5
ROUNDS_IDX = 6
FOUNDED_IDX = 7
FIRST_IDX = 8
LAST_IDX = 9

countryCodes = {
    'ISL' : 1, 'UKR' : 2, 'SVN' : 3, 'MEX' : 4, 'BGD' : 5,
    'ISR' : 6, 'NOR' : 7, 'PHL' : 8, 'MYS' : 9, 'CHN' : 10,
    'SYC' : 11, 'GHA' : 12, 'MAR' : 13, 'USA' : 14, 'TZA' : 15,
    'JOR' : 16, 'ARM' : 17, 'BWA' : 18, 'MDA' : 19, 'MUS' : 20,
    'GRC' : 21, 'LUX' : 22, 'LTU' : 23, 'HKG' : 24, 'CZE' : 25,
    'SRB' : 26, 'DNK' : 27, 'BMU' : 28, 'PRT' : 29, 'KHM' : 30,
    'ROM' : 31, 'OMN' : 32, 'KOR' : 33, 'IRL' : 34, 'TWN' : 35,
    'BGR' : 36, 'MMR' : 37, 'AUT' : 38, 'POL' : 39, 'LBN' : 40,
    'BHR' : 41, 'DOM' : 42, 'THA' : 43, 'ITA' : 44, 'CAN' : 45,
    'SLV' : 46, 'GBR' : 47, 'CHE' : 48, 'EGY' : 49, 'ESP' : 50,
    'GIB' : 51, 'NPL' : 52, 'CYM' : 53, 'BEL' : 54, 'MKD' : 55,
    'TUN' : 56, 'DZA' : 57, 'SVK' : 58, 'KEN' : 59, 'SWE' : 60,
    'DEU' : 61, 'NZL' : 62, 'CMR' : 63, 'BRA' : 64, 'ARE' : 65,
    'FIN' : 66, 'PER' : 67, 'CYP' : 68, 'CHL' : 69, 'CRI' : 70,
    'NLD' : 71, 'ARG' : 72, 'NGA' : 73, 'NIC' : 74, 'SAU' : 75,
    'MLT' : 76, 'HRV' : 77, 'BHS' : 78, 'AZE' : 79, 'SGP' : 80,
    'SOM' : 81, 'FRA' : 82, 'TUR' : 83, 'PAN' : 84, 'ECU' : 85,
    'BLR' : 86, 'COL' : 87, 'UGA' : 88, 'JPN' : 89, 'IND' : 90,
    'LVA' : 91, 'IDN' : 92, 'RUS' : 93, 'GTM' : 94, 'HUN' : 95,
    'AUS' : 96, 'MAF' : 97, 'EST' : 98, 'PAK' : 99
}

def processCountry(country):
    return countryCodes.get(country)

def processStatus(status):
    if(status == 'closed'):
        return -1
    if(status == 'operating'):
        return 1
    if(status == 'acquired'):
        return 1

def processRegion(region):
    if(region == 'SF Bay Area'):
        return 1
    else:
        return 0
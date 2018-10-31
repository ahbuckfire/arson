NFIRS_ARSON_REPORT_CODES = {
    "state,": "State",
    "fdid,": "Fire Dept. ID",
    "inc_date,": "Incident Date",
    "inc_no,": "Incident No.",
    "exp_no,": "Exposure No.",
    "version,": "Version",
    "case_stat,": "Case Satus",
    "avail_mfi,": "MFI Availability",
    "mot_facts1,": "Motivation 1",
    "mot_facts2,": "Motivation 2",
    "mot_facts3,": "Motivation 3",
    "grp_invol1,": "Group 1",
    "grp_invol2,": "Group 2",
    "grp_invol3,": "Group 3",
    "entry_meth,": "Entry Method",
    "ext_fire,": "Extent of Involvement",
    "devi_cont,": "Container",
    "devi_ignit,": "Ignition/Delay",
    "devi_fuel,": "Fuel",
    "inv_info1,": "Investigative Info. 1",
    "inv_info2,": "Investigative Info. 2",
    "inv_info3,": "Investigative Info. 3",
    "inv_info4,": "Investigative Info. 4",
    "inv_info5,": "Investigative Info. 5",
    "inv_info6,": "Investigative Info. 6",
    "inv_info7,": "Investigative Info. 7",
    "inv_info8,": "Investigative Info. 8",
    "prop_owner,": "Property Ownership",
    "init_ob1,": "Initial Observation 1",
    "init_ob2,": "Initial Observation 2",
    "init_ob3,": "Initial Observation 3",
    "init_ob4,": "Initial Observation 4",
    "init_ob5,": "Initial Observation 5",
    "init_ob6,": "Initial Observation 6",
    "init_ob7,": "Initial Observation 7",
    "init_ob8,": "Initial Observation 8",
    "lab_used1,": "Lab Used 1",
    "lab_used2,": "Lab Used 2",
    "lab_used3,": "Lab Used 3",
    "lab_used4,": "Lab Used 4",
    "lab_used5,": "Lab Used 5",
    "lab_used6,": "Lab Used 6",
    "serialid": "Serial ID"
}

ARSON_TO_CODEBOOK_KEY_MAPPING = {
    "Case Satus": "CASE_STATUS",
    "MFI Availability": "AVAILABILITY_OF_MATERIAL_FIRST_IGNITED",
    "Motivation 1": "SUSPECTED_MOTIVATION_FACTORS",
    "Motivation 2": "SUSPECTED_MOTIVATION_FACTORS",
    "Motivation 3": "SUSPECTED_MOTIVATION_FACTORS",
    "Group 1": "APPARENT_GROUP_INVOLVEMENT",
    "Group 2": "APPARENT_GROUP_INVOLVEMENT",
    "Group 3": "APPARENT_GROUP_INVOLVEMENT",
    "Extent of Involvement": "Extent of Fire Involvement Upon Arrival",
    "Container": "INCENDIARY_DEVICES",
    "Ignition/Delay": "IGNITION_DELAY_DEVICE",
    "Fuel": "FUEL",
    "Investigative Info. 1": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 2": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 3": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 4": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 5": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 6": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 7": "OTHER_INVESTIGATIVE_INFORMATION",
    "Investigative Info. 8": "OTHER_INVESTIGATIVE_INFORMATION",
    "Initial Observation 1": "INITIAL_OBSERVATIONS",
    "Initial Observation 2": "INITIAL_OBSERVATIONS",
    "Initial Observation 3": "INITIAL_OBSERVATIONS",
    "Initial Observation 4": "INITIAL_OBSERVATIONS",
    "Initial Observation 5": "INITIAL_OBSERVATIONS",
    "Initial Observation 6": "INITIAL_OBSERVATIONS",
    "Initial Observation 7": "INITIAL_OBSERVATIONS",
    "Initial Observation 8": "INITIAL_OBSERVATIONS",
    "Lab Used 1": "LABORATORY_USED",
    "Lab Used 2": "LABORATORY_USED",
    "Lab Used 3": "LABORATORY_USED",
    "Lab Used 4": "LABORATORY_USED",
    "Lab Used 5": "LABORATORY_USED",
    "Lab Used 6": "LABORATORY_USED",
    "Property Ownership": "PROPERTY_OWNERSHIP"
}

CASE_STATUS = {
    "1": "Investigation Open",
    "2": "Investigation Closed",
    "3": "Investigation Inactive",
    "4": "Closed with arrest",
    "5": "Closed with exceptional clearance"
}

AVAILABILITY_OF_MATERIAL_FIRST_IGNITED = {
    "1": "Transported to scene",
    "2": "Available at Scene",
    "U": "Unknown"
}

SUSPECTED_MOTIVATION_FACTORS = {
    "11": "Extortion",
    "12": "Labor unrest",
    "13": "Insurance fraud",
    "14": "Intimidation",
    "15": "Void contract/lease",
    "21": "Personal",
    "22": "Hate crime",
    "23": "Institutional",
    "24": "Societal",
    "31": "Protest",
    "32": "Civil unrest",
    "41": "Fireplay/curiosity",
    "42": "Vanity/recognition",
    "43": "Thrills",
    "44": "Attention/sympathy",
    "45": "Sexual excitement",
    "51": "Homicide",
    "52": "Suicide",
    "53": "Domestic violence",
    "54": "Burglary",
    "61": "Homicide concealment",
    "62": "Burglary concealment",
    "63": "Auto theft concealment",
    "64": "Destroy records/evidence",
    "00": "Other suspected motivation",
    "UU": "Unknown motivation"
}

APPARENT_GROUP_INVOLVEMENT = {
    "1": "Terrorist group",
    "2": "Gang",
    "3": "Anti-government group",
    "4": "Outlaw motorcycle organization",
    "5": "Organized crime",
    "6": "Racial/ethnic hate group",
    "7": "Religious hate group",
    "8": "Sexual preference hate group",
    "0": "Other group",
    "U": "Unknown"    
}

INCENDIARY_DEVICES = {
    "11": "glass bottle",
    "12": "plastic bottle",
    "13": "jug",
    "14": "pressurized container",
    "15": "can (not gas or fuel)",
    "16": "gasoline or fuel can",
    "17": "box",
    "00": "other container",
    "UU": "Unknown"
}

IGNITION_DELAY_DEVICE = {
    "11": "Wick or fuse",
    "12": "Candle",
    "13": "Cigarette and matchbook",
    "14": "Electronic component",
    "15": "Mechanical device",
    "16": "Remote control",
    "17": "Road flare/fuse",
    "18": "Chemical component",
    "19": "Trailer/streamer",
    "20": "Open flame source",
    "00": "Other delay device",
    "UU": "Unknown"
}

FUEL = {
    "11": "ordinary combustibles",
    "12": "flammable gas",
    "13": "ignitable liquid",
    "14": "ignitable solid",
    "16": "pyrotechnic material",
    "17": "explosive material",
    "00": "other material",
    "UU": "Unknown"
}

OTHER_INVESTIGATIVE_INFORMATION = {
    "1": "Code violations",
    "2": "Structure for sale",
    "3": "Structure vacant",
    "4": "Other crimes involved",
    "5": "Illicit drug activity",
    "6": "Change in insurance",
    "7": "Financial problem",
    "8": "Criminal/civil actions pending"
}

PROPERTY_OWNERSHIP = {
    "1": "private",
    "2": "city, town, village, local",
    "3": "county or parish",
    "4": "state or province",
    "5": "federal",
    "6": "foreign",
    "7": "military",
    "9": "other"
}

INITIAL_OBSERVATIONS = {
    "1": "Windows ajar",
    "2": "Doors ajar",
    "3": "Doors locked",
    "4": "Doors unlocked",
    "5": "Fire department forced entry",
    "6": "Entry forced prior to FD arrival",
    "7": "Security system activated",
    "8": "Security system present"
}

LABORATORY_USED = {
    "1": "local",
    "2": "state",
    "3": "ATF",
    "4": "FBI",
    "5": "other",
    "6": "private",
    "N": "None"
}

STATE_CODES = {"Mississippi": "MS", "Oklahoma": "OK", "Delaware": "DE", "Minnesota": "MN", "Illinois": "IL", "Arkansas": "AR", "New Mexico": "NM", "Indiana": "IN", "Maryland": "MD", "Louisiana": "LA", "Idaho": "ID", "Wyoming": "WY", "Tennessee": "TN", "Arizona": "AZ", "Iowa": "IA", "Michigan": "MI", "Kansas": "KS", "Utah": "UT", "Virginia": "VA", "Oregon": "OR", "Connecticut": "CT", "Montana": "MT", "California": "CA", "Massachusetts": "MA", "West Virginia": "WV", "South Carolina": "SC", "New Hampshire": "NH", "Wisconsin": "WI", "Vermont": "VT", "Georgia": "GA", "North Dakota": "ND", "Pennsylvania": "PA", "Florida": "FL", "Alaska": "AL", "Kentucky": "KY", "Hawaii": "HI", "Nebraska": "NE", "Missouri": "MO", "Ohio": "OH", "Alabama": "AK", "Rhode Island": "RI", "South Dakota": "SD", "Colorado": "CO", "New Jersey": "NJ", "Washington": "WA", "North Carolina": "NC", "New York": "NY", "Texas": "TX", "Nevada": "NV", "Maine": "ME"}
STATES = {"WA": "Washington", "DE": "Delaware", "WI": "Wisconsin", "WV": "West Virginia", "HI": "Hawaii", "FL": "Florida", "WY": "Wyoming", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "TX": "Texas", "LA": "Louisiana", "NC": "North Carolina", "ND": "North Dakota", "NE": "Nebraska", "TN": "Tennessee", "NY": "New York", "PA": "Pennsylvania", "CA": "California", "NV": "Nevada", "VA": "Virginia", "CO": "Colorado", "AK": "Alabama", "AL": "Alaska", "AR": "Arkansas", "VT": "Vermont", "IL": "Illinois", "GA": "Georgia", "IN": "Indiana", "IA": "Iowa", "OK": "Oklahoma", "AZ": "Arizona", "ID": "Idaho", "CT": "Connecticut", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "OH": "Ohio", "UT": "Utah", "MO": "Missouri", "MN": "Minnesota", "MI": "Michigan", "RI": "Rhode Island", "KS": "Kansas", "MT": "Montana", "MS": "Mississippi", "SC": "South Carolina", "KY": "Kentucky", "OR": "Oregon", "SD": "South Dakota"}

MONTHS = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

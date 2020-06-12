# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def update_damages(damages):
    upd_damages = []
    for data in damages:
        if data == 'Damages not recorded':
            upd_damages.append(data)
        else:
            conversion = {'B': 1000000000, 'M': 1000000}
            last_letter = data[-1]
            float_number = float(data.strip(last_letter)) * conversion[last_letter]
            upd_damages.append(float_number)
    return upd_damages

updated_damages = update_damages(damages)
print(updated_damages)

# write your construct hurricane dictionary function here:

def construct_hurricane_by_name(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes.update({names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}})
    return hurricanes

hurricanes = construct_hurricane_by_name(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

# write your construct hurricane by year dictionary function here:

def construct_hurricane_by_year(hurricanes):
    hurricanes_by_year = {}
    for keys in hurricanes.keys():
        current_cane = hurricanes[keys]
        current_year = current_cane['Year']
        if not current_year in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year

hurricanes_by_year = construct_hurricane_by_year(hurricanes)
print(hurricanes_by_year)

# write your count affected areas function here:

def frequency_in_areas(hurricanes):
    frequency_in_areas = {}
    for keys in hurricanes.keys():
        current_cane = hurricanes[keys]
        for area in current_cane['Areas Affected']:
            if not area in frequency_in_areas:
                frequency_in_areas[area] = 1
            else:
                frequency_in_areas[area] += 1
    return frequency_in_areas

frequency_in_areas = frequency_in_areas(hurricanes)
print(frequency_in_areas)

# write your find most affected area function here:

def most_affected_area(frequency_in_areas):
    most_affected_area = {'Area': 0}
    for key, value in frequency_in_areas.items():
        for defkey, defvalue in most_affected_area.items():
            if not key in most_affected_area:
                if value > defvalue:
                    most_affected_area.pop(defkey)
                    most_affected_area[key] = value
                if value == defvalue:
                    most_affected_area.update({key: value})
    return most_affected_area

most_affected_area = most_affected_area(frequency_in_areas)
print(most_affected_area)                

# write your greatest number of deaths function here:

def most_deadly_hurricane(hurricanes):
    most_deadly_hurricane = {'Hurricane': 0}
    for key in hurricanes.keys():
        current_cane = hurricanes[key]
        for defkey, defvalue in most_deadly_hurricane.items():
            if not key in most_deadly_hurricane:
                if current_cane['Deaths'] > defvalue:
                    most_deadly_hurricane.pop(defkey)
                    most_deadly_hurricane[key] = current_cane['Deaths']
                if current_cane['Deaths'] == defvalue:
                    most_deadly_hurricane.update({key: current_cane['Deaths']})
    return most_deadly_hurricane

most_deadly_hurricane = most_deadly_hurricane(hurricanes)
print(most_deadly_hurricane)
 
# write your catgeorize by mortality function here:

def mortality_rate(hurricanes):
    mortality_scale = {0: 0, 1: 100,2: 500, 3: 1000, 4: 10000}
    mortality_rate = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key in hurricanes.keys():
        current_cane = hurricanes[key]
        if mortality_scale[0] < current_cane['Deaths'] <= mortality_scale[1]:
            mortality_rate[1].append(current_cane)
        if mortality_scale[1] < current_cane['Deaths'] <= mortality_scale[2]:
            mortality_rate[2].append(current_cane)
        if mortality_scale[2] < current_cane['Deaths'] <= mortality_scale[3]:
            mortality_rate[3].append(current_cane)
        if mortality_scale[3] < current_cane['Deaths'] <= mortality_scale[4]:
            mortality_rate[4].append(current_cane)
        if current_cane['Deaths'] > mortality_scale[4]:
            mortality_rate[5].append(current_cane)
    return mortality_rate

mortality_rate = mortality_rate(hurricanes)
print(mortality_rate)

# write your greatest damage function here:

def most_costly_cane(hurricanes):
    most_costly_cane = {'Cane': 0}
    for key in hurricanes.keys():
        current_cane = hurricanes[key]
        for defkey, defvalue in most_costly_cane.items():
            if current_cane['Damage'] == 'Damages not recorded':
                None
            else:
                if current_cane['Damage'] > defvalue:
                    most_costly_cane.pop(defkey)
                    most_costly_cane[key] = current_cane['Damage']
                if current_cane['Damage'] == defvalue:
                    most_costly_cane.update({key: current_cane['Damage']})
    return most_costly_cane

most_costly_cane = most_costly_cane(hurricanes)
print(most_costly_cane)

# write your catgeorize by damage function here:

def damage_rate(hurricanes):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    damage_rate = {1: [], 2: [], 3: [], 4: [], 5: []}
    for key in hurricanes.keys():
        current_cane = hurricanes[key]
        damage = current_cane['Damage']
        if damage == 'Damages not recorded':
            None
        else:
            if damage_scale[0] < damage <= damage_scale[1]:
                damage_rate[1].append(current_cane)
            if damage_scale[1] < damage <= damage_scale[2]:
                damage_rate[2].append(current_cane)
            if damage_scale[2] < damage <= damage_scale[3]:
                damage_rate[3].append(current_cane)
            if damage_scale[3] < damage <= damage_scale[4]:
                damage_rate[4].append(current_cane)
            if damage > damage_scale[4]:
                damage_rate[5].append(current_cane)
    return damage_rate

damage_rate = damage_rate(hurricanes)
print(damage_rate)        
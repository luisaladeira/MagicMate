from ThemeParks import ThemeParks


def save_infos_about_all_destinations(ThemeParks : ThemeParks) -> None:
    destinations = ThemeParks.get_destinations()
    print('Salvando Complexos -> ', destinations)

def get_list_of_parks_in_locations(ThemeParks : ThemeParks, locations : list) -> list:
    list_parks = ThemeParks.get_parks_ids(locations)
    return list_parks

def save_info_about_parks(ThemeParks : ThemeParks, park_list : list) -> None:
    infos = ThemeParks.get_entity_infos(park_list)
    print('Salvando Infos de Parques -> ', infos)

def save_info_about_locations(ThemeParks : ThemeParks, locations_list : list) -> None:
    infos = ThemeParks.get_entity_infos(locations_list)
    print('Salvando Infos de Complexos -> ', infos)


def get_atractions_of_parks(ThemeParks : ThemeParks, park_list : list) -> None:
    park_atractions = []
    atractions = []
    for park_id in park_list:
        print(f'Buscando dados de: {park_id}')
        park_atractions = ThemeParks.get_entity_children(entity=park_id)
    
        for item in park_atractions['children']:
            atractions.append(item['id'])
    
    
    return atractions


def save_atractions_of_parks(ThemeParks : ThemeParks, park_list : list) -> None:
    atractions = get_atractions_of_parks(ThemeParks, park_list)
    print('Salvando Atrações de cada Parque -> ', atractions)


def save_info_about_atractions(ThemeParks : ThemeParks, atraction_list : list):
    infos = ThemeParks.get_entity_infos(atraction_list)
    print('Salvando Infos de atrações -> ', infos)


def save_atraction_live(ThemeParks : ThemeParks, park_list : list):
    live = []

    for park in park_list:
        print('Salvando Infos do parque -> ', park)
        dict_live = {}
        
        dict_live['park_id'] = park
        dict_live['live'] = ThemeParks.get_entity_live(entity=park)
        live.append(dict_live)

        return live
    
    print('Salvando Infos de Tempo de Espera dos Parques -> ', live)
    


def __main__():
    tp = ThemeParks()

    save_infos_about_all_destinations(tp)

    orlando_parks = ['e957da41-3552-4cf6-b636-5babc5cbc4e5', '89db5d43-c434-4097-b71f-f6869f495a22']
    park_list = get_list_of_parks_in_locations(tp, orlando_parks)

    save_info_about_locations(tp, orlando_parks)
    save_info_about_parks(tp, park_list)
    save_atractions_of_parks(tp, park_list)

    atraction_list = get_atractions_of_parks(tp, park_list)
    save_info_about_atractions(tp, atraction_list)
    save_atraction_live(tp, park_list)


from ThemeParks import ThemeParks


def save_infos_about_all_destinations(ThemeParks : ThemeParks) -> None:
    destinations = ThemeParks.get_destinations()

def get_list_of_parks_in_locations(ThemeParks : ThemeParks, locations : list) -> list:
    list_parks = ThemeParks.get_parks_ids(locations)
    return list_parks

def save_info_about_parks(ThemeParks : ThemeParks, park_list : list) -> None:
    infos = ThemeParks.get_entity_infos(park_list)

def save_info_about_locations(ThemeParks : ThemeParks, locations_list : list) -> None:
    infos = ThemeParks.get_entity_infos(locations_list)



def __main__():
    tp = ThemeParks()

    save_infos_about_all_destinations(tp)

    orlando_parks = ['e957da41-3552-4cf6-b636-5babc5cbc4e5', '89db5d43-c434-4097-b71f-f6869f495a22']
    park_list = get_list_of_parks_in_locations(tp, orlando_parks)

    save_info_about_locations(tp, orlando_parks)
    save_info_about_parks(tp, park_list)


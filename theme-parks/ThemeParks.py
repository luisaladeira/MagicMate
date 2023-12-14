import requests

class ThemeParks:
    def __init__(self):
        self.url_base = 'https://api.themeparks.wiki/v1'
        self.session = self.__create_session()

    
    def __create_session(self):
        session = requests.Session()
        session.headers.update({"Content-Type": "application/json"})
        return session

    
    def get_destinations(self):
        route = self.url_base + '/destinations'

        response = self.session.get(route)
        return response.json()

    
    def get_parks_ids(self, destinations_ids : list = []):
        destinations = self.get_destinations()['destinations']
        
        park_list = []
        
        for destination in destinations:
            if destinations_ids and destination['id'] in destinations_ids:
                park_list.extend([park['id'] for park in destination['parks']])
        
        return park_list
    
    
    def get_entity_infos(self, entity_list : list):
        route = self.url_base + '/entity/'
        infos_list = []
        
        for entity in entity_list:
            entity = self.session.get(route + entity)
            infos_list.append(entity)
        
        return infos_list
    

    def get_entity_children(self, entity):
        route = self.url_base + '/entity/' + entity + '/children'        
        response = self.session.get(route)

        return response.json()
    

    def get_entity_live(self, entity):
        route = self.url_base + '/entity/' + entity + '/live'        
        response = self.session.get(route)

        return response.json()
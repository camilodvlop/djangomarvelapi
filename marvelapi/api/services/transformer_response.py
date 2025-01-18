import re
class TransformResponse:
    @staticmethod
    def transform_response(response):
        
        transformed = {
            "code": response["code"],
            "status": response["status"],
            "copyright": response["copyright"],
            "attributionText": response["attributionText"],
            "attributionHTML": response["attributionHTML"],
            "etag": response["etag"],
            "results": []
            
        }

        for character in response["data"]["results"]:
            name = character["name"]
            series_items = character.get("series", {}).get("items", [])
            last_appearance = get_last_appearance(series_items)
            
            transformed["results"].append(
                "name: "+name+" last appearance: "+last_appearance
            )
        return transformed
        
def get_last_appearance(series_items):
    max_year = None
    last_appearance = "no encontrado"
    
    for item in series_items:
        # Buscar años dentro de paréntesis
        years = re.findall(r"\((\d{4})(?:\s*-\s*(\d{4}))?\)", item["name"])
        for start, end in years:
            # Considerar tanto el inicio como el fin del rango
            for year in [start, end]:
                if year:
                    year = int(year)
                    if max_year is None or year > max_year:
                        max_year = year
                        last_appearance = item["name"]
    
    return last_appearance
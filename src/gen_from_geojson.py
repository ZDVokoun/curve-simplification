import json
import numpy as np
import os
import matplotlib.pyplot as plt


for it in os.listdir():
    if (it[-8:] == ".geojson"):


        # Load the GeoJSON file
        with open(it) as f:
            geojson_data = json.load(f)

        # Function to extract coordinates from GeoJSON
        def extract_coordinates(geojson_data):
            # Check the type of GeoJSON geometry
            res = []
            for i in range(len(geojson_data['features'])):
                geom_type = geojson_data['features'][i]['geometry']['type']
                
                if geom_type == 'LineString':
                    # For LineString, extract the coordinates directly
                    res.append( geojson_data['features'][i]['geometry']['coordinates'])
                
                elif geom_type == 'Polygon':
                    # For Polygon, extract the outer boundary (first element in coordinates)
                    res.append( geojson_data['features'][i]['geometry']['coordinates'][0])

                else:
                    continue
                    # raise ValueError(f"Unsupported geometry type: {geom_type}")
            return res

        # Extract points from GeoJSON
        points = extract_coordinates(geojson_data)
        for i in range(len(points)):
            print(it[:-8], i)
            if len(points[i]) < 100:
                continue


            plt.scatter([p[0] for p in points[i]], [p[1] for p in points[i]])
            plt.plot([p[0] for p in points[i]], [p[1] for p in points[i]])
            plt.show()

            content = [f"{p[0]} {p[1]}\n" for p in points[i]]
            # print(content)
            with open("export/" + it[:-8] + str(i) + ".txt", "w") as f:
                f.writelines(content)
            # np.save(it[:-8] + str(i), np.array(points[i]))
        # print(points)

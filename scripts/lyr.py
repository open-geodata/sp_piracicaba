"""
Plano Diretor de Piracicaba
Configura Layers

"""




if __name__ == '__main__':
    from open_geodata import geo, lyr

    # Create Maps
    m = folium.Map(
        location=[-23.9619271, -46.3427499],
        zoom_start=10,
    )

    # Add Layers
    m.add_child(macrozona())
    m.add_child(divisa_abairramento())

    # Save/Open Map
    down_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    map_file = os.path.join(down_path, 'map_example.html')
    m.save(map_file)
    webbrowser.open(map_file)
    
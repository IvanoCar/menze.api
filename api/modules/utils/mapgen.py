import folium


def generateMAP():
    # marker_colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
    #                 'beige', 'darkblue', 'cadetblue', 'pink', 'lightblue', 'black']

    map = folium.Map(location=[45.327803, 14.466859], zoom_start=25)

    uni = folium.FeatureGroup("Fakulteti")
    kafici = folium.FeatureGroup("Kafici i restorani")
    ostalo = folium.FeatureGroup("Ostalo")

    universities = [

        '45.328616, 14.466992;Odjel za informatiku',
        '45.328744, 14.466724;Odjel za fiziku',
        '45.328599, 14.467199;Odjel za matematiku',
        '45.328524, 14.467014;Odjel za biotehnologiju',
        '45.328787, 14.467884;Gradevinski fakultet',
        '45.327956, 14.465935;Filozofski fakultet',
        '45.327036, 14.466727;Akademija primjenjennih umjetnosti'
    ]

    bars = [
        '45.328418, 14.467164;Formula',
        '45.328436, 14.468709;Akvarij',
        '45.328387, 14.469186;Restoran Kampus'
    ]

    various = [
        '45.328570, 14.466555;Sveucilisna knjiznica',
        '45.327752, 14.465455;PBZ, ZABA bankomat',
        '45.328785, 14.468049;Kopirnica',
        '45.327957, 14.465608;Kopirnica',
        '45.328549, 14.469771;Teretana',
        '45.328270, 14.469454;Recepcija domova',
        '45.327791, 14.469800;Studentski centar',
        '45.327700, 14.469864;Praonica'
    ]

    for univ in universities:
        location = (univ.split(sep=";")[0]).split(sep=", ")
        location = [float(no) for no in location]
        name = univ.split(sep=";")[1]
        pop = folium.Popup(folium.Html('<strong>%s</strong>' % name, script=True))
        uni.add_child(folium.Marker(location=location, popup=pop, icon=folium.Icon(color='red')))

    for kaf in bars:
        location = (kaf.split(sep=";")[0]).split(sep=", ")
        location = [float(no) for no in location]
        name = kaf.split(sep=";")[1]
        pop = folium.Popup(folium.Html('<strong>%s</strong>' % name, script=True))
        kafici.add_child(folium.Marker(location=location, popup=pop, icon=folium.Icon(color='blue')))

    for ost in various:
        location = (ost.split(sep=";")[0]).split(sep=", ")
        location = [float(no) for no in location]
        name = ost.split(sep=";")[1]
        pop = folium.Popup(folium.Html('<strong>%s</strong>' % name, script=True))
        ostalo.add_child(folium.Marker(location=location, popup=pop, icon=folium.Icon(color='green')))

    map.add_child(uni)
    map.add_child(kafici)
    map.add_child(ostalo)

    map.add_child(folium.LayerControl())
    map.save("../../templates/kampus-map.html")

# generateMAP()

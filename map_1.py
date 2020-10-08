import folium

# Create map object
m = folium.Map(location=[-26.274030, 28.451350], zoom_start=12) # the coordinates of the map object in latitude and longitude inside 'location'
# The above coordinates are for McDonald's at Springs Cnr Wit and Jan Smuts, Casseldale, Springs 1560, South Africa

# Global tootip
tooltip = 'Click For More Info'

# Create markers
# the coordinates of the tooltip, what the popup will say, the tooltip that will display additional info 
folium.Marker([-26.274030, 28.451350], popup='<strong>McDonalds Springs Cnr Wit and Jan Smuts,<br> Casseldale, Springs 1560,<br> South Africa</strong>', tooltip=tooltip).add_to(m)

# Generate the map that is going to display the HTML, fontawesome, leaflet and javascript dependencies involved
m.save('map.html') # Generate a file called ...

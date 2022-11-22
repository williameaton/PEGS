% Plot receiver and source locations for PEGS study
clc 
clear all 
close all 


src_lat = [-13.8200];
src_lon = [-67.2500];
   
lat = [-11.9875, -19.158199, -16.287901] ;
lon = [-76.8422 , -65.068703 , -68.130692]; 
dx = 1
dy = 1

names = ["NNA", "YUNZ", "LPAZ"]

geoscatter(src_lat, src_lon, 100, 'r', 'filled', "o")
hold on 

geoscatter(lat, lon, 100, 'b', 'filled', '^' )
geobasemap colorterrain

text(src_lat + 0.4, src_lon+0.2, 'Epicentre', 'BackgroundColor', 'white');

text(lat(1) + 0.4, lon(1)+0.2, 'NNA', 'BackgroundColor', 'white');
text(lat(2) + 0.5, lon(2)-1 , 'YUNZ', 'BackgroundColor', 'white'); 
text(lat(3) + 0.6, lon(3)+0.2, 'LPAZ', 'BackgroundColor', 'white'); 


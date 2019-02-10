1)The module is intended for visualization of locations on the world map, where the films of the specified year were shot, and the most populated cities of 2018.


2)<!DOCTYPE html> - specifies the type of document and provides basic information for the browser
<head>    - "the head file", container for data such as link, title, script, style ...
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> - stores additional page information for the browser, http-equiv accepts the value of 
									    the document encoding type, charset = UTF-8 assigns character encoding
    <script>L_PREFER_CANVAS=false; L_NO_TOUCH=false; L_DISABLE_3D=false;</script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.js"></script> - contains a link to the code
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.css"/> - css connects
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style> - defines "body" parameters
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style> -  defines the map parameters
    
    <meta name="viewport" content="width=device-width,
        initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <style>#map_147321a759604fe09a8e2c9a58cab68a { - define the map parametrs
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style>
</head>
<body>    - "the body of the file" - the main content
    
    <div class="folium-map" id="map_147321a759604fe09a8e2c9a58cab68a" ></div> - defines class folium map and its id
</body>
<script>    - "JavaScript code"


3) Conclusion: During the performance of the laboratory work, it was investigated that the most famous films were shot in North America and Europe, 
as well as the fact that the most populated cities are situated in Asia.
from PIL import Image
from sense_hat import SenseHat
import ephem
from datetime import datetime
import time
import math
import os
from picamera import PiCamera

sense = SenseHat ()

white = ( 255, 255, 255 )
red = ( 255, 0, 0 )
black = ( 0, 0, 0 )
dark_green = ( 0, 100, 0 )
dark_goldenrod = ( 184, 134, 11 )
yellow = ( 255, 255, 0 )
lawn_green = ( 124, 252, 0 )
hot_pink = ( 255, 105, 180 )
orange_red = ( 255, 69, 0 )
firebrick = ( 178, 34, 34 )
blue = ( 0, 0, 255 ) 
light_blue = ( 135, 206, 250 )
mauve = ( 194, 100, 255 )
indigo = ( 75, 0, 130 )
orange = ( 255, 165, 0 )

# http://www.celestrak.com/NORAD/elements/stations.txt

iss = ephem.readtle ( "ISS (ZARYA)",           
"1 25544U 98067A   18037.81619667  .00001858  00000-0  35391-4 0  9990",
"2 25544  51.6418 308.6383 0003223  81.0254  25.3342 15.54063142 98241" )

point = [
( "United Kingdom", "London", 51.5002, -0.126236, 14.6055 ),
( "France", "Paris", 48.8567, 2.35099, 35.917 ),
( "United States", "New York", 40.7144, -74.006, 9.77569 ),
( "Japan", "Tokyo", 35.6895, 139.692, 37.1454 ),
( "United States", "Chicago", 41.8781, -87.6298, 181.319 ),
( "Germany", "Frankfurt", 50.1115, 8.68051, 106.258 ),
( "Hong Kong", "Hong Kong", 22.3964, 114.109, 321.11 ),
( "United States", "Los Angeles", 34.0522, -118.244, 86.8471 ),
( "Italy", "Milan", 45.4637, 9.18814, 122.247 ),
( "Singapore", "Singapore", 1.35208, 103.82, 57.8216 ),
( "United States", "San Francisco", 37.7749, -122.419, 15.5578 ),
( "Australia", "Sydney", -33.86, 151.211, 3.34103 ),
( "Canada", "Toronto", 43.6525, -79.3817, 90.2394 ),
( "Switzerland", "Zurich", 47.3833, 8.53333, 405.501 ),
( "Belgium", "Brussels", 50.8503, 4.35171, 26.8086 ),
( "Spain", "Madrid", 40.4167, -3.70035, 653.005 ),
( "Mexico", "Mexico City", 19.427, -99.1276, 2228.15 ),
( "Brazil", "Sao Paulo", -23.5489, -46.6388, 760.345 ),
( "Russian Federation", "Moscow", 55.7558, 37.6176, 151.19 ),
( "South Korea", "Seoul", 37.5665, 126.978, 41.9809 ),
( "The Netherlands", "Amsterdam", 52.3731, 4.89222, 14.9755 ),
( "United States", "Boston", 42.3584, -71.0598, 15.3388 ),
( "Venezuela", "Caracas", 10.491, -66.9021, 974.727 ),
( "United States", "Dallas", 32.803, -96.7699, 154.141 ),
( "Germany", "Dusseldorf", 51.2249, 6.77565, 43.2048 ),
( "Switzerland", "Geneva", 46.2058, 6.14159, 379.026 ),
( "United States", "Houston", 29.7629, -95.3831, 6.91662 ),
( "South Africa", "Johannesburg", -26.1704, 27.9718, 1687.25 ),
( "Australia", "Melbourne", -37.8132, 144.963, 27 ),
( "Japan", "Osaka", 34.6937, 135.502, 16.3478 ),
( "Czech Republic", "Prague", 50.0878, 14.4205, 191.103 ),
( "Chile", "Santiago", -33.4254, -70.5665, 665.927 ),
( "Taiwan", "Taipei", 25.0911, 121.56, 32.2886 ),
( "United States", "Washington", 38.8951, -77.0364, 7.11964 ),
( "Thailand", "Bangkok", 13.7234, 100.476, 4.0901 ),
( "China", "Beijing", 39.9042, 116.407, 51.8589 ),
( "Canada", "Montreal", 45.5089, -73.5542, 16.6209 ),
( "Italy", "Rome", 41.8955, 12.4823, 19.7044 ),
( "Sweden", "Stockholm", 59.3328, 18.0645, 25.5959 ),
( "Poland", "Warsaw", 52.2297, 21.0122, 115.028 ),
( "United States", "Atlanta", 33.749, -84.388, 319.95 ),
( "Spain", "Barcelona", 41.3879, 2.16992, 19.9911 ),
( "Germany", "Berlin", 52.5234, 13.4114, 45.0139 ),
( "Argentina", "Buenos Aires", -34.6084, -58.3732, 40.5441 ),
( "Hungary", "Budapest", 47.4984, 19.0408, 106.463 ),
( "Denmark", "Copenhagen", 55.6934, 12.583, 6.72672 ),
( "Germany", "Hamburg", 53.5538, 9.99158, 5.10463 ),
( "Turkey", "Istanbul", 41.0053, 28.977, 37.3143 ),
( "Malaysia", "Kuala Lumpur", 3.139, 101.687, 52.2717 ),
( "Philippines", "Manila", 14.5833, 120.967, 3.04138 ),
( "United States", "Miami", 25.789, -80.2264, 0.946764 ),
( "United States", "Minneapolis", 44.98, -93.2638, 253.003 ),
( "Germany", "Munich", 48.1391, 11.5802, 523 ),
( "China", "Shanghai", 31.2304, 121.474, 15.9047 ),
( "Greece", "Athens", 37.9792, 23.7166, 47.5971 ),
( "New Zealand", "Auckland", -36.8485, 174.763, 21 ),
( "Ireland", "Dublin", 53.3441, -6.26749, 8.21432 ),
( "Finland", "Helsinki", 60.1698, 24.9382, 7.15331 ),
( "Luxembourg", "Luxembourg", 49.8153, 6.12958, 305.748 ),
( "France", "Lyon", 45.7673, 4.83433, 182.811 ),
( "India", "Mumbai", 19.0176, 72.8562, 12.4088 ),
( "India", "New Delhi", 28.6353, 77.225, 213.999 ),
( "United States", "Philadelphia", 39.9523, -75.1638, 12.4657 ),
( "Brazil", "Rio de Janeiro", -22.9035, -43.2096, 9.52193 ),
( "Israel", "Tel Aviv", 32.0599, 34.7851, 21.1142 ),
( "Austria", "Vienna", 48.2066, 16.3828, 170.493 ),
( "United Arab Emirates", "Abu Dhabi", 24.4667, 54.3667, 6.29604 ),
( "Kazakhstan", "Almaty", 43.2551, 76.9126, 785.522 ),
( "United Kingdom", "Birmingham", 52.483, -1.89359, 141.449 ),
( "Colombia", "Bogota", 4.59806, -74.0758, 2614.04 ),
( "Slovakia", "Bratislava", 48.1484, 17.1073, 155.813 ),
( "Australia", "Brisbane", -27.4709, 153.024, 28.1639 ),
( "Romania", "Bucharest", 44.4377, 26.0974, 80.4078 ),
( "Egypt", "Cairo", 30.0647, 31.2495, 20.248 ),
( "United States", "Cleveland", 41.4995, -81.6954, 198.88 ),
( "Germany", "Cologne", 50.9407, 6.95991, 59.1814 ),
( "United States", "Detroit", 42.3314, -83.0458, 182.763 ),
( "United Arab Emirates", "Dubai", 25.2644, 55.3117, 8.02923 ),
( "Vietnam", "Ho Chi Minh City", 10.7592, 106.662, 10.7571 ),
( "Ukraine", "Kiev", 50.45, 30.5233, 157.21 ),
( "Peru", "Lima", -12.0433, -77.0283, 154.334 ),
( "Portugal", "Lisbon", 38.7071, -9.13549, 2.88018 ),
( "United Kingdom", "Manchester", 53.4807, -2.23438, 57.8924 ),
( "Uruguay", "Montevideo", -34.8833, -56.1667, 45.005 ),
( "Norway", "Oslo", 59.9127, 10.7461, 10.5023 ),
( "The Netherlands", "Rotterdam", 51.9242, 4.48178, 2.76627 ),
( "Saudi Arabia", "Riyadh", 24.688, 46.7224, 613.475 ),
( "United States", "Seattle", 47.6062, -122.332, 53.5055 ),
( "Germany", "Stuttgart", 48.7771, 9.18077, 249.205 ),
( "The Netherlands", "The Hague", 52.0699, 4.29111, 3.68669 ),
( "Canada", "Vancouver", 49.2485, -123.109, 70.1459 ),
( "Australia", "Adelaide", -34.9306, 138.621, 49.0984 ),
( "Belgium", "Antwerp", 51.2199, 4.39625, 7.29688 ),
( "Denmark", "Arhus", 56.1629, 10.2039, 26.8794 ),
( "United States", "Baltimore", 39.2904, -76.6122, 10.2589 ),
( "India", "Bangalore", 12.9716, 77.5946, 911.858 ),
( "Italy", "Bologna", 44.4942, 11.3465, 72.8759 ),
( "Brazil", "Brazilia", -14.235, -51.9253, 259.063 ),
( "Canada", "Calgary", 51.045, -114.057, 1046 ),
( "South Africa", "Cape Town", -33.9248, 18.4299, 5.83845 ),
( "Sri Lanka", "Colombo", 6.92747, 79.8484, 9.97 ),
( "United States", "Columbus", 39.9612, -82.9988, 237.652 ),
( "Germany", "Dresden", 51.051, 13.7336, 114.032 ),
( "United Kingdom", "Edinburgh", 55.9502, -3.18754, 84.454 ),
( "Italy", "Genoa", 44.4071, 8.93399, 35.4181 ),
( "United Kingdom", "Glasgow", 55.8656, -4.25722, 38.0469 ),
( "Sweden", "Gothenburg", 57.697, 11.9865, 15.9863 ),
( "China", "Guangzhou", 23.1292, 113.264, 18.8929 ),
( "Vietnam", "Hanoi", 21.0333, 105.85, 20.009 ),
( "United States", "Kansas City", 39.1067, -94.6764, 274.249 ),
( "United Kingdom", "Leeds", 53.7996, -1.54912, 47.7624 ),
( "France", "Lille", 50.6372, 3.06302, 28.1395 ),
( "France", "Marseille", 43.2976, 5.38104, 24.7858 ),
( "United States", "Richmond", 37.543, -77.4691, 63.6245 ),
( "Russian Federation", "St. Petersburg", 59.939, 30.3158, 11.503 ),
( "Uzbekistan", "Tashkent", 41.2667, 69.2167, 430.668 ),
( "Iran", "Tehran", 35.6961, 51.4231, 1180.6 ),
( "Mexico", "Tijuana", 32.5335, -117.018, 22.712 ),
( "Italy", "Turin", 45.0706, 7.68662, 234 ),
( "The Netherlands", "Utrecht", 52.0901, 5.10966, 7.72088 ),
( "New Zealand", "Wellington", -41.2925, 174.773, 17 )
]

white = 1
black = 0

sens = 150

font_size = 20

x = 640
y = 480

max_surf = -1

dat_ind = 0
nstars = 0
ind = 0
iss_lat = iss_lon = 0

color = [ [ 0 for i in range ( y ) ] for j in range ( x ) ]
went =  [ [ 0 for i in range ( y ) ] for j in range ( x ) ]
data = [ ( 0, 0, 0, 0, 0, 0 ) for i in range ( x * y ) ] # where does each point start, surface, red avg, yellow avg, pollution coefficient
q_x = [ 0 for i in range ( x * y ) ]
q_y = [ 0 for i in range ( x * y ) ]
dir_x = [ 0 for i in range ( 8 ) ]
dir_y = [ 0 for i in range ( 8 ) ]
red_param = [ [ 0 for i in range ( y ) ] for j in range ( x ) ]
yel_param = [ [ 0 for i in range ( y ) ] for j in range ( x ) ]
font = [ [ [ 0 for i in range ( 37 ) ] for j in range ( font_size ) ] for k in range ( font_size ) ]
pix = [ [ 0 for i in range ( y ) ] for j in range ( x ) ]
grd = [ [ 0 for i in range ( y ) ] for j in range ( x ) ]
sns = [ [ 0 for i in range ( y ) ] for j in range ( x ) ]

def ndigits ( n ) :
    if n == 0 :
        return 1
    else :
        c = 0
        while n > 0 :
            c += 1
            n = int ( n / 10 )

        return c

def put_png ( cl, ln, v ) :
    global sns

    im = Image.open ( "numbers/" + v + ".png" )
    im = im.convert ( "RGB" )
    pix = im.load ()
    x, y = im.size

    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            sns[ cl + i, ln + j ] = pix [ i, j ]

    im.close ()    

def sense_data ( cyc, hmd, tmp, prs, vibr, spd, iss_lat, iss_lon, time ) : # hmd, tmp, prs, vibr, spd, iss_lat, iss_lon, time
    global sns
    global font_size
    
    im = Image.open ( "initial_data/sense_data.png" )
    im = im.convert ( "RGB" )
    sns = im.load ()
    # humidity
    write_text ( font_size, font_size, "HUMIDITY", 2 )
    put_png ( font_size * 9, font_size, "Zdouble_point" )
    write_text ( font_size * 11, font_size, str ( hmd ), 2 )
    put_png ( font_size * 14, font_size, "Zpercentage" )

    for i in range ( 0, hmd + 1 ) :
        put_png ( font_size + i * 4, font_size * 3, "ZZhmd_full" )
    for i in range ( hmd + 1, 100 ) :
        put_png ( font_size + i * 4, font_size * 3, "ZZhmd_empty" )
        
    # temperature
    write_text ( font_size, font_size * 5, "TEMPERATURE", 2 )
    put_png ( font_size * 12, font_size * 5, "Zdouble_point" )
    write_text ( font_size * 14, font_size * 5, str ( tmp ), 2 )
    put_png ( font_size * 17, font_size * 5, "Zdegree" )

    for i in range ( 0, tmp + 1 ) :
        put_png ( font_size + i * 4, font_size * 7, "ZZtmp_full" )
    for i in range ( tmp + 1, 100 ) :
        put_png ( font_size + i * 4, font_size * 7, "ZZtmp_empty" )
        
    # pressure
    write_text ( font_size, font_size * 9, "PRESSURE", 2 )
    put_png ( font_size * 9, font_size * 9, "Zdouble_point" )
    write_text ( font_size * 11, font_size * 9, str ( prs ), 2 )
    put_png ( font_size * 15, font_size * 9, "Zmbar" )

    prs = int ( ( prs - 800 ) / 4 )
    for i in range ( 0, prs + 1 ) :
        put_png ( font_size + i * 4, font_size * 11, "ZZprs_full" )
    for i in range ( prs + 1, 100 ) :
        put_png ( font_size + i * 4, font_size * 11, "ZZprs_empty" )
    
    # vibration
    write_text ( font_size, font_size * 13, "VIBRATION", 2 )
    put_png ( font_size * 10, font_size * 13, "Zdouble_point" )
    write_text ( font_size * 12, font_size * 13, str ( int ( vibr ) ), 2 )

    nd = ndigits ( int ( vibr ) )
    
    put_png ( font_size * ( 12 + nd ), font_size * 13, "Zpoint" )

    dig3 = int ( vibr * 1000 ) % 1000

    n0 = 0
    if ( ndigits ( dig3 ) < 3 ) :
        n0 = 3 - ndigits ( dig3 )
        for i in range ( 0, n0 ) :
            put_png ( font_size * ( 13 + nd + i ), font_size * 13, "0" )
    
    write_text ( font_size * ( 13 + nd + n0 ), font_size * 13, str ( dig3 ), 2 )
    put_png ( font_size * ( 16 + nd + n0 ), font_size * 13, "Zacceleration" )

    vibr = int ( vibr * 100 )
    for i in range ( 0, min ( vibr + 1, 100 ) ) :
        put_png ( font_size + i * 4, font_size * 15, "ZZvibr_full" )
    for i in range ( min ( vibr + 1, 100 ), 100 ) :
        put_png ( font_size + i * 4, font_size * 15, "ZZvibr_empty" )
    
    # speed

    nd = ndigits ( int ( spd ) )
    
    write_text ( font_size, font_size * 17, "SPEED", 2 )
    put_png ( font_size * 6, font_size * 17, "Zdouble_point" )
    write_text ( font_size * 8, font_size * 17, str ( int ( spd ) ), 2 )
    put_png ( font_size * ( 8 + nd ), font_size * 17, "Zpoint" )

    dig3 = int ( spd * 1000 ) % 1000

    n0 = 0
    if ( ndigits ( dig3 ) < 3 ) :
        n0 = 3 - ndigits ( dig3 )
        for i in range ( 0, n0 ) :
            put_png ( font_size * ( 9 + nd + i ), font_size * 17, "0" )
    
    write_text ( font_size * ( 9 + nd + n0 ), font_size * 17, str ( dig3 ), 2 )
    put_png ( font_size * ( 12 + nd + n0 ), font_size * 17, "Zspeed" )

    # lat

    write_text ( font_size, font_size * 19, "LAT", 2 )
    put_png ( font_size * 4, font_size * 19, "Zdouble_point" )

    if iss_lat < 0 :
        put_png ( font_size * 5, font_size * 19, "Zminus" )
        iss_lat = abs ( iss_lat )
        
    nd = ndigits ( int ( iss_lat ) )

    print ( nd )

    write_text ( font_size * 6, font_size * 19, str ( int ( iss_lat ) ), 2 )
    put_png ( font_size * ( 6 + nd ), font_size * 19, "Zpoint" )

    dig3 = int ( iss_lat * 1000 ) % 1000

    n0 = 0
    if ( ndigits ( dig3 ) < 3 ) :
        n0 = 3 - ndigits ( dig3 )
        for i in range ( 0, n0 ) :
            put_png ( font_size * ( 7 + nd + i ), font_size * 19, "0" )
    
    write_text ( font_size * ( 7 + nd + n0 ), font_size * 19, str ( dig3 ), 2 )
    
    # lon

    amt = font_size * ( 11 + nd )
    
    write_text ( amt, font_size * 19, "LON", 2 )
    put_png ( amt + font_size * 4, font_size * 19, "Zdouble_point" )

    if iss_lon < 0 :
        put_png ( amt + font_size * 5, font_size * 19, "Zminus" )
        iss_lon = abs ( iss_lon )
        
    nd = ndigits ( int ( iss_lon ) )    

    write_text ( amt + font_size * 6, font_size * 19, str ( int ( iss_lon ) ), 2 )
    put_png ( amt + font_size * ( 6 + nd ), font_size * 19, "Zpoint" )

    dig3 = int ( iss_lon * 1000 ) % 1000

    n0 = 0
    if ( ndigits ( dig3 ) < 3 ) :
        n0 = 3 - ndigits ( dig3 )
        for i in range ( 0, n0 ) :
            put_png ( amt + font_size * ( 7 + nd + i ), font_size * 19, "0" )
    
    write_text ( amt + font_size * ( 7 + nd + n0 ), font_size * 19, str ( dig3 ), 2 )

    # time
    write_text ( font_size, font_size * 21, "TIME", 2 )
    put_png ( font_size * 5, font_size * 21, "Zdouble_point" )
    
    time = int ( time )
    
    write_text ( font_size * 7, font_size * 21, str ( time ), 2 )

    nd = ndigits ( time )

    write_text ( font_size * ( 8 + nd ), font_size * 21, "S", 2 )

    out = "mid_data/"
    im.save ( out + "image3_" + str ( cyc ) + ".png" )
    
def calcdist ( lat1, lon1, lat2, lon2 ) :
    rpd = math.pi / 180

    lat1 *= rpd
    lat2 *= rpd
    lon1 *= rpd
    lon2 *= rpd
    
    p1 = 0.5 * ( 1 - math.cos ( lat2 - lat1 ) ) + math.cos ( lat1 ) * math.cos ( lat2 ) * 0.5 * ( 1 - math.cos ( lon2 - lon1 ) )
    r = 6370 
    
    return abs ( 2 * r * math.asin ( math.sqrt ( p1 ) ) )

def calc_nearest_city () :    
    dpr = 180 / math.pi
    
    orig = ephem.Observer ()
    orig.date = datetime.utcnow ()

    iss.compute ()

    iss_lat = iss.sublat * dpr
    iss_lon = iss.sublong * dpr

    print ( iss_lat, iss_lon )
    
    dist = 0
    distmin = 9999999
    pmin = 0

    for i in range ( 0, 121 ) :
        country, city, lat, lon, alt = point[i]
    
        #dist =  math.sqrt ( ( lat - iss_lat ) ** 2 + ( lon - iss_lon ) ** 2 )
        dist = calcdist ( lat / dpr, lon / dpr, iss_lat / dpr, iss_lon / dpr )
    
        if dist < distmin :
            distmin = dist
            pmin = i

    bundle = ( pmin, iss_lat, iss_lon )

    return bundle

def latlon2d ( lat, lon ) :
    cl0 = 37
    ln0 = 24

    len_cl = 23 / 15
    len_ln = 29 / 15
    
    lat = 90 - int ( lat )
    lon = int ( lon ) + 180
    
    lon = int ( cl0 + len_cl * lon )
    lat = int ( ln0 + len_ln * lat )

    bundle = ( lat, lon )

    return bundle

def draw_point ( cl, ln, r, g, b ) :
    global grd

    for i in range ( -2, 3 ) :
        for j in range ( -2, 3 ) :
            grd[ cl + i, ln + j ] = r, g, b

def load_font () :
    global font
    global font_size

    for k in range ( 0, 10 ) :
        im = Image.open ( "numbers/" + str ( k ) + ".png" ) 
        pix = im.load()

        for i in range ( 0, font_size ) :
            for j in range ( 0, font_size ) :
                font[i][j][k] = pix[ i, j ]

        im.close ()

    for k in range ( 0, 26 ) :
        im = Image.open ( "numbers/" + chr ( k + 65 ) + ".png" ) 
        pix = im.load()

        for i in range ( 0, font_size ) :
            for j in range ( 0, font_size ) :
                font[i][j][ k + 10 ] = pix[ i, j ]

        im.close ()

    im = Image.open ( "numbers/Zspace.png" )
    pix = im.load ()

    for i in range ( 0, font_size ) :
        for j in range ( 0, font_size ) :
            font[i][j][ 36 ] = pix[ i, j ]

    im.close ()

def decode_char ( a ) :
    #print ( a, ord ( a ), int ( a ) )
    if ord ( a ) == 32 :
        return 36
    elif ord ( a ) - ord ( '0' ) >= 0 and ord ( a ) - ord ( '0' ) <= 9 :
        return int ( a )
    else :
        return ord ( a ) - 65 + 10

def write_text ( cl, ln, v, which ) :
    global font
    global pix
    global grd
    global sns
    global font_size

    sz = len ( v )

    if cl + sz * font_size >= 640 :
        cl = 638 - sz * font_size

    if ln + font_size >= 480 :
        ln = 478 - font_size

    if ln < 0 :
        ln = 0
        
    for k in range ( 0, sz ) :
        #print ( v[k], decode_char ( v[k] ) ) 
        for i in range ( 0, font_size ) :
            for j in range ( 0, font_size ) :
                if which == 0 :
                    pix[ cl + k * font_size + i, ln + j ] = font[i][j][ decode_char ( v[k] ) ]
                elif which == 1 :
                    grd[ cl + k * font_size + i, ln + j ] = font[i][j][ decode_char ( v[k] ) ]
                else :
                    sns[ cl + k * font_size + i, ln + j ] = font[i][j][ decode_char ( v[k] ) ]
                
def bfs ( i, j, should_color ) :
    global q_x, q_y, data
    global x, y
    global dat_ind
    global pix
    global max_surf
    
    pr = 0
    ul = 0

    q_x[pr] = i
    q_y[pr] = j

    ln = 0
    cl = 0

    ind_ln = 0
    ind_cl = 0

    red_avg = 0
    yel_avg = 0
    
    while pr <= ul :
        cl = q_x[pr]
        ln = q_y[pr]

        if should_color != -1 :
            pix [ cl, ln ] = should_color, 0, 0

        for ind_cl in range ( -2, 3 ) :
            for ind_ln in range ( -2, 3 ) :
                cl = q_x[pr] + ind_cl
                ln = q_y[pr] + ind_ln
                        
                if cl >= 0 and cl < x and ln >= 0 and ln < y and went[cl][ln] == 0 and color[cl][ln] == white :
                    red_avg += red_param[cl][ln]
                    yel_avg += yel_param[cl][ln]
                    
                    ul += 1
                    went[cl][ln] = 1
                    q_x[ul] = cl
                    q_y[ul] = ln  
        
        pr += 1

    red_avg /= ( ul + 1 )
    yel_avg /= ( ul + 1 )
    
    data[dat_ind] = [ ul + 1, i, j, int ( red_avg ), int ( yel_avg ), 0 ]

    if ul + 1 > max_surf :
        max_surf = ul + 1

    dat_ind += 1

def sort_a_list ( nstars, ind ) :
    global data

    a1 = [ 0 for i in range ( 0, 6 ) ]
    a2 = [ 0 for i in range ( 0, 6 ) ]
    
    for i in range ( 0, nstars ) :
        for j in range ( i + 1, nstars ) :
            a1[0], a1[1], a1[2], a1[3], a1[4], a1[5] = data[i]
            a2[0], a2[1], a2[2], a2[3], a2[4], a2[5] = data[j]

            if a1[ind] < a2[ind] :
                data[i] = ( a2[0], a2[1], a2[2], a2[3], a2[4], a2[5] )
                data[j] = ( a1[0], a1[1], a1[2], a1[3], a1[4], a2[5] )

# 1st part
def light_pollution ( cyc ) :
    global pix
    global red_param
    global yel_param
    global color
    global went
    global data
    global point

    global dat_ind
    global iss_lat, iss_lon
    global white, black
    global sens
    global nstars
    global max_surf
    global font_size

    folder = "photos/"
    str_img = "photo0_" + str ( cyc )
    ext = ".jpg"

    im = Image.open ( folder + str_img + ext ) # Can be many different formats.
    im = im.convert ( "RGB" )
    pix = im.load()
    x, y = im.size

    #print ( x, y )

    # polarise the picture
    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            r, g, b = pix [ i, j ]

            red_param[i][j] = r
            yel_param[i][j] = g

            if r >= 255 - sens and g >= 255 - sens : # white / light yellow
                color[i][j] = white
            else : # r <= sens and g <= sens : # black / dark blue
                color[i][j] = black

    # measure the points' surface, as well as the number of luminous spots
    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            if color[i][j] == white and went[i][j] == 0 :
                nstars += 1
                went[i][j] = 1
                bfs ( i, j, -1 )

    print ( nstars )

    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            if color[i][j] == white :
                pix [ i, j ] = 0, 0, 0
            else :
                pix [ i, j ] = 255, 255, 255

    #data = sorted ( data, key = lambda x: x[0], reverse = True )
    sort_a_list ( nstars, 0 ) # sort the points decreasingly by size

    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            went[i][j] = 0

    #calculating the pollution coefficient based on the mean R and G values for the point ( 66% ), as well as its size ( 33% )
    for i in range ( 0, nstars ) :
        s, cs, ls, red_avg, yel_avg, pc = data [ i ]
        
        pc = ( ( ( red_avg + yel_avg ) / 2 ) / 255 ) * 2 / 3 + ( s / max_surf ) * 1 / 3

        data[i] = ( s, cs, ls, red_avg, yel_avg, pc )
    
        if i < 10 :
            print ( pc )

    # coloring the points by their pollution coefficient
    for i in range ( 0, nstars ) :
        s, cs, ls, red_avg, yel_avg, pc = data [ i ]
        bfs ( cs, ls, int ( pc * 255 ) )

    # print the pollution coefficient if it's bigger than 35%
    for i in range ( 0, nstars ) :
        s, cs, ls, red_avg, yel_avg, pc = data [ i ]

        pc = pc * 9

        if pc - int ( pc ) >= 0.5 :
            pc = int ( pc ) + 1
        else :
            pc = int ( pc )

        if pc >= 4 :
            write_text ( cs, max ( ls - font_size, 0 ), str ( int ( pc ) ), 0 )

    pmin, iss_lat, iss_lon = calc_nearest_city ()

    sort_a_list ( min ( 10, nstars ), 5 ) # sort the points with the biggest surface ( reduces time ) decreasingly by the pollution coefficient

    s, cs, ls, red_avg, yel_avg, pc = data[0]

    country, city, lat, lon, alt = point [ pmin ]

    write_text ( cs, max ( ls - 2 * font_size, 0 ), city.upper (), 0 )

    out = "mid_data/"
    im.save ( out + "image1_" + str ( cyc ) + ".png" )

    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            went[i][j] = 0

    for i in range ( 0, nstars ) :
        data[i] = 0, 0, 0, 0, 0, 0

    max_surf = 0
    nstars = 0
    dat_ind = 0

# 2nd part
def pinpoint_iss ( cyc ) :
    global grd

    im = Image.open ( "initial_data/grid.jpg" )

    im = im.convert ( "RGB" )

    grd = im.load ()
    
    pmin, iss_lat, iss_lon = calc_nearest_city ()
    country, city, lat, lon, alt = point [ pmin ]
    
    lat, lon = latlon2d ( lat, lon )
    
    write_text ( lon, lat, city.upper(), 1 )
    draw_point ( lon, lat, 0, 255, 0 )

    iss_lat, iss_lon = latlon2d ( iss_lat, iss_lon )   
    draw_point ( iss_lon, iss_lat, 255, 0, 0 )

    out = "mid_data/"
    im.save ( out + "image2_" + str ( cyc ) + ".png" )

def iss_latlon () :
    dpr = 180 / math.pi
    
    orig = ephem.Observer ()
    orig.date = datetime.utcnow ()

    iss.compute ()

    iss_lat = iss.sublat * dpr
    iss_lon = iss.sublong * dpr

    bundle = ( iss_lat, iss_lon )
    
    return bundle

def full_data ( cyc ) :
    out = "mid_data/"
    im1 = Image.open ( out + "image1_" + str ( cyc ) + ".png" )
    im2 = Image.open ( out + "image2_" + str ( cyc ) + ".png" )
    im3 = Image.open ( out + "image3_" + str ( cyc ) + ".png" )
    im0 = Image.open ( "photos/" + "photo0_" + str ( cyc ) + ".jpg" )
    im = Image.open ( "initial_data/full_data.png" )

    im = im.convert ( "RGB" )
    im0 = im0.convert ( "RGB" )
    im1 = im1.convert ( "RGB" )
    im2 = im2.convert ( "RGB" )
    im3 = im3.convert ( "RGB" )

    pix = im.load ()
    pix0 = im0.load ()
    pix1 = im1.load ()
    pix2 = im2.load ()
    pix3 = im3.load ()

    x = 640
    y = 480

    for i in range ( 0, x ) :
        for j in range ( 0, y ) :
            pix[ i, j ] = pix0 [ i, j ]

    for i in range ( x, 2 * x ) :
        for j in range ( 0, y ) :
            pix[ i, j ] = pix2 [ i - x, j ]

    for i in range ( 0, x ) :
        for j in range ( y, 2 * y ) :
            pix [ i, j ] = pix1 [ i, j - y ]

    for i in range ( x, 2 * x ) :
        for j in range ( y, 2 * y ) :
            pix [ i, j ] = pix3 [ i - x, j - y ]

    im.save ( "full_data/image" + str ( cyc ) + ".png" )
    im.close ()
    im1.close ()
    im2.close ()
    im3.close ()
    im0.close ()

    for i in range ( 1, 4 ) : # deletes the 3 images that were merged into one previously
        os.remove ( out + "image" + str ( i ) + "_" + str ( cyc ) + ".png" )

camera = PiCamera ()
camera.resolution = ( 640, 480 )

load_font ()

cyc = 0

TIME_START = time.time ()
cyc_time = TIME_START
cyc_time1 = TIME_START
cyc_time2 = 0

z1 = z2 = 0
dif = 0
max_dif = 0
numcyc = 150

iss_lat1, iss_lon1 = iss_latlon ()

vibr_height = [ 8 for i in range ( 0, 8 ) ]

while cyc_time - TIME_START < 10800 : # 10800
    # accelerometer
    orientation = sense.get_accelerometer_raw ()
    z2 = orientation["z"]
  
    dif = z2 - z1
    if dif > max_dif :
        max_dif = dif

    for i in range ( 0, 7 ) :
        vibr_height[i] = vibr_height[ i + 1 ]
    
    i = 7
    while ( 8 - i ) * 0.02 <= dif and i >= 4 :
      sense.set_pixel ( 7, i, blue )
      i -= 1

    vibr_height[7] = i + 1

    while i >= 4 :
      sense.set_pixel ( 7, i, 0, 0, 0 )
      i -= 1

    for i in range ( 0, 7 ) :
        j = 7
        while j >= vibr_height[i] :
            sense.set_pixel ( i, j, blue )
            j -= 1

        while j > 0 :
            sense.set_pixel ( i, j, 0, 0, 0 )
            j -= 1

    z1 = z2

    # humidity, temperature, pressure, speed + light pollution, localisation
    if cyc % numcyc == 0 :
        sense.set_pixel ( 0, 0, 0, 255, 0 )

        sense.set_pixel ( 1, 0, yellow ) # taking a picture

        camera.capture ( "photos/photo0_" + str ( int ( cyc / numcyc ) ) + ".jpg" )

        sense.set_pixel ( 1, 0, 0, 0, 0 ) # finished taking the picture
        
        print ( cyc / numcyc )
        
        hmd = int ( sense.get_humidity () )
        tmp = int ( sense.get_temperature () )
        prs = int ( sense.get_pressure () )

        vibr = max_dif
        max_dif = 0
        
        iss_lat2, iss_lon2 = iss_latlon ()
        dist = calcdist ( iss_lat1, iss_lon1, iss_lat2, iss_lon2 )

        cyc_time1 = cyc_time2
        cyc_time2 = time.time ()
        
        spd = dist / ( cyc_time2 - cyc_time1 )

        print ( spd )
        
        iss_lat1 = iss_lat2
        iss_lon1 = iss_lon2

        light_pollution ( int ( cyc / numcyc ) )
        pinpoint_iss ( int ( cyc / numcyc ) )
        sense_data ( int ( cyc / numcyc ), hmd, tmp, prs, vibr, spd, iss_lat2, iss_lon2, cyc_time2 - TIME_START )

        full_data ( int ( cyc / numcyc ) )
    else :
        sense.set_pixel ( 0, 0, 255, 0, 0 ) 
        
    cyc += 1
    cyc_time = time.time ()

sense.clear ()

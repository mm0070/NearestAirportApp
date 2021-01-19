CREATE TABLE public.airportsList (
    ICAO varchar(255) PRIMARY KEY,
    Type varchar(255),
    Name varchar(255),
    LAT float,
    LON float,
    Elevation int,
    Country varchar(255),
    Region varchar(255)
);

COPY airportsList FROM '/db/airports.csv' DELIMITER ',' CSV HEADER;
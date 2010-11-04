/*Sample SQL for freespan to LPA*/
SELECT 
    freespan.easting, 
    freespan.northing,
    @lpa_easting := (SELECT Easting FROM lpa_table WHERE freespan.easting <= Easting LIMIT 1) AS lpa_easting,
    (SELECT Northing FROM lpa_table WHERE freespan.easting <= Easting LIMIT 1) AS lpa_northing, 
    (SELECT KP FROM lpa_table WHERE freespan.easting <= Easting LIMIT 1) AS kp,
    @lpa_easting2 := (SELECT Easting FROM lpa_table WHERE freespan.easting >= Easting ORDER BY Easting desc LIMIT 1) AS lpa_easting2,
    (SELECT Northing FROM lpa_table WHERE freespan.easting >= Easting ORDER BY Easting desc LIMIT 1) AS lpa_northing2, 
    (SELECT KP FROM lpa_table WHERE freespan.easting >= Easting ORDER BY Easting desc LIMIT 1) AS kp2,
    IF(
        ABS(freespan.easting - @lpa_easting) < ABS(freespan.easting - @lpa_easting2 ),
        (SELECT KP FROM lpa_table WHERE freespan.easting <= Easting LIMIT 1),
        (SELECT KP FROM lpa_table WHERE freespan.easting >= Easting ORDER BY Easting desc LIMIT 1)
    ) AS nearest_kp,
    LEAST(
        ABS(freespan.easting - @lpa_easting),
        ABS(freespan.easting - @lpa_easting2 )
    ) AS diff
FROM freespan freespan 

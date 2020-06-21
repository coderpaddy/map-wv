counties = {
    "All": "-1",
    "1-Barbour": "1",
    "2-Berkeley": "2",
    "3-Boone": "3",
    "4-Braxton": "4",
    "5-Brooke": "5",
    "6-Cabell": "6",
    "7-Calhoun": "7",
    "8-Clay": "8",
    "9-Doddridge": "9",
    "10-Fayette": "10",
    "11-Gilmer": "11",
    "12-Grant": "12",
    "13-Greenbrier": "13",
    "14-Hampshire": "14",
    "15-Hancock": "15",
    "16-Hardy": "16",
    "17-Harrison": "17",
    "18-Jackson": "18",
    "19-Jefferson": "19",
    "20-Kanawha": "20",
    "21-Lewis": "21",
    "22-Lincoln": "22",
    "23-Logan": "23",
    "24-Marion": "24",
    "25-Marshall": "25",
    "26-Mason": "26",
    "27-McDowell": "27",
    "28-Mercer": "28",
    "29-Mineral": "29",
    "30-Mingo": "30",
    "31-Monongalia": "31",
    "32-Monroe": "32",
    "33-Morgan": "33",
    "34-Nicholas": "34",
    "35-Ohio": "35",
    "36-Pendleton": "36",
    "37-Pleasants": "37",
    "38-Pocahontas": "38",
    "39-Preston": "39",
    "40-Putnam": "40",
    "41-Raleigh": "41",
    "42-Randolph": "42",
    "43-Ritchie": "43",
    "44-Roane": "44",
    "45-Summers": "45",
    "46-Taylor": "46",
    "47-Tucker": "47",
    "48-Tyler": "48",
    "49-Upshur": "49",
    "50-Wayne": "50",
    "51-Webster": "51",
    "52-Wetzel": "52",
    "53-Wirt": "53",
    "54-Wood": "54",
    "55-Wyoming": "55",
}


def get_refiner():
    refiner = {}
    for x in range(100):
        if x == 0:
            refiner[x] = {
                "min_value": "1",
                "max_value": "10001",
            }
        else:
            refiner[x] = {
                "min_value": f"{x}0001",
                "max_value": f"{x + 1}0001",
            }
    return refiner

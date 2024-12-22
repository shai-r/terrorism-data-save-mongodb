from app.utils.num_util import convert_to_int, convert_to_float


def transform_data_to_record(raw_data):
    return [{
        "event_id": row["eventid"],
        "date": {
            "year": convert_to_int(row["iyear"]),
            "month": convert_to_int(row["imonth"]),
            "day": convert_to_int(row["iday"]),
        },
        "location": {
            "country": {"code": convert_to_int(row["country"]), "text": row["country_txt"]},
            "region": {"code": convert_to_int(row["region"]), "text": row["region_txt"]},
            "state": row.get("provstate"),
            "city": row.get("city"),
            "latitude": convert_to_float(row.get("latitude")),
            "longitude": convert_to_float(row.get("longitude")),
        },
        "weapons": [
            {
                "type": {
                    "code": convert_to_int(row[f"weaptype{i}"]),
                    "text": row[f"weaptype{i}_txt"]
                },
                "subtype": {
                    "code": convert_to_int(row.get(f"weapsubtype{i}")),
                    "text": row.get(f"weapsubtype{i}_txt"),
                },
            }
            for i in range(1, 5)
            if row.get(f"weaptype{i}") and row.get(f"weaptype{i}_txt")
        ],
        "casualties": {
            "killed": convert_to_int(row.get("nkill")),
            "wounded": convert_to_int(row.get("nwound")),
            "details": {
                "us_killed": convert_to_int(row.get("nkillus")),
                "terrorists_killed": convert_to_int(row.get("nkillter")),
                "us_wounded": convert_to_int(row.get("nwoundus")),
                "terrorists_wounded": convert_to_int(row.get("nwoundte")),
            },
        },
        "groups": [
            {
                "name": row.get(f"gname{i if i > 1 else ""}"),
                "subname": row.get(f"gsubname{i if i > 1 else ""}"),
            }
            for i in range(1, 4)
            if row.get(f"gname{i if i > 1 else ""}")
        ],
        "targets": [
            {
                "type": {"code": convert_to_int(row[f"targtype{i}"]), "text": row[f"targtype{i}_txt"]},
                "subtype": {
                    "code": convert_to_int(row.get(f"targsubtype{i}")),
                    "text": row.get(f"targsubtype{i}_txt"),
                },
                "details": row.get(f"target{i}"),
                "nationality": {
                    "code": convert_to_int(row.get(f"natlty{i}")),
                    "text": row.get(f"natlty{i}_txt"),
                },
            }
            for i in range(1, 4)
            if row.get(f"targtype{i}") and row.get(f"targtype{i}_txt")
        ],
        "attack_type": {
            "primary": {"code": convert_to_int(row["attacktype1"]), "text": row["attacktype1_txt"]},
            "secondary": {
                "code": convert_to_int(row.get("attacktype2")),
                "text": row.get("attacktype2_txt"),
            },
            "tertiary": {
                "code": convert_to_int(row.get("attacktype3")),
                "text": row.get("attacktype3_txt"),
            },
        },
        "perpetrators": {
            "count": convert_to_int(row.get("nperps")),
            "captured": convert_to_int(row.get("nperpcap")),
        },
    }  for row in raw_data ]

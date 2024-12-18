def transform_row_to_record(raw_data):
    return [{
        "event_id": row["eventid"],
        "date": {
            "year": row["iyear"],
            "month": row["imonth"],
            "day": row["iday"],
        },
        "location": {
            "country": {"code": row["country"], "text": row["country_txt"]},
            "region": {"code": row["region"], "text": row["region_txt"]},
            "state": row.get("provstate"),
            "city": row.get("city"),
            "latitude": row.get("latitude"),
            "longitude": row.get("longitude"),
        },
        "weapons": [
            {
                "type": {"code": row[f"weaptype{i}"], "text": row[f"weaptype{i}_txt"]},
                "subtype": {
                    "code": row.get(f"weapsubtype{i}"),
                    "text": row.get(f"weapsubtype{i}_txt"),
                },
            }
            for i in range(1, 5)
            if row.get(f"weaptype{i}") and row.get(f"weaptype{i}_txt")
        ],
        "casualties": {
            "killed": row.get("nkill"),
            "wounded": row.get("nwound"),
            "details": {
                "us_killed": row.get("nkillus"),
                "terrorists_killed": row.get("nkillter"),
                "us_wounded": row.get("nwoundus"),
                "terrorists_wounded": row.get("nwoundte"),
            },
        },
        "groups": [
            {
                "name": row.get(f"gname{i}"),
                "subname": row.get(f"gsubname{i}"),
            }
            for i in range(1, 4)
            if row.get(f"gname{i}")
        ],
        "targets": [
            {
                "type": {"code": row[f"targtype{i}"], "text": row[f"targtype{i}_txt"]},
                "subtype": {
                    "code": row.get(f"targsubtype{i}"),
                    "text": row.get(f"targsubtype{i}_txt"),
                },
                "details": row.get(f"target{i}"),
                "nationality": {
                    "code": row.get(f"natlty{i}"),
                    "text": row.get(f"natlty{i}_txt"),
                },
            }
            for i in range(1, 4)
            if row.get(f"targtype{i}") and row.get(f"targtype{i}_txt")
        ],
        "attack_type": {
            "primary": {"code": row["attacktype1"], "text": row["attacktype1_txt"]},
            "secondary": {
                "code": row.get("attacktype2"),
                "text": row.get("attacktype2_txt"),
            },
            "tertiary": {
                "code": row.get("attacktype3"),
                "text": row.get("attacktype3_txt"),
            },
        },
        "perpetrators": {
            "count": row.get("nperps"),
            "captured": row.get("nperpcap"),
        },
    }  for row in raw_data ]
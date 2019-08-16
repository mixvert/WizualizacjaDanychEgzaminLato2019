miesiace = {"styczeń": 31, "luty": 28, "marzec": 31,
            "kwiecień": 30, "maj": 31, "czerwiec": 30,
            "lipiec": 31, "sierpień": 31, "wrzesień": 30,
            "październik": 31, "listopad": 30, "grudzień": 31}

for k, v in miesiace.items():
    if v == 30:
        print(k)

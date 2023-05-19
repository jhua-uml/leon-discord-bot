def getMaxDay(dict):
    return max(dict, key=dict.get)

def getDayIcon(day_str):
    match day_str:
        case 'mon_cnt':
            return '<:mon:1075213992550731877> ``Monday'
        case 'tue_cnt':
            return '<:tue:1075214017540399214> ``Tuesday'
        case 'wed_cnt':
            return '<:wed:1075217903546269797> ``Wednesday'
        case 'thu_cnt':
            return '<:thu:1075246801118036020> ``Thursday'
        case 'fri_cnt':
            return '<:fri:1075246796357521428> ``Friday'
        case 'sat_cnt':
            return '<:sat:1075246797934563350> ``Saturday'
        case 'sun_cnt':
            return '<:sun:1075246799838773298> ``Sunday'
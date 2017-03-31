def wx(place_identifier):
    import geocoder

    g = geocoder.google(place_identifier)
    if not len(g.latlng):
        return 'where to heck'

    import requests

    lat,lng = g.latlng

    r = requests.get('https://api.darksky.net/forecast/e656f2d2a411c5c0503726efb6076680/{0},{1}'.format(lat,lng))

    if r.status_code != 200:
        return 'oops'

    wthr = r.json()
    currently = wthr['currently']

    return '\x0308{0}: \x03{1} \x0309{2}°F\x03'.format(
        g.address,
        currently['summary'],
        int(currently['temperature']),
        )

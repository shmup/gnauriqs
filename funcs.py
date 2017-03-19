import contrib.irc as irc


'''
{
    'time': datetime.now(),
    'nick': NICK,
    'admins': ADMINS,
    'raw': '',
}
'''

def cmd_process(raw_data):
    channels = ['#tarpit']
    data = irc.parseirc(raw_data)
    if data['parsed']['to'] not in channels:
        return
    msg = data['parsed']['msg']
    parts = msg.split(' ')
    preface = parts[0]

    if preface == 'wx':
        return wx(parts)


def wx(data):
    if len(data) < 2:
        return

    import geocoder
    import requests

    g = geocoder.google(' '.join(data[1:]))
    if not len(g.latlng):
        return ['PRIVMSG #tarpit :{0}'.format('where to heck')]

    lat,lng = g.latlng

    r = requests.get('https://api.darksky.net/forecast/e656f2d2a411c5c0503726efb6076680/{0},{1}'.format(lat,lng))

    if r.status_code != 200:
        return ['PRIVMSG #tarpit :{0}'.format('oops')]

    wthr = r.json()
    currently = wthr['currently']

    return ['PRIVMSG #tarpit :\x0308{0}: \x03{1} \x0309{2}°F\x03'.format(
        g.address,
        currently['summary'],
        int(currently['temperature']),
        )]

import contrib.irc as irc


'''
{
    'time': datetime.now(),
    'nick': NICK,
    'admins': ADMINS,
    'raw': '',
}
'''

def send(target, msg):
    return ['PRIVMSG {0} :{1}'.format(target, msg)]


def cmd_process(raw_data):
    channels = ['#tarpit']
    data = irc.parseirc(raw_data)['parsed']
    if data['to'] not in channels:
        return
    parts = data['msg'].split(' ')
    chan = '#tarpit'

    # weather
    if parts[0] == 'wx':

        if len(parts) < 2:
            return send(data['to'], 'where to heck')

        from modules import weather
        return send(data['to'], weather.wx(' '.join(parts[1:])))

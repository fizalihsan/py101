import json
import urllib

testfile = urllib.URLopener()
download_location = '/Users/maryam/Fizal/HifzTracker/AudioMP3/AlAfasy/'

for surah_index in range(1, 115):
    url = 'http://api.alquran.cloud/surah/{0}/ar.alafasy'.format(surah_index)

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    for ayah in data['data']['ayahs']:
        audio_url = ayah['audio']
        file_name = "{0}{1:03d}_{2:03d}.mp3" \
            .format(download_location, surah_index, ayah['numberInSurah'])
        print 'Downloading ' + file_name
        testfile.retrieve(audio_url, file_name)

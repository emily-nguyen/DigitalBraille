import httplib
import json
import urllib

def image_to_text(image_url):
    '''Returns a list of words using OCR on the image to parse the text'''

    api_key = 'cb34dfdea76b4a44a25f8695c3455584'

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key
    }

    params = urllib.urlencode({
        # Language unk = automatically detect the language
        'language': 'unk',
        'detectOrientation': 'true'
    })

    body = str({'url': image_url})

    try: 
        text = []
        connection = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        connection.request('POST', '/vision/v1.0/ocr?%s' % params, body, headers)
        response = connection.getresponse()
        data = json.loads(response.read())

        lines = data['regions'][0]['lines']

        for i in lines:
            words = i['words']

            for j in words:
                word = j['text']

                text.append(word)
 
        connection.close()

        return ' '.join(text)
    except Exception as e:
        print e

# Used for Braille API
BRAILLE_END_POINT = 'http://api.funtranslations.com/translate/'
BRAILLE_API_KEY =  'X-FunTranslations-Api-Secret'

def text_to_braille(text, output_type):
    '''Returns a list of translated text into braille (i.e. dots, images)'''
    headers = {
        'Content-Type': 'application/json',
        'api_key': BRAILLE_API_KEY
    }

    params = urllib.urlencode({
        'text': text
    })

    try: 
        connection = httplib.HTTPSConnection('api.funtranslations.com')
        connection.request('POST', '/translate/braille/{0}.json?{1}{2}{3}'.format(output_type, 
            params, '', headers))
        response = connection.getresponse()
        data = json.loads(response.read())
        error_message = data.get('error', {}).get('message', '')

        if len(error_message) > 0:
            print error_message
            return

        contents = data.get('contents', {}).get('translated', [])
 
        connection.close()

        # Filter out '\r' and '\n'
        return list(filter(lambda x: (x not in ['\r', '\n']), contents))
    except Exception as e:
        print e

def braille_dots(text):
    '''Returns a list of translated text into braille dots'''
    result = text_to_braille(text, 'dots')

    with open('dots.json', 'w') as f:
        json.dump(result, f)

    return result

def braille_image(text):
    '''Returns a list of translated text into braille images'''   
    result = text_to_braille(text, 'image')

    with open('image.json', 'w') as f:
        json.dump(result, f)

    return result

if __name__ == '__main__':
    # Image to Text
    #print image_to_text('https://lh4.ggpht.com/rptGO2VdZ82IHqgeUkcU7eXL1zL3bwLUr0dDsijJSnYcj7qxtSnAi7A0XR1MzmMccA=w300')
    '''
    This is a lot of 12 point text to test the ocr code and see if it works on all types of 
    file format.
    The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy
    fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the
    laxy fox.
    ''' 
    #print image_to_text('http://jeroen.github.io/images/testocr.png')

    #print braille_image('Fun Translations has something for everyone.')
    #print braille_dots('Image to Text')
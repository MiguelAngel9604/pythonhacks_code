
import tempfile
import json

#Create a temp file in order to use the path
temp = tempfile.NamedTemporaryFile(prefix="arctictravelcompany")

                #lighthouse_call = os.popen('lighthouse https://arctictravelcompany.com/ --chrome-flags="--headless" --only-audits=bypass,color-contrast,document-title,duplicate-id-active,duplicate-id,html-has-lang,html-lang-valid,image-alt,label,link-name,list,listitem,'+
                #'meta-viewport,is-on-https,uses-http2,uses-passive-event-listeners,no-document-write,external-anchors-use-rel-noopener,geolocation-on-start,doctype,no-vulnerable-libraries,notification-on-start,deprecations,password-inputs-can-be-pasted-into,errors-in-console,image-aspect-ratio,'
                #+'first-contentful-paint,first-meaningful-paint,speed-index,interactive,first-cpu-idle,'+
                #'load-fast-enough-for-pwa,works-offline,installable-manifest,redirects,viewport,service-worker,without-javascript,splash-screen,themed-omnibox,'+
                #'meta-description,http-status-code,link-text,is-crawlable,robots-txt,hreflang,font-size,plugins '+
                #'--disable-storage-reset=true --preset=desktop --output=json --output-path='+temp.name)

                #time.sleep(60)

#In order to have the file converted in JSON we have to follow the next steps:
#1.- Save the temp file in a variable, the temp file is not allow to be converted to JSON (the new file will be a dictionary)
json_temp=json.load(temp)
#2.- Create a string object by using the dictionary
json_string_obj = json.dumps(json_temp) 
#3.- Convert that string to JSON
loaded_json = json.loads(json_string_obj)

#4.- Finally you will be able to access to the JSON file by using the fields on it
data_feed_json = [{
    'fetch_time' : loaded_json['fetchTime'],
    'site_url' : loaded_json['finalUrl'],
    'site_id' : 1,
    'user_agent' :loaded_json['userAgent'],
    'emulated_as' : loaded_json['configSettings']['formFactor']

}]

print(data_feed_json)
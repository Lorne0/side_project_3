from flask import Flask, request, render_template, redirect
import hashlib

app = Flask(__name__)

uh_dic = {}
hu_dic = {}

@app.route('/', methods=['GET','POST'])
def url_input():
    if request.method == 'POST':
        url = request.values['user_url']
        print("URL", url)
        sha256 = hashlib.sha256()
        sha256.update(url.encode('utf-8'))
        hash_value = sha256.hexdigest()[:7]

        uh_dic[url] = hash_value
        hu_dic[hash_value] = url

        hash_url = request.host_url + 'r/' + hash_value

        # return 'This is user url: ' + hash_value
        return render_template('main.html', hash_url=hash_url)
    return render_template('main.html')

@app.route('/r/<hash_value>')
def url_redirect(hash_value):
    url = hu_dic[hash_value]
    if url[:4] != 'http':
        url = 'http://' + url
    return redirect(url)
    

if __name__ == '__main__':
    app.debug = True
    app.run()

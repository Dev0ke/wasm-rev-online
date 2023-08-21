from flask import *  
from os import system
from hashlib import sha256

app=Flask(__name__)    
app.secret_key = 'devoke'
app._static_folder = "./templates/static"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件的最大大小为 16MB

input_folder = "./input/"
output_folder = "./output/"


def sha(filename):
    sha = sha256()
    sha.update(filename.encode())
    return sha.hexdigest()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['fileToUpload']
    session['uploaded_filename'] = file.filename
    filename_sha = sha(file.filename)
    file.save(input_folder + filename_sha)
    return render_template("index.html",filename=session['uploaded_filename']) 

@app.route('/process', methods=['POST'])
def process():
    filename = session.get('uploaded_filename')
    if filename:
        filename_sha = sha(filename)
        output = ''
        if request.form['action'] == 'wasm2c':
            output = run_wasm2c(filename_sha)
            f = open(output)
            data = f.read()
            return render_template("index.html",filename=session['uploaded_filename'], code=data)
        elif request.form['action'] == 'decompile':
            pass
        else:
            result = 'unexcepted action'
    else:
        return 'please upload first'

def run_wasm2c(filename):
    outputfile = output_folder + filename
    cmd = ["./bin/wasm2c",input_folder + filename,"-o",outputfile]
    system(" ".join(cmd))
    return outputfile
    



if __name__=="__main__":
    app.run(port=5000,host="127.0.0.1",debug=False)   #调用run方法，设定端口号，启动服务
    
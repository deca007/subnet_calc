from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        site_name = request.form['site_name']
        subnet = request.form['subnet']
        br01_lo1 = request.form['br01_lo1']
        br01_lo2 = request.form['br01_lo2']
        br02_lo1 = request.form['br02_lo1']
        br02_lo2 = request.form['br02_lo2']
        dc_type = request.form['dc_type']
        racks = request.form['racks']

        return render_template('form2.html', site_name=site_name,dc_type=dc_type,subnet=subnet,loop1=br01_lo1,racks=racks)

    return render_template('form1.html')
if __name__=='__main__':
    app.run(debug=True)
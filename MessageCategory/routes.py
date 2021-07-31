from MessageCategory import app

from flask import render_template, request, redirect, url_for

from wtforms import Form, StringField, validators

import json, plotly
import pickle

from visualization.viz import return_figures, load_data



Pkl_Filename = "./models/message_category.pkl"  

with open(Pkl_Filename, 'rb') as file:  
    Model = pickle.load(file)

# load the dataset
df = load_data()

print(df.columns)
print(df['offer'].sum())


def charts():
	figures = return_figures()

	# plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
	return ids, figuresJSON

class QueryForm(Form):
    
    query = StringField('', [validators.Length(min=5, max=150)])


@app.route('/', methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
	form = QueryForm(request.form)
	
	ids, figuresJSON = charts()
	
	return render_template('master.html',
	                       ids=ids,
	                       figuresJSON=figuresJSON, form=form)


@app.route('/go', methods=['POST'])
def go():
	form = QueryForm(request.form)

	if request.method == 'POST' and form.validate():
		query = form.query.data
		predict = Model.predict([query])[0]
		columns_name = df.columns[5:]

		classification_results = dict(zip(columns_name, predict))

		return render_template('go.html',form=form, 
		classification_results=classification_results)
	else:
		ids, figuresJSON = charts()

		return render_template('master.html',
	                       ids=ids,
	                       figuresJSON=figuresJSON, form=form)

import pandas as pd
import sqlite3
import plotly.graph_objs as go


def load_data():
	con = sqlite3.connect('./Data/messages_categories.db')
	try:
		df = pd.read_sql_query("""SELECT * FROM messages_categories""", con)
	except Exception as e:
		return (e)
	
	return df




def return_figures():
	df = load_data()

# first bar chart for Genre
	graph_one = []

	# x_val = df.genre.value_counts().index
	x_val = ['News', 'Direct', 'Social']
	y_val = df.genre.value_counts().values

	graph_one.append(
          go.Bar(
          x = x_val,
          y = y_val,
        )

	    
	)

	layout_one = dict(title = 'Genres Count',
 		        xaxis = dict(title = 'Genre',),
                yaxis = dict(title = 'Count'),

    )	

# append all charts to the figures list
	figures = []
	figures.append(dict(data=graph_one, layout=layout_one))
	return figures
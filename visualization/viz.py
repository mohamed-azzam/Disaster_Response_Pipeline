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

# second bar chart for top 10 categories
	graph_two = []

	x_val = []
	y_val = []

	for i in df.columns[5:]:
		x_val.append(i)
		y_val.append(df[i].sum())

	y_val, x_val = zip(*sorted(zip(y_val, x_val)))

	graph_two.append(
          go.Bar(
          x = x_val[::-1][:10],
          y = y_val[::-1][:10],
        )

	    
	)

	layout_two = dict(title = 'Top 10 Categories Count',
 		        xaxis = dict(title = 'Category',),
                yaxis = dict(title = 'Count'),

    )	

# append all charts to the figures list
	figures = []
	figures.append(dict(data=graph_one, layout=layout_one))
	figures.append(dict(data=graph_two, layout=layout_two))
	return figures
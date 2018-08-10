import datetime as dt
import pandas as pd
import seaborn as sns

sns.set(style='whitegrid', rc={"grid.linewidth": 0.1})
sns.set_context("paper", font_scale=0.9)                                                                                                                                                                                                                                                                                 
color = sns.color_palette("Set2", 6)

today_date = str(dt.datetime.now().strftime("%d-%m-%y"))
gr = pd.read_csv('Mini_outputs/Report_for_'+today_date+'.csv')
sns_plot = sns.barplot(x=gr['Time'], y=gr['Count'])
fig = sns_plot.get_figure()
fig.savefig("output_"+today_date+".png")
html_content ='''<!DOCTYPE html>
<html>
	<head>
		<title>Person Count Analysis</title>
	</head>
	<body>
		<center>
			<h2>Report for {0}</h2>	
			<hr/>
			<p> <img src="{1}" alt="Report_Barplot"></p>
				<p>The Total people entered in:		{2}</p>
				<p>The Maximum people for a period:	{3}</p>
				<p>The Maximum people in a period:	{4}</p>
		</center>
	</body>
</html>'''.format(today_date,"output_"+today_date+".png",gr['Count'].sum(),gr['Count'].max(),
					gr[gr.Count == gr['Count'].max()]['Time'].tolist())

f = open('report_for_'+today_date+'.html','w')
f.write(html_content)
f.close()